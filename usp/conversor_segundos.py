segundos_texto=input("Quantos segundo deseja converter?")
segundos=int(segundos_texto)

horas=segundos//3600
segundos_restantes_hora=segundos%3600
minutos=segundos_restantes_hora//60
segundos_restantes_minutos=segundos_restantes_hora%60

print("Esse total de segundos equivale a", horas,"horas,", minutos, "minutos e", segundos_restantes_minutos, "segundos.")