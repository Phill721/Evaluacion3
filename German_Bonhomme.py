from os import system
import random
def clear():
    system("cls")
def pause():
    print()
    input("Presione enter para continuar...")
def registrar():
    disp6=0 #Contadores
    disp10=0 #Contadores
    disp20=0 # Contadores
    clear()
    name=input("Ingrese un nombre y apellido: ")
    direccion=input("Ingrese su direccion: ")
    if len(name)<=0 or len(direccion)<=0:
        print("Error! | Nombre no valido")
    else:
        comuna=input("""
                     ********************************************************************
                     COMUNAS DISPONIBLES: CHIGUAYANTE | CONCEPCION | HUALPEN | TALCAHUANO
                     ********************************************************************
                     Primera letra debe ser mayuscula!
                     ********************************************************************
                     Ingrese una comuna: """)
        if comuna not in comunas:
            clear()
            print("Error! | Comuna no disponible")
        else:
            while True:
                clear()
                try:
                    detalles=input("""
                                    *************************
                                    Dispensadores disponibles
                                    *************************
                                    1- 6 litros
                                    2- 10 litros
                                    3- 20 litros
                                    4- continuar
                                    5- cancelar
                                    *************************
                                    Ingrese una opcion: """)
                    match detalles:
                        case "1":
                            clear()
                            disp6+=1
                            print(f"Seleccion exitosa | Disp. 6lts: {disp6}")
                            pause()
                        case "2":
                            clear()
                            disp10+=1
                            print(f"Seleccion exitosa | Disp. 10lts: {disp10}")
                            pause()
                        case "3":
                            clear()
                            disp20+=1
                            print(f"Seleccion exitosa | Disp. 20lts: {disp20}")
                            pause()
                        case "4":
                            if disp6==0 and disp10==0 and disp20==0:
                                clear()
                                print("Error! | Pedido no valido")
                                pause()
                            else:
                                clear()
                                pedido={
                                    "ID":random.randint(111111,999999),
                                    "Nombre":name,
                                    "Direccion":direccion,
                                    "Comuna":comuna,
                                    "6lts":disp6,
                                    "10lts":disp10,
                                    "20lts":disp20
                                }
                                lista.append(pedido)
                                print("Pedido registrado!")
                                break
                        case "5":
                            clear()
                            print("Pedido cancelado!")
                            pause()
                            break
                        case other:
                            clear()
                            print("Error! | Opcion no valida")
                            pause()

                except ValueError:
                    clear()
                    print("Error! Dato incorrecto")
                    break
    pause()
def listar(lista):
    clear()
    if len(lista)==0:
        print("Error! | No hay pedidos registados!")
    else:
        for pedido in lista:
            print(f"""
                ID: {pedido["ID"]} | Cliente: {pedido["Nombre"]} | Direccion: {pedido["Direccion"]} |Comuna: {pedido["Comuna"]} | Disp. 6lts: {pedido["6lts"]} | Disp. 10lts: {pedido["10lts"]} | Disp. 20lts: {pedido["20lts"]}""")
            print()
    pause()
def imprimir(lista):
    clear()
    global pedido
    if len(lista)==0:
        print("Error! | No hay pedidos registrados")
    else:
        f=open("Detalles.csv","w")
        f.write("ID;Cliente;Direccion;Comuna;Disp._6lts;Disp._10lts;Disp._20lts\n")
        for pedido in lista:
            f.write(f"{pedido["ID"]};{pedido["Nombre"]};{pedido["Direccion"]};{pedido["Comuna"]};{pedido["6lts"]};{pedido["10lts"]};{pedido["20lts"]}\n")
            print("Plantilla impresa!")
    pause()
def buscar(lista):
    global pedido
    clear()
    if len(lista)==0:
        print("Error! | No hay pedidos registrados!")
    else:
        search=int((input("Ingrese el ID del pedido que desea buscar: ")))
        if search in lista[pedido["ID"]]:
            print("Error! | No hay pedido registrado con ese ID")
        else:
            for pedido in lista:
                print(f"""
                ID: {pedido["ID"]} | Cliente: {pedido["Nombre"]} | Direccion: {pedido["Direccion"]} |Comuna: {pedido["Comuna"]} | Disp. 6lts: {pedido["6lts"]} | Disp. 10lts: {pedido["10lts"]} | Disp. 20lts: {pedido["20lts"]}""")
                print()
    pause()

    
lista=[]
pedido={}
comunas=["Chiguayante","Concepcion","Hualpen","Talcahuano"]
disp6=0 #Contadores
disp10=0 #Contadores
disp20=0 # Contadores
while True:
    clear()
    print("""
          *******************************
          LEMON'S PURIFIED WATER SERVICES
          *******************************
          1- Registrar pedido
          2- Listar todos los pedidos
          3- Imprimir hoja de ruta
          4- Buscar por ID
          5- Salir
          *******************************""")
    op=input("Ingrese una opcion: ")
    match op:
        case "1":
            registrar()
        case "2":
            listar(lista)
        case "3":
            imprimir(lista)
        case "4":
            pass
        case "5":
            import sys
            sys.exit()
        case "secret":
            clear()
            print("""
                  **********************************
                  ¡¡¡HAS ENCONTRADO UN EASTER EGG!!!
                  **********************************""")
            pause()
        case other:
            clear()
            print("Error! | Opcion no valida!")
            pause()