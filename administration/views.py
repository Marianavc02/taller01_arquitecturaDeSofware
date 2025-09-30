from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import ComputerLog


from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

from .models import Alert, Computer
from .ComputerForm import ComputerForm   
from .repositories import DjangoORMComputerRepository
from .factories import AlertFactory
from .google_sheets import GoogleSheet

import os
import json

# ====================
# Configuración Google
# ====================
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'credenciales.json')
SCOPES = ['https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build('drive', 'v3', credentials=credentials)

file_name_gs = "credenciales.json"
google_sheet = "Datos SafeDesk"
google_sheet_fotos = "Datos faciales Safedesk"
sheet_name = "Hoja 1"


# Utilidades

def es_admin(user):
    return user.is_superuser or user.groups.filter(name='admin').exists()


def buscar_id_por_nombre(nombre_archivo, carpeta_id=None):
    query = f"name = '{nombre_archivo}'"
    if carpeta_id:
        query += f" and '{carpeta_id}' in parents"
    resultados = service.files().list(q=query, fields="files(id, name)").execute()
    archivos = resultados.get('files', [])
    if archivos:
        return archivos[0]['id']
    return None

# Vistas Google

def update_photos(request):
    google = GoogleSheet(file_name_gs, google_sheet_fotos, sheet_name)
    photo_data = google.get_last_row()
    if photo_data and len(photo_data) >= 2:
        id_archivo = buscar_id_por_nombre(photo_data[0])
        id_reconocido = buscar_id_por_nombre(photo_data[1])
        return JsonResponse({'id_archivo': id_archivo, 'id_reconocido': id_reconocido})
    return JsonResponse({'error': 'No se encontró la foto'}, status=404)

def alerts(request):
    return render(request, 'administration/alerts.html')

def alertas_json(request):
    google = GoogleSheet(file_name_gs, google_sheet, sheet_name)
    alertas = google.get_all_values()
    return JsonResponse(alertas, safe=False)

def update_alert(request):
    alerta_data = ["2025-09-26", "Intruso detectado", "Activo"]
    alerta = AlertFactory.create_alert("intrusion", alerta_data[1], alerta_data[2], alerta_data[0])
    alerta.save()
    return JsonResponse({"msg": "Alerta registrada"})


# Vistas de Computadoras (CBV)

class ComputerListView(LoginRequiredMixin, ListView):
    model = Computer
    template_name = 'administration/computer_list.html'
    context_object_name = 'computadoras'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['is_admin'] = self.request.user.groups.filter(name='admin').exists()
        return ctx

class ComputerCreateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = Computer
    form_class = ComputerForm
    template_name = 'administration/computer_form.html'
    success_url = reverse_lazy('computadoras')
    success_message = "Computadora registrada correctamente."

    def test_func(self):
        return es_admin(self.request.user)

class ComputerUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Computer
    form_class = ComputerForm
    template_name = 'administration/computer_form.html'
    success_url = reverse_lazy('computadoras')
    success_message = "Computadora actualizada correctamente."

    def test_func(self):
        return es_admin(self.request.user)

class ComputerDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Computer
    template_name = 'administration/computer_confirm_delete.html'
    success_url = reverse_lazy('computadoras')
    success_message = "Computadora eliminada correctamente."

    def test_func(self):
        return es_admin(self.request.user)
    
class ComputerLogListView(ListView):
    model = ComputerLog
    template_name = 'administration/computer_logs.html'
    context_object_name = 'logs'
    ordering = ['-timestamp']
    