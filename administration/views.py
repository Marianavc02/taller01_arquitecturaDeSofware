from django.http import JsonResponse
from .models import Alert, Computer
from dotenv import load_dotenv
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .import ComputerForm
from .ComputerForm import ComputerForm
from django.shortcuts import get_object_or_404

from google.oauth2 import service_account
from googleapiclient.discovery import build
from .google_sheets import GoogleSheet
from datetime import date
import json
import uuid
import os
# Credenciales para APIs de Google
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'credenciales.json')

SCOPES = ['https://www.googleapis.com/auth/drive']

SERVICE_ACCOUNT_FILE = "credenciales.json"
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)


service = build('drive', 'v3', credentials=credentials)

file_name_gs = "credenciales.json"
google_sheet = "Datos SafeDesk"
google_sheet_fotos = "Datos faciales Safedesk"
sheet_name = "Hoja 1"

def buscar_id_por_nombre(nombre_archivo, carpeta_id=None):
    query = f"name = '{nombre_archivo}'"
    if carpeta_id:
        query += f" and '{carpeta_id}' in parents"

    resultados = service.files().list(q=query, fields="files(id, name)").execute()
    archivos = resultados.get('files', [])

    if archivos:
        return archivos[0]['id']  # El ID del primer archivo que coincida
    return None

def update_photos(request):
    google = GoogleSheet(file_name_gs, google_sheet_fotos, sheet_name)
    photo_data = google.get_last_row()  # Suponiendo que devuelve una lista como [nombre1, nombre2]

    if photo_data and len(photo_data) >= 2:
        id_archivo = buscar_id_por_nombre(photo_data[0])
        id_reconocido = buscar_id_por_nombre(photo_data[1])

        return JsonResponse({
            'id_archivo': id_archivo,
            'id_reconocido': id_reconocido
        })
    else:
        return JsonResponse({'error': 'No se encontró la foto'}, status=404)


def alerts(request):
    return render(request, 'alerts.html')

def alertas_json(request):
    google = GoogleSheet(file_name_gs, google_sheet, sheet_name)
    alertas = google.get_all_values()

    return JsonResponse(alertas, safe=False)

def update_alert(request):
    google = GoogleSheet(file_name_gs, google_sheet, sheet_name)
    alerta_data = google.get_last_row()  # Suponiendo que devuelve una lista

    if alerta_data:
        alerta, created = Alert.objects.get_or_create(pk=1)  # Solo una alerta
        alerta.fecha = alerta_data[0]
        alerta.mensaje = alerta_data[2]
        alerta.estado = alerta_data[3]
        alerta.save()

        return JsonResponse(alerta_data, safe=False)
    else:
        return JsonResponse({'error': 'No se encontró alerta'}, status=404)
    
# Verifica si pertenece al grupo "admin"
def es_admin(user):
    return user.groups.filter(name='admin').exists()

def computers_view(request):
    computadoras = Computer.objects.all()  # Obtener todas las computadoras
    return render(request, 'computers.html', {'computadoras': computadoras})

@login_required
@user_passes_test(es_admin)
def registrar_computadora(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('computadoras')  
    else:
        form = ComputerForm()
    return render(request, 'registrar_computadora.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def eliminar_computadora(request, computadora_id):
    computadora = get_object_or_404(Computer, id=computadora_id)
    computadora.delete()
    return redirect('computadoras')