#PROGRAMA5
#CristianRonaldoVillavazoGonzalez
pos=0
neg=0
num=0
for con in range (1,21):
    num=int(input("Introduzca su numero"))
    if num>0:
        pos=pos+1
    else:
        neg=neg+1
print("Positivos: ",pos)
print("Negativos: ",neg)
print("FIN DEL PROGRAMA")