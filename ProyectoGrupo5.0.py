#Estructuras sacadas de investicación
             #Estas estructuras son utilizadas con el fin de hacer más estético el programa. Se obtuvo la información de estas estructuras en la biblioteca de python y de libros.
#zip crea un objeto iterable juntando otros objetos iterables de una o varias listas, en este caso lo usamos para comprimir todas las listas.
#Tambien cuando se imprime nos permite imprmirlo de la siguiente manera:
#Elemento 0 de listaP con Elemento 0 de listaPre con elemento 0 de status sin problemas.
#Variables
from datetime import datetime
fechaactual=datetime.now().strftime('%d/%m/%Y %H:%M:%S')
listaP=[]
listaPre=[]
status=[]


def Mostrar():
    tareasp=[i+1 for i,s in enumerate(status) if s=="Pendiente"]
    if tareasp:
        for i,(t,p,s) in enumerate(zip(listaP, listaPre, status)):
            if status[i]=="Pendiente":
             print(f"{fechaactual},{i+1}.{t}-{p}")
    else:
        print("Ya no hay tareas pendientes")
#Acá se le pide que si no hay tareas pendientes muestre el mensaje. De caso contrario que siga poniendo las tareas ingresadas en esa lista, el i es el indice y el s es el status.      

def completa():
    Mostrar()
    try:
        tarcom= int(input("Ingrese el número de la tarea completada:"))-1
        if status[tarcom]=="Completada":
            print("La tarea ya se marcó como completada")
        elif 0<=tarcom<len(listaP):
            status[tarcom]="Completada"
            print("Tarea completada con existo!")

        else:
            print("El número de tarea no existe")
    
    except ValueError:
        print("Ingrese un número válido")
def Mos():
    for i,(t,p) in enumerate(zip(listaP,listaPre)):
        if status[i]=="Completada":
            print(f"{fechaactual},{i+1}.{t}-{p}")
            
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
            status.append("Pendiente")
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
                           completa()
                      elif op== 'n':
                           break
                      else:
                           print("Inválido")
                      op=input("Desea completar una tarea?(s/n):").lower()
                           
        elif menu=='3':
            if "Completada" in status:
                print("----TAREAS COMPLETADAS----")
                Mos()
                print("-------------------------")
            else:
                print("No hay tareas completadas aún")
    
        elif menu == '4' or menu=='5':
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

   
          

    


            

   

     

        


        
    

