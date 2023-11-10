# Crea un menú con las opciones de agendar contacto y ver información de contacto.
# Para agendar se solicitará al usuario: nombre, apellido, teléfono, dirección.
# Para ver informacion se pedirá el nombre y apellido.
# La información será un listado de diccionarios, donde cada diccionario tendrá como claves lo solicitado al usuario y como valor lo que ingrese el usuario. A su vez, este listado debe estar guardado en un archivo JSON.
# ---------------------------------------------------------------------------------------------------------------------------------

import json


# FX PARA QUE EL USUARIO INDIQUE SI QUIERE REALIZAR OTRA OPERACION
def continuar_operando():
    print('\n¿Desea realizar otra operación? (y/n)')
    decision = input('').lower()
    if decision == 'yes' or decision == 'y':
        main()
    else:
        print('\nOk. Nos vemos pronto. ¡Adiós!\n')
        quit()

################ FUNCIONES PROPIAS DEL PROGRAMA #################

# FX QUE AGENDA LOS CONTACTOS QUE QUIERA EL USUARIO. 
def agendar_contacto():

    datos = []

    while True: 
        contacto = {}
        print("Ingrese los datos de contacto a continuación...")
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        telefono = input("Ingrese telefono: ")
        direccion = input("Ingrese direccion: ")

        contacto["nombre"] = nombre
        contacto["apellido"] = apellido
        contacto["telefono"] = telefono
        contacto["direccion"] = direccion
        
        datos.append(contacto)  
   
        print('\n¡Contacto creado exitosamente!\n')
        print("¿Desea agregar otro contacto? (Indique 'no' para salir)")
        decision = input("").lower()

        if decision == "no":
            break
        
    with open("contactos.json","w") as jdoc:
        json.dump(datos, jdoc, indent=4)

    
    continuar_operando() 

# FX QUE MUESTRA EL CONTACTO INDICADO POR EL USUARIO.
def ver_contacto():
    
    try:
        jdoc = open("contactos.json") 
    except:
        print("No hay registros de contactos.")
    else: 
        print("Ingrese NOMBRE y APELLIDO del contacto a continuacion...")
        nom = input("Nombre: ").capitalize()
        ape = input("Apellido: ").capitalize() 
        datos = json.load(jdoc)
        for contacto in datos:
            if contacto["nombre"] == nom and contacto["apellido"] == ape:
                print("\nDatos de contacto: ")
                print("Nombre:", contacto["nombre"])
                print("Apellido:", contacto["apellido"])
                print("Telefono:", contacto["telefono"])
                print("Direccion:", contacto["direccion"])
    continuar_operando()

# FUNCION SOLO PARA MOSTRAR EL MENU DE OPCIONES - RETORNA LA OPCION ELEGIDA POR EL USUARIO
def show_menu():
    print(
'''------------------------------------------------

- Mi lista de contactos -
¿Qué desea hacer?

1- Agendar Contacto 
2- Ver Contacto
3- Salir

-------------------------------------------------
''')
    option= input('Ingrese una opcion: ')
    return option

# FX QUE VA A EVALUAR LA OPCION QUE DESEA REALIZAR EL USUARIO  
def main(): 
    # MOSTRAMOS EL MENU DE OPCIONES Y EVALUAMOS LA OPCION ELEGIDA
    option = show_menu()
    if option == '1':
        agendar_contacto()
    elif option == '2':
        ver_contacto()
    elif option == '3':
        print('¡Adiós!')
        quit()
    else: 
        print('Opción invalida. Elija una de las opciones disponibles') 
        continuar_operando()

# ACA ARRANCA EL PROGRAMA  
if __name__ == '__main__':
    main()