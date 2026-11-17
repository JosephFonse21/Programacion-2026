"""Expediente de 12 atenciones ficticias.

Complete lector_csv.py y siga la guía de Semana 09. Cambie ETAPA de 1 a 2
y luego a 3 conforme verifique cada parte con python analisis_atenciones.py.
"""

from lector_csv import cargar_atenciones


ETAPA =  int(input("ingrese la etapa que quieres ver: "))


def explorar_atenciones(atenciones):
    """Recibe la lista de atenciones y muestra el total, los tipos y los campos."""
    # P1. Complete el lector y compruebe el mensaje de archivo faltante.
    print("P1. Archivo leído correctamente.")

    # P2. Cuente las filas con un ciclo. Compruebe que obtuvo 12.
    contador = 0
    for atencion in atenciones:
        contador += 1
    print(contador)

    # P3. Ejemplo listo para ejecutar. Explique qué tipos y campos observa.
    primer_registro = atenciones[0]

    print("Primer registro:", primer_registro)
    print("Tipo de registro:", type(primer_registro))
    print("Campos:", primer_registro.keys())

   


def contar_y_limpiar(atenciones):
    """Recibe la lista de atenciones y muestra los conteos y sus comprobaciones."""
    print("Etapa 2. Complete y compruebe las preguntas 4 a 8.")
    # P4. Cuente los medicamentos tal como aparecen en el CSV con .get().
    # Muestre el contador y su total.
    contador_medicamentos = {}
    contador_texto_normal = 0

    for atencion in atenciones:
        medicamento = atencion.get("medicamento", "")
        contador_medicamentos[medicamento] = contador_medicamentos.get(medicamento, 0) + 1
        contador_texto_normal += 1

    print("Conteo de medicamentos: ", contador_medicamentos)
    print("Total de medicamentos:",  contador_texto_normal)

    # P5. Muestre ejemplos de espacios o mayúsculas en hospital,
    # diagnostico y medicamento.
    for atencion in atenciones:
        hospital = atencion.get("hospital", "")
        diagnostico = atencion.get("diagnostico", "")
        medicamento = atencion.get("medicamento", "")
        if hospital != hospital.strip() or hospital != hospital.lower():
            print("Ejemplo hospital:", hospital)
            break
        if diagnostico != diagnostico.strip() or diagnostico != diagnostico.lower():
            print("Ejemplo diagnostico:", diagnostico)
            break
        if medicamento != medicamento.strip() or medicamento != medicamento.lower():
            print("Ejemplo medicamento:", medicamento)
            break

    # P6. Cuente los medicamentos con strip() y lower(). Muestre el
    # contador limpio y su total. Compare con P4.
   
       


    # P7. Agrupe los nombres limpios con las equivalencias de la guía.
    # Complete el diccionario. La clave es la variante y el valor es
    # el nombre que conservará. El nuevo contador debe sumar 12.

    medicamentos_corregidos = {}
    contador_texto_limpio = 0
    
    EQUIVALENCIAS = {
        "acetaminofen": "acetaminofén",
        "paracetamol":  "acetaminofén",
        "panadol": "acetaminofén",
        "losartan" : "losartán",
        "nitrofurantoína" : "nitrofurantoína"
    }
    for atencion in atenciones:
        medicamento = atencion.get("medicamento", "")
        medicamento_arreglado = medicamento.strip().lower()
        medicamento_arreglado = EQUIVALENCIAS.get(medicamento_arreglado, medicamento_arreglado)
        medicamentos_corregidos[medicamento_arreglado] = medicamentos_corregidos.get(medicamento_arreglado, 0) + 1
        contador_texto_limpio += 1

    print("Conteo de medicamentos limpios:", medicamentos_corregidos)
    print("Total de medicamentos limpios:", contador_texto_limpio)
    print("Comparación P4 vs P6:", contador_texto_normal, "->",  contador_texto_limpio)
    

    # P8. Cuente hospitales y diagnósticos con los nombres limpios.
    # Muestre ambos contadores, sus totales y la categoría más frecuente de
    # cada campo.
    contador_hospitales = {}
    contador_diagnosticos = {}
    total_hospitales = 0
    total_diagnosticos = 0
    for atencion in atenciones:
        hospital = atencion.get("hospital", "").strip().lower()
        diagnostico = atencion.get("diagnostico", "").strip().lower()
        contador_hospitales[hospital] = contador_hospitales.get(hospital, 0) + 1
        contador_diagnosticos[diagnostico] = contador_diagnosticos.get(diagnostico, 0) + 1
        total_hospitales += 1
        total_diagnosticos += 1

    print("Hospitales con nombre limpio: ", contador_hospitales)
    print("El total de hospitales son: ",total_hospitales)
    print("Diagnosticos con nombre limpio",contador_diagnosticos)
    print("El total de diagnosticos son: ",total_diagnosticos)
    print("El hospital más visitado es: ", max(contador_hospitales))
    print("El diagnostico más frecuente es : ", max(contador_diagnosticos))


def concluir(atenciones):
    """Recibe la lista de atenciones y muestra el resumen de pacientes y esperas."""
    print("Etapa 3. Complete y compruebe las preguntas 9 y 10.")
    # P9. Cuente por cédula. Muestre cuántas personas hay, cuáles cédulas
    # se repiten y si coinciden el nombre, la edad y la provincia.
    contador_cedula = {}
    contador = 0 
    cedulas_repetidas = {}
    for atencion in atenciones:
        cedula = atencion.get("cedula", "")
        contador_cedula[cedula] = contador_cedula.get(cedula, 0) + 1
        contador += 1
        if contador_cedula.get(cedula) > 1:
            cedulas_repetidas[cedula] = cedulas_repetidas.get(cedula, 0) + 1   

  # P10. Sume minutos_espera con un ciclo. Muestre el total y el promedio.
    # Redacte un hallazgo que use el promedio y un conteo.     
    total = 0 
    for atencion in atenciones:
        minutos_espera = atencion.get("minutos_espera", "")
        total += minutos_espera


   
    print("Cedulas de pacientes: ",contador_cedula)
    print("Cantidad de pacientes por cedula: ",contador)
    print("Las cedulas repetidas son: ", cedulas_repetidas.keys())
    print("El total de minutos espera es: ",total)
    print("El promedio de minutos espera es:  ",total / len(atenciones))

    






atenciones = cargar_atenciones()
#print(atenciones)
if not atenciones:
    print("Revise los TODO de lector_csv.py antes de continuar.")
elif ETAPA == 1:
    explorar_atenciones(atenciones)
elif ETAPA == 2:
    contar_y_limpiar(atenciones)
elif ETAPA == 3:
    concluir(atenciones)
else:
    print("Seleccione 1, 2 o 3 en ETAPA.")

