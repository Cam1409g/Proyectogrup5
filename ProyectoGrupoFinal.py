#Estructuras sacadas de investigación
             #Estas estructuras son utilizadas con el fin de hacer más estético el programa. Se obtuvo la información de estas estructuras en la biblioteca de python y de libros.
#zip crea un objeto iterable juntando otros objetos iterables de una o varias listas, en este caso lo usamos para comprimir todas las listas.
#Tambien cuando se imprime nos permite imprmirlo de la siguiente manera:
#Elemento 0 de listaP con Elemento 0 de listaPre con elemento 0 de status sin problemas.

#Listas
listaP= []
listaD= []
listaPre=[]
status= []
fechas= []


def guardarT():
    with open('TareasP.txt', 'w') as archivo:
        for f, t, d, p, s in zip(fechas, listaP,listaD,listaPre, status):
            if s == "Pendiente":
                archivo.write(f"{f},{t},{d},{p}\n")
                
    with open('TareasC.txt', 'w') as archivo:
        for f, t, d, p, s in zip(fechas, listaP,listaD,listaPre, status):
            if s == "Completada":
                archivo.write(f"{f},{t},{d},{p}\n")

#Función para leer los datos almacenados
def Pushup():
    try:
        with open('TareasP.txt', 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split(',', 3)
                if len(partes) == 4:
                    f, t, d, p = partes
                    listaP.append(t.strip())
                    listaD.append(d.strip())
                    listaPre.append(float(p.strip().split(':')[-1]))  # Tomar el último elemento después de dividir por ':'
                    fechas.append(f.strip())
                    status.append("Pendiente")

        with open('TareasC.txt', 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split(',', 3)
                if len(partes) == 4:
                    f, t, d, p = partes
                    listaP.append(t.strip())
                    listaD.append(d.strip())
                    listaPre.append(float(p.strip().split(':')[-1]))
                    fechas.append(f.strip())
                    status.append("Completada")
                    
    except FileNotFoundError:
        print("No se encontraron archivos de tareas guardadas, guarde algunas.")


def pendiente():
    pendientes = [i+1 for i, s in enumerate(status) if s == "Pendiente"]
    if pendientes:
        print("---------------------------")
        for i, (f, t, d, p, s) in enumerate(zip(fechas, listaP, listaD, listaPre, status), start=1):
            if s == "Pendiente":
                print(f"{i}. Fecha: {f}, Tarea: {t}, Descripción: {d}, Precio: {p}")
        print("---------------------------")
    else:
        print("No hay tareas pendientes")
        
#Acá se le pide que si no hay tareas pendientes muestre el mensaje. De caso contrario que siga poniendo las tareas ingresadas en esa lista, el i es el indice y el s es el status.      

def completa():
    pendiente()
    try:
        tarcom= int(input("Ingrese el número de la tarea completada:"))-1
        if status[tarcom]=="Completada":
            print("La tarea ya se marcó como completada")
        elif 0<=tarcom<len(listaP):
            status[tarcom]="Completada"
            print("Tarea completada con existo!")
            guardarT() #Guarda las tareas despues de marcar como completada
        else:
            print("El número de tarea no existe")
    except (ValueError,IndexError):
        print("Ingrese un número válido")
        
#Función para marcar de nuevo una tarea pendiente
def wrong():
     Mos()
     try:
        tar= int(input("Ingrese el número de la tarea que debe seguir pendiente:"))-1
        if status[tar]=="Pendiente":
            print("La tarea ya se marcó como completada")
        elif 0<=tar<len(listaP):
            status[tar]="Pendiente"
            print("Tarea se marcó como pendiente nuevamente!")
            guardarT() #Guarda las tareas despues de marcar como completada
        else:
            print("El número de tarea no existe")
     except (ValueError,IndexError):
        print("Ingrese un número válido")
        
      
def Mos():
    completadas = False
    for i, (t, d, p, f, s) in enumerate(zip(listaP, listaD, listaPre, fechas, status), start=1):
        if s == "Completada":
            if not completadas:
                completadas = True
            print("----TAREAS COMPLETADAS----")
            print("--------------------------")
            print(f"{i}. Fecha: {f}, Tarea: {t}, Descripción: {d}, Precio: {p}")
    if not completadas:
        print("No hay tareas completadas aún")
        
#Funciones para los totales de tareas       
def total_final():
    if not listaPre:
        print("No hay ningún valor a considerar.")
    else:
        total = sum(listaPre)
        print(f"El costo total de todas las tareas es: {total}")
        costeP()
        costeC()

def costeP():
    costep = sum(listaPre[i] for i, s in enumerate(status) if s == "Pendiente")
    print(f"El costo total de las tareas pendientes es: {costep}")

def costeC():
    costec = sum(listaPre[i] for i, s in enumerate(status) if s == "Completada")
    print(f"El costo total de las tareas completadas es: {costec}")

#Función para validar las fechas ingresadas       
def validar(fecha):
    partesf = fecha.split('/') 
    if len(partesf) == 3:
        for parte in partesf:
            if not parte.isdigit(): #Para asegurarse que lo que ingrese el usuario es un valor númerico
                return False
        day = int(partesf[0])
        m = int(partesf[1])
        a = int(partesf[2])
        # Verificar si el día, mes y año están en los rangos adecuados
        if 1 <= day <= 31 and 1 <= m <= 12 and a >= 2024:
            return True
    
    return False

#Función para eliminar una tarea
def eliminar_tarea_pendiente():
    while True:  # Agregar un bucle para permitir múltiples intentos
        pendientes =[i for i, s in enumerate(status) if s == "Pendiente"]
        if not pendientes: # Comprobar si no hay tareas pendientes
            print("No hay tareas pendientes para eliminar.")
            return
        else:
            print("TAREAS PENDIENTES")
            print("---------------------------")
            pendiente()
            print("---------------------------")
            try:
                num_tarea = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
                if num_tarea in pendientes:  # Verificar si la tarea seleccionada está pendiente
                    tarea_eliminada = listaP.pop(num_tarea)
                    listaD.pop(num_tarea)
                    listaPre.pop(num_tarea)
                    fechas.pop(num_tarea)
                    status.pop(num_tarea)
                    print(f"Tarea '{tarea_eliminada}' eliminada con éxito.")
                    guardarT()  # Guarda las tareas después de eliminar una
                    break  # Salir del bucle si la tarea se elimina correctamente
                else:
                    print("El número de tarea no es válido o la tarea ya está completada.")
            except ValueError:
                print("Ingrese un número válido.")
#Ordenada
def obtener_fecha(tarea):
    return tarea[0]

def listaordenada():
    tareas = [] #Para agregar las dos listas en una 
    with open('TareasP.txt', 'r') as archivo:
        for linea in archivo:
            f, t, d, p = linea.strip().split(',')
            tareas.append((f, t, d, p, 'Pendiente'))

    with open('TareasC.txt', 'r') as archivo:
        for linea in archivo:
            f, t, d, p = linea.strip().split(',')
            tareas.append((f, t, d, p, 'Completada'))
    tareas_ordenadas = sorted(tareas, key=obtener_fecha)
    if not tareas_ordenadas:
        print("No hay tareas registradas.")
    else:
        print("Lista de tareas ordenadas por fecha:")
        for i, tarea in enumerate(tareas_ordenadas, start=1):
            print(f"{i}. Fecha: {tarea[0]}, Tarea: {tarea[1]}, Descripción: {tarea[2]}, Precio: {tarea[3]}, Estado: {tarea[4]}")


#La estadisticas
def cantidadTotal():
    total= len(listaP)
    print(f"Hay un total de {total} tareas registradas hasta la fecha")
    cantidadTPendiente()
    cantidadTCompletada()
    listaordenada()
    
def cantidadTPendiente():
    with open('TareasP.txt', 'r') as archivo:
        contenido = archivo.readlines()
        cantidad_pendientes = len(contenido)
        print(f"Hay {cantidad_pendientes} tareas pendientes registradas.")
def cantidadTCompletada():
    with open('TareasC.txt', 'r') as archivo:
        contenido = archivo.readlines()
        cantidad_completadas = len(contenido)
        print(f"Hay {cantidad_completadas} tareas completadas registradas.")


#Función para editar tareas
def editar():
    while True:
        pendientes =[i for i, s in enumerate(status) if s == "Pendiente"]
        if not pendientes:
            print("No hay tareas pendientes para eliminar.")
            return
        else:
            print("------TAREAS PENDIENTES------")
            pendiente()
        try:
            num = int(input("Ingrese el número de la tarea que desea editar: ")) - 1
            if 0 <= num < len(listaP):
                tarea = input("Nombre de la tarea:")
                while not tarea.strip():
                    print("Ingrese un nombre de tarea válido")
                    tarea = input("Nombre de la tarea:")
                descripcion= input("Descripción de la tarea:")
                while not nueva_descripcion.strip():
                    print("Ingrese una descripción válida:")
                    descripcion= input("Descripción de la tarea:")
                fech = input("Ingrese la nueva fecha de la tarea (dd/mm/aaaa): ")
                while not validar(fech):
                    print("Formato de fecha incorrecto (dd/mm/aaaa) o se sale de la actualidad (2024).")
                    fecha = input("Ingrese la nueva fecha de la tarea (dd/mm/aaaa): ")
                while True:
                    precio = float(input("Ingrese el nuevo precio de la tarea: "))
                    try:
                         precio= float(precio)
                         break
                    except ValueError:
                          print("Por favor, ingrese un valor numérico.")
                          p = input("Valor aproximado de la tarea:") 
                listaP[num]= tarea
                listaD[num]= descripcion
                fechas[num]= fech
                listaPre[num]= precio
                print("Tarea editada exitosamente.")
                guardarT()
                break
            else:
                print("Número de tarea no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido para la tarea.")   
        

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
        print("6-Estadísticas")
        print("7-Editar tarea")
        print("8-Salir")
        menu = input("Ingrese una opción:")
        if menu == '1':
            print("-----AGREGUE UNA TAREA------")
            t = input("Nombre de la tarea:")
            while not t.strip(): #La función strip aparte de servir para eliminar los espacios en blanco también impide que el usuario deje en blanco el espacio.
                print("Ingrese un nombre de tarea válido")
                t = input("Nombre de la tarea:")
            d = input("Descripción de la tarea:")
            while not d.strip():
                print("Ingrese una descripción bichillo, no sea malo :)")
                d = input("Descripción de la tarea:")
            while True:
                f = input("Ingrese la fecha de la tarea (dd/mm/aaaa):")
                if validar(f):
                    break
                else:
                    print("Formato de fecha incorrecto(dd/mm/aaaa). O el año esta fuera de la actualidad(2024)")
            while True:
                p = input("Valor aproximado de la tarea:")
                try:
                    p = float(p)
                    break
               
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")
                    p = input("Valor aproximado de la tarea:")    
            listaP.append(t)
            listaD.append(d)
            listaPre.append(p)
            fechas.append(f)
            status.append("Pendiente")
            guardarT() #Guarda las tareas al agregar una
            print("Tarea agregada con éxito")
            
        elif menu == '2':
            if 0==len(listaP) and 0== len(listaPre):
                print("Ooops, no existen tareas,crea algunas con la opción 1 del menú")
            else:
                print("TAREAS PENDIENTES")
                pendiente()
                pendientes =[i for i, s in enumerate(status) if s == "Pendiente"]
                if pendientes:
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
                Mos()
                print("-------------------------")
                op=input("Se equivocó al marcar una tarea completada?(s/n):").lower()
                completadas= pendientes =[i for i, s in enumerate(status) if s == "Completadas"]
                if completadas:
                    while op!='s' or op!='n':
                      if op=='s':
                          wrong()
                      elif op== 'n':
                           break
                      else:
                           print("Inválido")
                      op=input("Desea completar una tarea?(s/n):").lower()
                else:
                    print("No hay tareas completadas")
            else:
                print("No hay tareas completadas aún")
                
    
        elif menu == '4':
            total_final()
            
        elif menu == '5':
            eliminar_tarea_pendiente()

        elif menu=='6':
            cantidadTotal()
            
        elif menu=='7':
            editar()
        elif menu == '8':
              print("Hasta luego")
              print("------------------------")
              guardarT()
              break
        else:
             print("Opción no válida :)")
            
def respuesta(): #Defino la respuesta.
    respuesta= input("Ingrese una opción(S/N):").lower() #Lower para poder ingresarlo en mayúscula o minúscula
    while respuesta!='s' or respuesta!='n': #Ciclo while para que lo repita en caso de no ingresar la opción correcta.
        if respuesta=='s':
            print("----BIENVENIDO----")
            Pushup()
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
    usuario = input("Ingrese su nombre: ")
    while not usuario.strip():  # Verificar si el usuario ha ingresado un nombre en blanco
        print("Por favor, ingrese su nombre por fa :(")
        usuario = input("Ingrese su nombre: ")

    print(f"Bienvenid@ {usuario}! ¿Desea ingresar al menú?")
    respuesta()
bienvenida() #La respuesta se define antes de bienvenida para que no hayan errores de definiciones y la bienvenida queda como un main afuera de todo.

   
          

    


            

   

     

        


        
    

