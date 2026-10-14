"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""
dias = ['Lunes', 'Martes','Miercoles', 'Jueves','Viernes']
ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000
# TODO: calcula total, cantidad, mayor y menor para Centro.
total_centro = sum(ventas_centro) # Total de ventas semanal
cantidad_centro = len(ventas_centro)# Cantidad de dias registrados
menor_centro = min(ventas_centro) # Venta minima de la Tienda del Centro
mayor_centro = max(ventas_centro) #  Venta maxima de la Tienda del Centro

# TODO: calcula promedio, rango, diferencia y porcentaje para Centro.

promedio_centro = total_centro / cantidad_centro #Promedio ventas diario
porcentaje_centro = (total_centro * 100 / meta_centro) #

# TODO: repite los indicadores para Norte.
total_norte = sum(ventas_norte) # Total de ventas semanal
cantidad_norte = len(ventas_norte)# Cantidad de dias registrados
menor_norte = min(ventas_norte) # Venta minima de la Tienda del Centro
mayor_norte = max(ventas_norte) #  Venta maxima de la Tienda del Centro
dia_mayor = dias[ventas_centro.index(mayor_centro)] #El dia que se hizo mas ventas
print(dia_mayor, mayor_centro)

promedio_norte = total_norte / cantidad_norte #Promedio ventas diario
porcentaje_norte = (total_norte * 100 / meta_norte) #

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.
if total_centro > meta_centro:
    estado_centro = 'Meta superada'
elif  total_centro == meta_centro:
    estado_centro = 'Meta alcanzada'
else:
    estado_centro = 'Meta NO alcanzada'


if total_norte > meta_norte:
    estado_norte = 'Meta superada'
elif  total_norte == meta_norte:
    estado_norte = 'Meta alcanzada'
else:
    estado_norte = 'Meta NO alcanzada'




# TODO: compara los totales y los rangos.

if total_centro > total_norte:
    tienda_mayor_ventas = 'Tienda del Centro'
elif total_norte > total_centro:
    tienda_mayor_ventas = 'Tienda del Norte'
else:
    tienda_mayor_ventas = 'Ambas tiendas tienen el mismo total'

# TODO: presenta un reporte con etiquetas claras y f-strings.

print('COMPARACION SEMANAL DE TIENDAS')
print("-" * 70)
print(f"Centro | total:  ₡{total_centro:,.2f} | meta: ₡{meta_centro:,.2f} |  cumplimiento {porcentaje_centro:.0f}% ")
print(f"Centro logro: {estado_centro}\n")
print(f"Norte | total:  ₡{total_norte:,.2f} | meta: ₡{meta_norte:,.2f} |  cumplimiento {porcentaje_norte:.0f}% ")
print(f"Norte logro: {estado_norte}\n")
print(f"Tienda con mayor ventas: {tienda_mayor_ventas}\n")
# TODO: escribe las tres conclusiones solicitadas en la guía.
