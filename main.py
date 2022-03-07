#EJEMPLO 1

'''

nivelAgua=float(input("Digita el Nivel del Agua: "))

if(nivelAgua>0 and  nivelAgua<200):
    print("la represa tiene POCA agua ")

elif(nivelAgua>=200 and nivelAgua<450):
    print("la respresa esta ESTABLE")

elif(nivelAgua>=450):
    print("!CUIDADO , abra compuertas")

else:
    print("Digito un nivel invalido")

'''
#EJEMPLO 2 
'''
mesUsuario=input("Digite el Mes en el que esta para saber su ESTACION : ")


if(mesUsuario=="enero" or mesUsuario=="febrero"or  mesUsuario=="marzo"):
    print("Estas en INVIERNO")

elif(mesUsuario=="abril" or mesUsuario=="mayo"or  mesUsuario=="junio"):
    print("Estas en VERANO")

elif(mesUsuario=="julio" or mesUsuario=="agosto"or  mesUsuario=="septiembre"):
    print("Estas en OTOÑO")

elif(mesUsuario=="octubre" or mesUsuario=="noviembre"or  mesUsuario=="diciembre"):
    print("Estas en PRIMAVERA")

else:
    print("NO DIGITASTE UN MES VALIDO!!")
    '''

 #EJEMPLO 3
'''
edad=float(input("Digite su edad : "))
if(edad>0 and edad<15):
    print("usted es un nño")

elif(edad >=15 and edad < 28 ):
       print("usted es un Joven")

elif(edad >=28 and edad < 60 ):
       print("usted es un adulto")

elif(edad>=60):
     print("usted es un ANCIANO")

else:
    print("Error")
'''
#EJEMPLO 4 

#Operador Ternario
parametro=True
print("El parametro es verdadero ")if parametro==True else  print("el parametro es falso")

estaLLoviendo=False

if(estaLLoviendo==False):
    print("es verdadero")
else:
    print("es falso")

print("es verdadero")if estaLLoviendo==False else print("es Falso")
