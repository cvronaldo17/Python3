#PROGRAMA7
#CristianRonaldoVillavazoGonzalez
edad=0
adultos=0
for con in range (1,21):
    edad=int(input("Introduzca su edad"))
    if edad>=18:
        adultos=adultos+1
print("Asistieron",adultos,"adultos")