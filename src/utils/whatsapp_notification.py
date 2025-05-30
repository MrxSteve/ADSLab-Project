from twilio.rest import Client
from flask import current_app


def enviar_mensaje_whatsapp(mensaje, numero_destino):
    client = Client(
        current_app.config['TWILIO_ACCOUNT_SID'],
        current_app.config['TWILIO_AUTH_TOKEN']
    )

    message = client.messages.create(
        from_=current_app.config['TWILIO_WHATSAPP_NUMBER'],
        body=mensaje,
        to=f'whatsapp:{numero_destino}'
    )

    return message.sid
