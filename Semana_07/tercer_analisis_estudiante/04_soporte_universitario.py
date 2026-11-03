"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).
acumulador_minutos = 0
categoria = {
    "Acceso": 0,
    "Equipo" : 0,
    "Red" : 0,
}
provincias_pendientes = set()
casos_pendientes = 0
casos_urgentes = []
caso_maximo = ()

for incidencia in incidencias:
    acumulador_minutos += incidencia["minutos_atencion"]
    categoria[incidencia["categoria"]] += 1

    if incidencia["resuelto"] == False:
        casos_pendientes += 1
        provincias_pendientes.add(incidencia["provincia"])

        if incidencia["minutos_atencion"] >= 60:
            casos_urgentes.append((incidencia["id"],incidencia["minutos_atencion"]))

    if not caso_maximo or incidencia["minutos_atencion"] > caso_maximo[1]:
        caso_maximo = (incidencia["id"],incidencia["minutos_atencion"])

total_casos = len(incidencias)
promedio_minutos = acumulador_minutos / total_casos


print(f"Total de casos: {total_casos}")
print(f"Total de minutos: {acumulador_minutos}")
print(f"Promedio de minutos: {promedio_minutos}")
print(f"Conteo por categoría: {categoria}")
print(f"Cantidad de pendientes: {casos_pendientes}")
print(f"Provincias pendientes: {provincias_pendientes}")
print(f"Casos urgentes: {casos_urgentes}")
print(f"Caso más largo: {caso_maximo}")

pertenece_sanjose = "San Jose" in provincias_pendientes
print(f"¿Hay pendientes en San Jose?: {pertenece_sanjose}")


# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.
# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.