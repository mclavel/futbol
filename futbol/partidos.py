import random

jugadas = [] 
jugadas_interes_tipo_positivas = ["remate", "gol"]
jugadas_interes_tipo_negativas = ["falta", "amonestacion", "expulsion"]
jugadas_interes_peso_positivas = [70,30]
jugadas_interes_peso_negativas = [80,15,5]
jugadas_interes_min_positivas = 5
jugadas_interes_max_positivas = 15
jugadas_interes_min_negativas = 10
jugadas_interes_max_negativas = 20

bonificacion_local = 1.2

def tiempo_adicional():
    tiempo = int(random.triangular(0,10,4))
    #multiplicado por los 2 tiempos
    return tiempo*2

# Se solicita como parametros de ingreso:
# local: obligatorio - diccionario: { "nombre": string, "peso": float }
# visita: obligatorio - diccionario: { "nombre": string, "peso": float }
# Retorna una lista de eventos del partido
#[{"minuto": int, "tipo": string, "equipo": string}]
def partido(local, visita, relato = False):
    goles = [0, 0]
    remates = [0, 0]
    faltas = [0, 0]
    amonestaciones = [0, 0]
    expulsiones = [0, 0]
    eventos_positivos = eventos_partido(jugadas_interes_tipo_positivas,
                                        jugadas_interes_min_positivas,
                                        jugadas_interes_max_positivas,
                                        jugadas_interes_peso_positivas,
                                        90+tiempo_adicional(),
                                        local,
                                        visita)
    for jugada in eventos_positivos:
        if jugada["tipo"] == "remate":
            if jugada["equipo"] == local["nombre"]:
                remates[0] = remates[0]+1
            else:
                remates[1] = remates[1]+1
        elif jugada["tipo"] == "gol":
            if jugada["equipo"] == local["nombre"]:
                goles[0] = goles[0]+1
            else:
                goles[1] = goles[1]+1
        elif jugada["tipo"] == "falta":
            if jugada["equipo"] == local["nombre"]:
                faltas[0] = faltas[0]+1
            else:
                faltas[1] = faltas[1]+1 
        elif jugada["tipo"] == "amonestacion":
            if jugada["equipo"] == local["nombre"]:
                amonestaciones[0] = amonestaciones[0]+1
            else:
                amonestaciones[1] = amonestaciones[1]+1 
        elif jugada["tipo"] == "expulsion":
            if jugada["equipo"] == local["nombre"]:
                expulsiones[0] = expulsiones[0]+1
            else:
                expulsiones[1] = expulsiones[1]+1 
        else:
            pass

        if relato:
            print("[{0}] equipo {1}: {2}".format(jugada["minuto"], jugada["equipo"], jugada["tipo"]))
    temp = []
    for x in range(0,2):
        temp.append({"goles": goles[x], "remates": remates[x], "faltas": faltas[x], "amonestaciones": amonestaciones[x], "expulsiones": expulsiones[x]})
    return temp[0], temp[1]

def eventos_partido(listado_jugadas, jugadas_min, jugadas_max, distribucion_jugadas, tiempo_partido, local, visita):
    eventos = []
    tiempo_jugadas = []
    num_jugadas = random.randint(jugadas_min, jugadas_max)
    # Saco una lista con todas las jugadas de interes
    lista_jugadas = random.choices(listado_jugadas, weights=distribucion_jugadas, k=num_jugadas)
    for x in lista_jugadas:
        tiempo_jugadas.append(random.randint(0, tiempo_partido+1))
    tiempo_jugadas.sort()
    responsable_jugada = random.choices([local["nombre"], visita["nombre"]], weights=[local["peso"], visita["peso"]], k=num_jugadas)
    for i in range(0, num_jugadas):
        eventos.append({ "minuto": tiempo_jugadas[i], "tipo": lista_jugadas[i], "equipo": responsable_jugada[i] })
    return eventos