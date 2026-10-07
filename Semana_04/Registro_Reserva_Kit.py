#Solucion Mision kit seguro
#Autor: Joseph Fonseca V. Fecha: 2026/10/06

nombre = input('Nombre: ').strip().upper()
kit = input('Tipo de kit: ').strip().lower()
autorizacion = input('Tiene autorización (si/ no)?: ').lower().strip() == 'si'
resultado = " "

try:
    cantidad = int(input('Ingrese la cantidad: '))
except ValueError:
    print('Error cantidad inválida, asignada -1')
    cantidad = -1

try:
    dias = int(input('Dias de prestamo: '))
except ValueError:
    print('Error cantidad de dáas inválida, asignado -1')
    dias = -1


if not nombre or kit == ' ' or cantidad < 1 or dias < 1:
    resultado = "Registro rechazado: datos inválidos! "

elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado = f"Solicitud aprobada para {nombre}: {cantidad} kit(s) de {kit}."
elif cantidad > 3 or dias > 7:
    resultado = "Solicitud enviada a revisión! "
else:
    resultado = "Solicitud rechazada: se requiere autorización"
    
print(resultado)