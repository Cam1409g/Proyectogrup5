#Estructuras sacadas de investicación
             #Estas estructuras son utilizadas con el fin de hacer más estético el programa. Se obtuvo la información de estas estructuras en la biblioteca de python y de libros.  
#Variables
from datetime import datetime
listaP=[]
listaPre=[]

def Mostrar():
    k=0
    while k <len(listaP) and k <len(listaPre):
       fechaact= datetime.now() #Para ver la fecha y hora de ingreso de la tarea.
       print(fechaact,"    ",k+1,".",listaP[k],"   ",listaPre[k])
       k+=1    
#-----MENU-------
def menu():  #Defino el menú primero para que no haya errores de definiciones al elegir si se desea entrar.
    #Se decidió cambiar el menu para evitar errores de validación.
    while True:
        print("--------Menú Principal--------")
        print("1-Agregar tarea")
        print("2-Ver tareas pendientes")
        print("3-Ver tareas completadas")
        print("4-Ver el coste total")
        print("5-Eliminar tarea")
        print("6-Salir")
        menu= input("Ingrese una opción:")
        if menu =='1':
            print("-----AGREGUE UNA TAREA------")
            t=input("Nombre de la tarea:")
            while True:
                try: #Esto es para evitar que el usuario ingrese un srt en vez del precio.
                    p=float(input("Valor aproximado de la tarea:"))
                    break
                except ValueError:
                    continue      
            listaP.append(t)
            listaPre.append(p)
            print("Tarea agregada con éxito")   
        elif menu == '2':
            if 0==len(listaP) and 0== len(listaPre):
                print("Ooops, no existen tareas,crea algunas con la opción 1 del menú")
            else:
                print("TAREAS PENDIENTES")
                print("---------------------------")
                Mostrar()
                print("---------------------------")
                op=input("Desea completar una tarea?(s/n):").lower()
                while op!='s' or op!='n':
                      if op=='s':
                           print("Opción inhabilitada")
                      elif op== 'n':
                           break
                      else:
                           print("Inválido")
                      op=input("Desea completar una tarea?(s/n):").lower()
                           
        elif menu=='3'or menu == '4' or menu=='5':
              print("Opción aún no habilitada")
        elif menu == '6':
              print("Hasta luego")
              print("------------------------")
              break
        else:
             print("Opción no válida :)")
            
def respuesta(): #Defino la respuesta.
    respuesta= input("Ingrese una opción(S,N):").lower() #Lower para poder ingresarlo en mayúscula o minúscula
    while respuesta!='s' or respuesta!='n': #Ciclo while para que lo repita en caso de no ingresar la opción correcta.
        if respuesta=='s':
            print("----BIENVENIDO----")
            menu()
            while True: #Esta opción se pone aquí para evitar que respuesta() se siga ejecutando despues de ingresar 6.
                if menu==6:
                    break
        elif respuesta=='n':
            print("Hasta pronto")
            print("-----------------------")
            bienvenida()
        else:
            print("Inválido")
        respuesta= input("Ingrese una opción(S,N):").lower()
def bienvenida():
    print("Bienvenido a la mejor app de organización de tareas, acá te permitimos gestionar tus tareas y gastos de manera sencilla :)")
    usuario = input("Ingrese su nombre:")
    print(f"Bienvenid@ {usuario}! ¿Desea ingresar al menú?")
    respuesta()

   
bienvenida() #La respuesta se define antes de bienvenida para que no hayan errores de definiciones y la bienvenida queda como un main afuera de todo.

   
          

    


            

   

     

        


        
    

