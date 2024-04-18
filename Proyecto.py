# -----Menú------
print("Bienvenido a la mejor app de organización de tareas, acá te permitimos gestionar tus tareas y gastos de manera sencilla :)")

# Iniciar sesión
usuario = input("Ingrese su nombre de usuario:")


# Dar la bienvenida y preguntar si desea ingresar
print(f"Bienvenid@ {usuario}! ¿Desea ingresar al menú?")

# Ingresar opción
respuesta = input("Ingrese una opción (Sí, No, Luego):")

# Respuesta
if respuesta == 'No' or respuesta == 'Luego':
    print("Nos vemos pronto :)")
elif respuesta == 'Sí':
    print("Bienvendid@, gracias por confiar en nosotros ;)")
    menu = int(input("Menú Principal:\n1-Agregar tarea\n2-Ver tareas pendientes\n3-Ver tareas completadas\n4-Ver el coste total\n5-Eliminar tarea\n6-Salir \n"))
    
while menu!= 0:
    if menu == 1 or menu == 2 or menu == 3 or menu == 4 or menu == 5:
        print("Opción aún no habilitada")
    elif menu == 6:
        print("Saliendo del programa. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida :)")
        
    menu = int(input("Menú Principal:\n1-Agregar tarea\n2-Ver tareas pendientes\n3-Ver tareas completadas\n4-Ver el coste total\n5-Eliminar tarea\n6-Salir \n"))
        

else:
    print("Opción no válida. Nos vemos pronto :)")
