def nota_media(a, b, c):
    media = (a + b + c) / 3.0
    estado = 'aprobado' if media >= 5 else 'suspenso'
    return media, estado # Devuelve una tupla (media, estado)