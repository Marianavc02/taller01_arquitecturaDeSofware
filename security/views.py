from django.shortcuts import render,redirect
from django.http import HttpResponse
from administration.ComputerForm import ComputerForm 


def registrar_computadora(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_computadoras')  # Reemplaza con tu URL correcta
    else:
        form = ComputerForm()
    return render(request, 'security/registrar_computadora.html', {'form': form})