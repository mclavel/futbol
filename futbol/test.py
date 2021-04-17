# se asume que el campeonato tiene numero par de equipos

from partidos import *

equipo1 = {"nombre": "Universidad de Chile", "peso": 1.59, "puntos": 0}
equipo2 = {"nombre": "Colo Colo", "peso": 1.82, "puntos": 0}
equipo3 = {"nombre": "Católica", "peso": 2.40, "puntos": 0}
equipo4 = {"nombre": "Unión Española", "peso": 1.95, "puntos": 0}
equipo5 = {"nombre": "Huachipato", "peso": 1.21, "puntos": 0}
equipo6 = {"nombre": "Palestino", "peso": 1.62, "puntos": 0}

lista_equipos = [equipo1, equipo2, equipo3, equipo4, equipo5, equipo6]
random.shuffle(lista_equipos)

# Revisa si el número es par
def es_par(numero):
    if numero%2 == 0:
        return True
    return False

# Revisa si la información corresponde a un equipo correcto
# retorna True si está bien
# retorna False si está mal
# requiere un equipo
def es_equipo_valido(equipo):
    if not type(equipo) == dict:
        return False
    if not "nombre" in equipo:
        return False
    if not "puntos" in equipo:
        return False
    if not "peso" in equipo:
        return False
    # peso sea un float
    # nombre sea un string
    # puntos sea un int
    return True

# Revisa que la lista entregada sean equipos
# correcttamente diseñados, superior a 0
# retorna true si todos los equipos están OK
# retorna false si alguno falla
def es_lista_equipos_valido(lista_equipos):
    if not type(lista_equipos) == list:
        return False
    if len(lista_equipos) == 0:
        return False
    for equipo in lista_equipos:
        if not es_equipo_valido(equipo):
            return False
    return True

# revisa si la lista de equipos es valida para crear un fixture
# deben ser al menos 2 equipos
# lista de equipos
def es_lista_valida_para_fixture(lista_equipos):
    if len(lista_equipos) < 2:
        return False
    # En caso de cambiar restriccion equipos pares, sacar está condicion
    if not es_par(len(lista_equipos)):
        return False
    if not es_lista_equipos_valido(lista_equipos):
        return False
    return True
   
def calcula_resultado(nombre1, goles1, nombre2, goles2, puntos1, puntos2):
    if goles1 > goles2:
        #print("Gana "+nombre1+ " "+str(goles1))
        #print("Pierde "+nombre2+ " "+str(goles2))
        #print(nombre1+" suma 3 puntos")
        puntos1 = puntos1 + 3

    elif goles2 == goles1: #Empate 3 - 3
        #print("Empate "+str(goles2)+" - "+str(goles1))
        #print("ambos equipos suman 1 punto")
        puntos1 = puntos1 + 1
        puntos2 = puntos2 + 1
    else:
        #print("Gana "+nombre2+ " "+str(goles2))
        #print("Pierde "+nombre1+ " "+str(goles1))
        #print(nombre2+" suma 3 puntos")
        puntos2 = puntos2 + 3
    return puntos1, puntos2

# TODO
# Falta implementar el fixture utilizando una lista con N
# equipos, independiente de los que existan.
# Restricciones:
# - lista_equipos tiene que ser mayor o igual a 2 equipos
# - lista_equipos tiene que tener una lista con equipos
def crear_fixture(lista_equipos):
    fixture = [[[equipo1, equipo2], [equipo3, equipo4]],
                [[equipo2, equipo3], [equipo4, equipo1]],
                [[equipo1, equipo4], [equipo3, equipo2]],
                [[equipo2, equipo1], [equipo4, equipo3]],
                [[equipo1, equipo3], [equipo2, equipo4]],
                [[equipo3, equipo1], [equipo4, equipo2]]]
    return fixture

def puntaje(equipo):
    return equipo["puntos"]

def tabla(lista_equipos):
    print("+++++ TABLA +++++")
    #tabla = [puntaje(equipo1),puntaje(equipo2), puntaje(equipo3),puntaje(equipo4)]
    lista_ordenada = sorted(lista_equipos, key=lambda var_super_temporal_lambda: var_super_temporal_lambda['puntos'], reverse=True)  
    #tabla.sort() #sort retorna la lista ordenada, sorted trae una nueva lista 
    for equipo in lista_ordenada:
        print("["+str(equipo['puntos'])+"] "+equipo['nombre'])

    return lista_ordenada

    # print("equipo1 -> "+str(puntaje(equipo1)))
    # print("equipo2 -> "+str(puntaje(equipo2)))
    # print("equipo3 -> "+str(puntaje(equipo3)))
    # print("equipo4 -> "+str(puntaje(equipo4))) 

# Codigo sacado de internet
# https://gist.github.com/ih84ds/be485a92f334c293ce4f1c84bfba54c9
def crear_fixture_balanceado(lista_equipos):
    """ Create a schedule for the players in the list and return it"""
    fechas_fixture = []
    if len(lista_equipos) % 2 == 1: 
        lista_equipos = lista_equipos + [None]
    # manipulate map (array of indexes for list) instead of list itself
    # this takes advantage of even/odd indexes to determine home vs. away
    largo_lista_equipos = len(lista_equipos)
    identificador_equipo = list(range(largo_lista_equipos))
    numero_partidos_fecha = largo_lista_equipos // 2
    for i in range(largo_lista_equipos-1):
        l1 = identificador_equipo[:numero_partidos_fecha]
        l2 = identificador_equipo[numero_partidos_fecha:]
        l2.reverse()
        fecha = []
        for j in range(numero_partidos_fecha):
            t1 = lista_equipos[l1[j]]
            t2 = lista_equipos[l2[j]]
            if j == 0 and i % 2 == 1:
                # flip the first match only, every other round
                # (this is because the first match always involves the last player in the list)
                fecha.append((t2, t1))
            else:
                fecha.append((t1, t2))
        fechas_fixture.append(fecha)
        # rotate list by n/2, leaving last element at the end
        identificador_equipo = identificador_equipo[numero_partidos_fecha:-1] + identificador_equipo[:numero_partidos_fecha] + identificador_equipo[-1:]
    return fechas_fixture

def mostrar_fixture(fixture):
    for fecha in fixture:
        print("Nueva Fecha")
        for partido in fecha:
            print("  --> Local: "+partido[0]["nombre"])
            print("  --> Visita: "+partido[1]["nombre"])
#fixture = crear_fixture(lista_equipos)
fixture = crear_fixture_balanceado(lista_equipos)
mostrar_fixture(fixture)
for fecha in fixture:
    print("======== NUEVA FECHA =======")
    for encuentro in fecha:
        print("=== NUEVO PARTIDO ===")
        local = encuentro[0]
        visita = encuentro[1]
        print(local["nombre"]+ " v/s "+visita["nombre"])
        res_local, res_visita = partido(local, visita, False)
        puntos_local, puntos_visita = calcula_resultado(local["nombre"], res_local["goles"], visita["nombre"], res_visita["goles"], local["puntos"], visita["puntos"])
        local["puntos"] = puntos_local
        visita["puntos"] = puntos_visita
    tabla(lista_equipos)


### Repasar lo hecho.
### Agregar comentarios
### -> importar módulos para visualizar & mostrar información
### -> modificar lógica librería
### -> utilizar clases (python class)
### -> estructurar ordenadamente