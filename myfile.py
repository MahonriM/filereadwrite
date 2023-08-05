def escribir():
    f=open('mitexto.txt','a+')
    c=int(input("Ingresa  la cantidad de lineas que deseas agregar"))
    for i in range(0,c):
        nombre=input("Ingresa el texto que deseas ingresar en esta linea")
        f.write('\n'+nombre)
    f.close()
    print("MEnsaje escrito")
def leer():
    f=open('mitexto.txt','r')
    for i in f:
        print(i)
    f.close()
print("1-Leer el texto")
print("2-Escribir")
op=int(input("¿Que opcion deseas realizar con el archivo de texto?"))
if op==1:
    leer()
elif op==2:
    escribir()
else:
    print("Intenta de nuevo")
    
