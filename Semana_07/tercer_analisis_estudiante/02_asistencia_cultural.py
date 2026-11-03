"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300
total = 0
contador = 0

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
for bloque in asistencias:
    total += bloque
    supera_capacidad = bloque / capacidad * 100
    if supera_capacidad >= 70 and bloque != asistencias[2]:
        contador += 1


# TODO: Calcule el promedio y su porcentaje de ocupación.
promedio = total / len(asistencias)
porcentaje_ocupacion = (promedio / capacidad) * 100

# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.

if porcentaje_ocupacion >= 80:
    clasificacion = 'Ocupación alta'
elif porcentaje_ocupacion >= 50:
    clasificacion = 'Ocupación media'
else:
    clasificacion = 'Ocupación baja'
    
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.

print('Total: ',total)
print('Promedio: ',promedio)
print(f'Porcentaje: {porcentaje_ocupacion}%')
print(f'{contador} Bloques')
print(clasificacion)