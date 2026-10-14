producto = ['Café', 5000,20]
descuento = producto[1] * 15 / 100
ingreso_actual = producto[1] * producto[2]
proyeccion = (producto[2] * 20 / 100) + producto[2]
precio_promocional = producto[1] - descuento
ingreso_proyectado = (proyeccion * precio_promocional) - ingreso_actual
ingreso_promocion = ingreso_actual + ingreso_proyectado


if ingreso_proyectado > 0:
    recomendacion = 'Lanzar!!'
else:
    recomendacion = 'No lanzar!'
    
print('ANÁLISIS DE PROMOCIÓN\n')
print(f"Producto: {producto[0]}")
print(f"Precio actual: ₡{producto[1]}")
print(f"Unidades actuales: {producto[2]}")
print(f"Ingreso actual: ₡{ingreso_actual}")
print(f"Descuento: ₡{descuento}")
print(f"Precio promocional: ₡{precio_promocional}")
print(f"Unidades proyectadas: {proyeccion}")
print(f"Ingreso con promoción: ₡{ingreso_promocion}")
print(f"Diferencia: ₡{ingreso_proyectado}")
print(f"RECOMENDACIÓN : {recomendacion}")

    
