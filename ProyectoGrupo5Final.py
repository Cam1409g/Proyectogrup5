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
    with open('TareasP.txt', 'w') as archivo: #Esta función nos permite actualizar todo lo que hagamos y aparte crea el archivo
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
        with open('TareasP.txt', 'r') as archivo: #Se encarga de subir toda la información de los archivo cuando volvemos a ejecutar el programa
            for linea in archivo:
                partes = linea.strip().split(',')
                if len(partes) == 4: #Acá le definimos cuales partes se muestran en el archivo y cuales son importantes mostrar
                    f, t, d, p = partes
                    listaP.append(t.strip())
                    listaD.append(d.strip())
                    listaPre.append(float(p.strip())) #Le decimos que el precio va a ser un float para que cuando se ejecute de nuevo el programa no tenga problemas.
                    fechas.append(f.strip())
                    status.append("Pendiente")

        with open('TareasC.txt', 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split(',')
                if len(partes) == 4:
                    f, t, d, p = partes
                    listaP.append(t.strip())#Se agrega la información a cada una de las listas
                    listaD.append(d.strip())
                    listaPre.append(float(p.strip()))
                    fechas.append(f.strip())
                    status.append("Completada")
                    
    except FileNotFoundError:
        print("Seguramente es tu primer inicio, por ello, para empezar a guardar información necesitamos que ingreses tus tareas :)")
        print("Acá tenemos nuestra interfaz de menú, para agregar nuevas tareas, presiona la opción 1 ;D") #Esto sale cuando los archivos aún no se han creado


def pendiente(): #El +1 es para que inicie en 1
    pendientes = [i+1 for i, s in enumerate(status) if s == "Pendiente"] #Estamos creando una lista clasificando todas las tareas en los indices que esten en pendiente
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
        tarcom= int(input("Ingrese el número de la tarea completada:"))-1 #Es porque las listas siempre inician desde 0 sí el usuario ingresa 1, le va a restar 1 para que sea correcto
        if status[tarcom]=="Completada": #El parentesis cuadrado me va a evaluar las tareas en el indice que le dimos
            print("Mmmm como que ya habias marcado esa tarea como completada")
        elif 0<=tarcom<len(listaP): #Tiene que estar igualado a 0 para que el programa reciba correctamente el ejemplo de 1-1= '0' del indice de la tarea
            status[tarcom]="Completada"
            print("Tarea completada con existo!")
            guardarT() #Guarda las tareas despues de marcar como completada
        else:
            print("El número de tarea no existe")
    except Exception:
        print("Necesitamos un valor númerico o un número dentro del rango :)")

        
#Función para marcar de nuevo una tarea pendiente
def Mos():
    completadas = [i for i, s in enumerate(status) if s == "Completada"] #Acá es lo mismo que la parte de pendiente
    if completadas:  
        print("----TAREAS COMPLETADAS----")
        print("--------------------------")
        for i, (t, d, p, f, s) in enumerate(zip(listaP, listaD, listaPre, fechas, status), start=1):
            if s == "Completada":
                print(f"{i}. Fecha: {f}, Tarea: {t}, Descripción: {d}, Precio: {p}")
        print("-------------------------")
        return True
    else:
        print("No hay tareas completadas para poner aquí, que mal")
        return False

def wrong():
    completadas = [i for i, s in enumerate(status) if s == "Completada"]
    if completadas: 
        print("----TAREAS COMPLETADAS----")
        for i, (t, d, p, f, s) in enumerate(zip(listaP, listaD, listaPre, fechas, status), start=1):
            if s == "Completada":
                print(f"{i}. Fecha: {f}, Tarea: {t}, Descripción: {d}, Precio: {p}")
        print("-------------------------")
        try:
            tar = int(input("Ingrese el número de la tarea que debe seguir pendiente:")) - 1 #Funciona bien para devolver la tarea selecionada a pendiente
            if tar in completadas:  
                status[tar] = "Pendiente"  
                print("Tarea marcada como pendiente nuevamente. Ánimo")
                guardarT()  # Guardar cambios
            else:
                print("El número de tarea no es una tarea completada.")
        except Exception: #Esto es para que en caso de que se de un error de estos el programa no se caiga y le avise al usuario que salió mal
            print("Valor númerico por faaa")
    else:
        print("Hey, no hay tareas completadas para marcar como pendiente")

        
#Funciones para los totales de tareas       
def total_final():
    if not listaPre:
        print("No hay ningún valor a considerar")
    else:
        total = sum(listaPre)
        print(f"El costo total de todas las tareas es: {total}")
        costeP()
        costeC()
        print("¿Y por que tan caro?")

def costeP():
    costep = sum(listaPre[i] for i, s in enumerate(status) if s == "Pendiente")
    print(f"El costo total de las tareas pendientes es: {costep}")

def costeC():
    costec = sum(listaPre[i] for i, s in enumerate(status) if s == "Completada")
    print(f"El costo total de las tareas completadas es: {costec}")

#Función para validar las fechas ingresadas       
def validar(fecha):
    partesf = fecha.split('/')#Para que sea valido que se divida por este signo 
    if len(partesf) == 3:
        for parte in partesf:
            if not parte.isdigit(): #Para asegurarse que lo que ingrese el usuario es un valor númerico
                return False
        day = int(partesf[0])
        m = int(partesf[1])
        a = int(partesf[2])
        # Verificar si el día, mes y año están en los rangos adecuados
        if 1 <= day <= 31 and 1 <= m <= 12 and a >= 2000: #2000 solo por el hecho de que esta app también sirve para documentar las tareas
            return True
    
    return False

#Función para eliminar una tarea
def eliminar_tarea_pendiente():
    while True:  # Agregar un bucle para permitir múltiples intentos
        pendientes =[i for i, s in enumerate(status) if s == "Pendiente"]
        if not pendientes: # Comprobar si no hay tareas pendientes
            print("Ojo, no hay tareas pendientes para eliminar")
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
                    print("El número de tarea no es válido o la tarea ya está completada :)")
            except Exception:
                print("Ingrese un número válido por dios")
#Ordenada
def obtener_fecha(tarea):
    return tarea[0] #El elememto 0 de la lista va a ser la fecha

def listaordenada():
    tareas = [] #Para agregar las dos listas en una 
    with open('TareasP.txt', 'r') as archivo:
        conte= archivo.readlines()
        for linea in conte:
            f, t, d, p = linea.strip().split(',')
            tareas.append((f, t, d, p, 'Pendiente'))

    with open('TareasC.txt', 'r') as archivo:
        con= archivo.readlines()
        for linea in con:
            f, t, d, p = linea.strip().split(',')
            tareas.append((f, t, d, p, 'Completada'))
            
    tareas_ordenadas = sorted(tareas, key=obtener_fecha) #La función key sirve para encontrar un dato y lo evalue en el sorted
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
    cantidadT_Pendiente()
    cantidadTCompletada()
    listaordenada()
    
def cantidadT_Pendiente(): #Estas ya son individuales para cada archivo pidiendo que lea los elementos que tienen
    with open('TareasP.txt', 'r') as archivo:
        contenido = archivo.readlines()
        cantidad_pendientes = len(contenido)
        print(f"Hay {cantidad_pendientes} tareas pendientes registradas.")
        
def cantidadTCompletada():
    with open('TareasC.txt', 'r') as archivo:
        content = archivo.readlines()
        completadas = len(content)
        print(f"Hay {completadas} tareas completadas registradas.")

#Editar tareas
def editarcompletadas():
    while True:
        completadas = [i for i, s in enumerate(status) if s == "Completada"]
        if not completadas:
            print("No hay tareas completadas para editar, mmm, que sorpresa...")
            return
        else:
            print("------TAREAS COMPLETADAS------")
            Mos()
        try:
            num = int(input("Ingrese el número de la tarea que desea editar: ")) - 1
            if num in completadas:
                tarea = input("Nombre de la tarea:")
                while not tarea.strip():
                    print("Ingrese un nombre de tarea válido,¿quien deja las respuestas en blanco?")
                    tarea = input("Nombre de la tarea:")
                descripcion = input("Descripción de la tarea:")
                while not descripcion.strip():
                    print("Ingrese una descripción válida bichillo, no sea malo :)")
                    descripcion = input("Descripción de la tarea:")
                fech = input("Ingrese la nueva fecha de la tarea (dd/mm/aaaa): ")
                while not validar(fech):
                     print("Formato de fecha incorrecto (dd/mm/aaaa), tienes que poner algo como 15/09/2021")
                     fech = input("Ingrese la nueva fecha de la tarea (dd/mm/aaaa): ")
                while True:
                    precio = input("Ingrese el nuevo precio de la tarea: ")
                    try:
                        precio = float(precio)
                        break
                    except ValueError:
                        print("Por favor, ingrese un valor numérico, es un precio")
                listaP[num] = tarea
                listaD[num] = descripcion
                fechas[num] = fech
                listaPre[num] = precio
                print("Tarea editada exitosamente.")
                guardarT()
                break
            else:
                print("El número de tarea no es una tarea completada")
        except Exception:
            print("Por favor, ingrese un número válido")

def editarpendientes():
    while True:
        pendientes = [i for i, s in enumerate(status) if s == "Pendiente"]
        if not pendientes:
            print("No hay tareas pendientes para editar, ¿por qué seleciona esta opción entonces?.")
            return
        else:
            print("------TAREAS PENDIENTES------")
            pendiente()
        try:
            num = int(input("Ingrese el número de la tarea que desea editar: ")) - 1
            if num in pendientes:  # Verifica si el número de tarea está en la lista de tareas pendientes
                tarea = input("Nombre de la tarea:").strip()
                while not tarea:
                    print("Ingrese un nombre de tarea válido,¿quien deja las respuestas en blanco?")
                    tarea = input("Nombre de la tarea:").strip()
                descripcion = input("Una descripción:").strip()
                while not descripcion:
                    print("Ingrese una descripción, no lo deje en blanco en serioooo")
                    descripcion = input("Descripción:").strip()
                fech = input("Ingrese la nueva fecha de la tarea (dd/mm/aaaa): ")
                while not validar(fech):
                     print("Formato de fecha incorrecto (dd/mm/aaaa), tienes que poner algo como 15/09/2021")
                     fech = input("Ingrese la nueva fecha de la tarea (dd/mm/aaaa): ")
                while True:
                    precio = input("Ingrese el nuevo precio de la tarea: ")
                    try:
                        precio = float(precio)
                        break
                    except ValueError:
                        print("Por favor, ingrese un valor numérico, es un precio")
                listaP[num] = tarea #Lo más destacante, evaluado en el indice que le dimos en num permite que sea reemplazado por los nuevos valores
                listaD[num] = descripcion
                fechas[num] = fech
                listaPre[num] = precio
                print("Tarea editada exitosamente.")
                guardarT()
                break
            else:
                print("El número de tarea no es una tarea pendiente")
        except (ValueError, IndexError):
            print("Por favor, ingrese un número válido")

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
                    print("Formato de fecha incorrecto (dd/mm/aaaa), tienes que poner algo como 15/09/2021")
            while True:
                p = input("Valor aproximado de la tarea:")
                try:
                    p = float(p)
                    break
               
                except ValueError:
                    print("Por favor, ingrese un valor numérico")    
            listaP.append(t)
            listaD.append(d)
            listaPre.append(p)
            fechas.append(f)
            status.append("Pendiente")
            guardarT() #Guarda las tareas al agregar una
            print("Tarea agregada con éxito y sin tropiezos!")
            
        elif menu == '2':
            if 0==len(listaP):
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
                           
        elif menu == '3':
             if "Completada" in status:
                 Mos()
                 print("-------------------------")
                 completadas = [i for i, s in enumerate(status) if s == "Completada"]
                 if completadas:
                     opcion = input("¿Desea marcar una tarea completada como pendiente? (s/n): ").lower()
                 if opcion == 's':
                     wrong()
                 elif opcion =='n':
                     print("Oki pues")
                 else:
                     print("Esa no es una opción válida")
             else:
                 print("No hay tareas completadas aún")

        elif menu == '4':
            total_final()
            
        elif menu == '5':
            eliminar_tarea_pendiente()

        elif menu=='6':
            cantidadTotal()
            
        elif menu=='7':
            if 0==len(listaP):
                print("Ooops, no existen tareas")
            else:
                while True:
                    print("Editar tareas:")
                    print("a.Pendientes")
                    print("b.Completadas")
                    print("c. Dejarlo así")
                    op=input("Elija una opción:").lower()
                    if op== 'a':
                        editarpendientes()
                    elif op=='b':
                        editarcompletadas()
                    elif op=='c':
                        break
                    else:
                        print("Opción inválida :/")
                    
        elif menu == '8':
              print("Hasta luego :)")
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
            print("Pienselo :)")
            print("-----------------------")
            bienvenida()
        else:
            print("Omg.. que sorpresa, tan temprano y ya desafiando")
        respuesta= input("Ingrese una opción(S/N):").lower()
        
def bienvenida():
    print("Bienvenido a la mejor app de organización de tareas, acá te permitimos gestionar tus tareas y gastos de manera sencilla :)")
    usuario = input("Ingrese su nombre: ").strip()
    while not usuario:  # Verificar si el usuario ha ingresado un nombre en blanco
        print("Por favor, ingrese su nombre por fa :(")
        usuario = input("Ingrese su nombre: ")

    print(f"Bienvenid@ {usuario}! ¿Desea ingresar al menú?")
    respuesta()
bienvenida() #La respuesta se define antes de bienvenida para que no hayan errores de definiciones y la bienvenida queda como un main afuera de todo.

   
          



   
                 


            

   

     

        


        
    

