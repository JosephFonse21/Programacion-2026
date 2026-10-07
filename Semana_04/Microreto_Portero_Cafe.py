"""Microreto: el portero del café."""

energia = int(input('Cuanta energia tienes del 0 al 100: '))
trae_cafe = input("¿Traes café? (si/no): ").strip().lower() == 'si'
mensaje = "Completa las reglas del portero."

# TODO: usa and para detectar energía baja sin café.
if energia < 30 and not(trae_cafe):
    mensaje = 'Denegado el acceso'
# TODO: usa or para permitir energía suficiente o café.
elif energia >= 30 or trae_cafe:
    mensaje = 'Bienvenido,acceso concedido !'
else:
    mensaje = 'Portero confundido, revisa las respuestas'


# TODO: escribe mensajes claros para cada resultado.

print(mensaje)
