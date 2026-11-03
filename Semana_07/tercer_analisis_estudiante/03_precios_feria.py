"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]
indice = 0
superan_promedio = 0
promedio = 0
# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
#for precio in precios:
    
total = sum(precios)
promedio = total / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo

# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.    
while indice < len(precios): 
    if precios[indice] > promedio:
            superan_promedio += 1
    indice += 1

# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >= 300:
      clasificacion = 'Variacion alta'
elif rango >= 150:
      clasificacion = 'Moderada'
else:
      clasificacion = 'Baja'

# TODO: Muestre producto y todos los resultados.
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.

print('Producto: ',producto)
print('Promedio: ₡',promedio)
print('Minimo: ₡',minimo)
print('Maximo: ₡',maximo)
print('Rango: ₡',rango)
print(f'{superan_promedio} precios sobre el promedio')
print(clasificacion)