def study_schedule(permanence_period, target_time):

    contador = 0
    try:
        for tupla in permanence_period:
            if tupla[0] <= target_time <= tupla[1]:
                contador += 1
    except TypeError:
        return None
    return contador
