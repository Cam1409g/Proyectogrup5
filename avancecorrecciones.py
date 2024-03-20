# -----Dar bienvenida------
def bienvenida():
    print("Bienvenido a la mejor app de organización de tareas, acá te permitimos gestionar tus tareas y gastos de manera sencilla :)")
    usuario = input("Ingrese su nombre de usuario:")
    print(f"Bienvenid@ {usuario}! ¿Desea ingresar al menú?")

bienvenida() #Esta definido así para poder ponerlo de nuevo en caso de que el usuario elija que no quiere ingresar al menú, si cambia de opinión no tiene que ejecutarlo de nuevo.
             #De igual manera al seleccionar salir solo se sale del menú, no de la app, para ello hay que precionar la x.

#-----Ingresar opción-------

def menu():  #Defino el menú primero para que no haya errores de definiciones al elegir si se desea entrar.
    menu = int(input("Menú Principal:\n1-Agregar tarea\n2-Ver tareas pendientes\n3-Ver tareas completadas\n4-Ver el coste total\n5-Eliminar tarea\n6-Salir \n"))
    while menu!= 7:
        if menu ==1 or menu == 2 or menu == 3 or menu == 4 or menu==5:
              print("Opción aún no habilitada")
        elif menu == 6:
              print("Hasta luego")
              print("------------------------")
              bienvenida()
              break
        else:
             print("Opción no válida :)")
        
        menu = int(input("Menú Principal:\n1-Agregar tarea\n2-Ver tareas pendientes\n3-Ver tareas completadas\n4-Ver el coste total\n5-Eliminar tarea\n6-Salir \n"))
        
    else:
         print("Opción inválida")
         
def respuesta(): #Defino la respuesta.
    respuesta= input("Ingrese una opción(S,N):").lower() #Lower para poder ingresarlo en mayúscula o minúscula
    while respuesta!='s' or respuesta!='n': #Ciclo while para que lo repita en caso de no ingresar la opción correcta.
        if respuesta=='s':
            print("----BIENVENIDO----")
            menu()
        elif respuesta=='n':
            print("Hasta pronto")
            print("-----------------------")
            bienvenida()
        else:
            print("Inválido")
        respuesta= input("Ingrese una opción(S,N):").lower()

            

respuesta()

    
         

    


            

   

     

        


        
    

