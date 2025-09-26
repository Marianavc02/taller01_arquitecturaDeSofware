# administration/factories.py
from .models import Alert

class AlertFactory:
    @staticmethod
    def create_alert(tipo, mensaje, estado, fecha):
        if tipo == "intrusion":
            return Alert(mensaje=f"[INTRUSION] {mensaje}", estado=estado, fecha=fecha)
        elif tipo == "desconexion":
            return Alert(mensaje=f"[DESCONECTADO] {mensaje}", estado=estado, fecha=fecha)
        else:
            return Alert(mensaje=mensaje, estado=estado, fecha=fecha)
