"""Microreto independiente: crear una función que limpie un nombre."""

#TODO : Aquí puede agregar un diccionario de equivalencias de nombres de medicamentos, por ejemplo: "ibuprofeno" y "paracetamol".
EQUIVALENCIAS = {
    "ACETAMINOFEN": "ACETAMINOFÉN",
    "PARACETAMOL":  "ACETAMINOFÉN",
    "PANADOL": "ACETAMINOFÉN",
    "MOTRIN": "IBUPROFENO",
    "SALIR": 'N'
}
def limpiar_nombre(nombre):
    """Devuelve nombre sin espacios en los extremos y en mayúsculas."""
    # TODO: complete el retorno del string limpio.
    nombre = nombre.strip().upper()
    #TODO: Agregue equivalente de nombres del diccionario de me dicamentos, por ejemplo: "ibuprofeno" y "paracetamol".
    nombre = EQUIVALENCIAS.get(nombre, nombre)
    return nombre


#print(limpiar_nombre("  acetaminofén "))
#TODO: Pruebe la función con varios nombres de medicamentos como "ibuprofeno", "paracetamol", "amoxicilina", etc. y verifique que los resultados sean correctos.
medicamentos = []
while True:
    medicamento = input("Ingrese el nombre del medicamento o 'n'para salir: ")
    medicamento = limpiar_nombre(medicamento)
    if medicamento == 'N':
        break

    medicamentos.append(medicamento)

print(medicamentos)