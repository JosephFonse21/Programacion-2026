"""Semana 8: la red hospitalaria nos contrata como analistas de datos.

Construimos el informe debajo de este inicio con GUIA_ESTUDIANTE.md.
Leemos la fuente preparada en fuente.py y contamos las menciones recibidas.
"""

from fuente import cargar_datos


USAR_RESPALDO = False  # Lo cambiamos solo si recibimos copias actualizadas.
registros, equivalencias, origen = cargar_datos(USAR_RESPALDO)
print("Fuente:", origen)
print("Registros recibidos:", len(registros))
print("Equivalencias publicadas:", len(equivalencias))

conteo_medicamento = {}
conteo_recetas = 0

# Comencemos aquí con la muestra y después construyamos nuestro contador.

print("\nMUESTRA DE DATOS\n")
for indice in range(3):
    registro = registros[indice]
    print('Codigo: ',registro["codigo"])
    print('Cedula: ',registro["paciente_cedula"])
    print('Nombre del paciente: ',registro["paciente_nombre"])
    print('Diagnostico: ',registro["diagnostico"])
    print('Medicamentos: ',registro["medicamentos"])
    print('-'*50,'\n')

#CONTEO
#FASE 1 : CONTAR MEDICAMENTOS
conteo_medicamento = {}
conteo_recetas = 0
#FASE 2 : Limpieza de datos
equivalencias = {
    "acetaminofén": "acetaminofen",
    "paracetamol": "acetaminofen",
    "antiácido": "antiacido",
    "losartán": "losartan"
}

for registro in registros:
    for medicamento in registro['medicamentos']:
        nombre = medicamento.strip().lower()
        #Aplicacion fase 2
        if nombre in equivalencias:
            nombre = equivalencias[nombre]

        if nombre in conteo_medicamento:
            conteo_medicamento[nombre] += 1
        else:
            conteo_medicamento[nombre] = 1
        conteo_recetas += 1

print("\n ----------CONTEO DE MEDICAMENTOS--------")
print("Total de recetas:", conteo_recetas)
for medicamento, cantidad in conteo_medicamento.items():
    print(f"- {medicamento}: {cantidad}")


#Pacientes que atendio cada sede
conteo_pacientes_hospital = {}

for registro in registros:
    hospital = registro['hospital']
    if hospital not in conteo_pacientes_hospital:
        conteo_pacientes_hospital[hospital] = 0
    conteo_pacientes_hospital[hospital] += 1

print("\nATENCIONES POR HOSPITAL")
for hospital, cantidad in conteo_pacientes_hospital.items():
    print(f"- {hospital}: {cantidad}")
    
