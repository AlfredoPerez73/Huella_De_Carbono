

# Programa que calcule la huella de carbono de una persona
# dependiendo de los datos que se ingresen

# (------- Referencias -------)
# http://huelladeciudades.com/AppHCCali/main.html
# https://calculator.carbonfootprint.com/calculator.aspx?lang=es


# (------- Presentacion del programa -------)
print("--------------------------------------------------------------")
print("------------------------- Bienvenido -------------------------")
print("--------------------------------------------------------------")
print("")

print("--------------------------------------------------------------")
print("-------------------- Interfaz de algorimos -------------------")
print("--------------------------------------------------------------")

texto = """
Prgrama que calcule la huella de carbono de una persona dependiendo
de los valores que se le ingresen.
"""
print(texto)
menu = """
-------------------- Opciones del programa -------------------

1. Prgrama que calcule la huella de carbono de una persona dependiendo
de los valores que se le ingresen.
--------------------------------------------------------------
2. Salir del programa.
"""
print("--------------------------------------------------------------")


# (------- Inicializacion de variables -------)
pop = True
arregloTotal = []


# (------- Ciclo repetitivo -------)
while pop == True:
    print(menu)
    print("--------------------------------------------------------------")

    op = int(input("Selecciona una opcion: \n"))
    print("--------------------------------------------------------------")
    if op == 1:
        print("1. Prgrama que calcule la huella de carbono de una persona dependiendo de los valores que se le ingresen. \n")
        print("--------------------------------------------------------------")
        # (------- Recoleccion de datos -------)
        cantidad = float(input("¿Cuantas personas viven en tu casa? \n"))
        print("--------------------------------------------------------------")
        mensualidad = float(input("¿Aproximadamente, cuanto paga mensualmente por el servicio de energia? \n"))
        print("--------------------------------------------------------------")
        # Cantidad de energia por kilovatio de mes
        energia = mensualidad / 265.80
        # Consumo cO2 de mes
        energia2 = (164.38 * energia) / cantidad
        
        
        print ("¿Que tipo de gas usas?")
        gas= float(input( """
        * Ingrese 1 si utiliza gas natural
        * Ingrese 2 si utiliza gas GPL
        \n"""))
        print("--------------------------------------------------------------")

        gasnt = 0
        gpl = 0
                
        if gas == 1:
            gas = float(input("Ingrese cuanto paga al mes por gas natural \n"))
            # Consumo de gas por metro cubico
            metro3 = gas/113.82 
            # Cantidad de cO2 producida por metro cubico de gas
            gasnt = 2150 * (metro3 / 9.23)
            print("--------------------------------------------------------------")
              
        elif gas == 2:
            gas = float(input("Ingrese cuanto tanques gastas de GPL mensual \n"))
            # Consumo de cO2 mediante tanques de 10 libras por mes
            gpl = 102.840 * gas
            print("--------------------------------------------------------------")

        
        print("Digite los km que recorre en los medios de transporte")
        mediotrans="""
        * Si no Utliza indique (0)
        """
        print(mediotrans)
        print("--------------------------------------------------------------")        
        kmh = float(input("¿Cuantos kilomestros recorre en motocicleta? \n"))
        # Contaminacion de cO2 de una moto
        motocicleta = 162 * kmh 
        kmh = float(input("¿Cuantos kilomestros recorre en automovil? \n"))
        # Contaminacion de cO2 de una carro
        automovil = 143 * kmh
        kmh = float(input("¿Cuantos kilomestros recorre en buceta? \n"))
        # Contaminacion de cO2 de un bus
        buceta = 5.23 * kmh

        print("--------------------------------------------------------------")        

        
        print("Digite si este mes ha montado un avion")
        vuelos="""
        * Si no Utliza indique (0)
        """
        print(vuelos)
        print("--------------------------------------------------------------") 
        kmh = float(input("¿Cuantos kilomestros recorrio? \n"))
        avion = 3.16 * kmh
        # Contaminacion de cO2 de un avion por pasajero

        # (------- Procesos de calculos cO2 -------)
        # Cantidad de cO2 por todos los servicios juntos
        sumaServicios = (energia2 + gasnt + gpl) * 12
        # Cantidad de cO2 por todos los medios de transporte juntos
        sumatotal = (motocicleta + automovil + buceta + avion) * 365
        # Cantidad de cO2 gastada por cada respiracion humana
        rt = 1.200 * 365
        totalrt = sumatotal + sumaServicios + rt
        kgcO2 = totalrt / 1000 
        toncO2 = kgcO2 / 1000
        print("")


        # (------- Resultados del algoritmo -------)
        print("------------------------- Resultados -------------------------")
        print("Su huella de carbono es: ", "{:.2f}".format (toncO2), "Toneladas al año.")
        print("--------------------------------------------------------------")


        # (------- Estructura condicional -------)
        if toncO2 > 1.6:
            print("Lamentablemente el resultado de tu Huella es alto, te recomendamos que la reduzcas aplicando los consejos de la siguiente manera:")
            # Recomendaciones
            recomendaciones = """
        * Sustituir los focos convencionales por focos de bajo consumo.
        * Apagar las luces que no necesito.
        * Desenchufar la televisión si no estoy viendo.
        * Apagar la computadora si no la uso.
        * Ducharme máximo 5 minutos. Las duchas cortas no solo ahorran agua, sino que también ahorran la energía que se necesita para calentarla.
        * Utilizar más transporte público o compartir mi auto con quienes están en mi ruta.
        * Caminar o usar la bicicleta para distancias cortas.
        * Llevar mi auto al taller regularmente. Esto es para asegurarte que los filtros de combustible, aire y aceite sean reemplazados oportunamente. Cuando tu auto funciona bien genera menos emisiones.
        * Reducir el número de vuelos en avión. El avión es uno de los transportes que más emisiones generan, intenta encontrar un vuelo directo en lugar de uno con escalas.
                """
            print(recomendaciones)
                        
                                
        elif toncO2 >= 1.3 and toncO2 <= 1.5:
            print("Su huella de cO2 es media. Siga las siguentes recomendaciones")
            recomendaciones = """
        * Sustituir los focos convencionales por focos de bajo consumo.
        * Apagar las luces que no necesito.
        * Desenchufar la televisión si no estoy viendo.
        * Apagar la computadora si no la uso.
        * Ducharme máximo 5 minutos. Las duchas cortas no solo ahorran agua, sino que también ahorran la energía que se necesita para calentarla.
        * Utilizar más transporte público o compartir mi auto con quienes están en mi ruta.
        * Caminar o usar la bicicleta para distancias cortas.
        * Llevar mi auto al taller regularmente. Esto es para asegurarte que los filtros de combustible, aire y aceite sean reemplazados oportunamente. Cuando tu auto funciona bien genera menos emisiones.
        * Reducir el número de vuelos en avión. El avión es uno de los transportes que más emisiones generan, intenta encontrar un vuelo directo en lugar de uno con escalas.
                """
            print(recomendaciones)
                            
        elif toncO2 >= 0 and toncO2 <= 1.2:
            print("Su huella de cO2 es baja. Sin embargo, siga las siguentes recomendaciones")
            recomendaciones = """
        * Sustituir los focos convencionales por focos de bajo consumo.
        * Apagar las luces que no necesito.
        * Desenchufar la televisión si no estoy viendo.
        * Apagar la computadora si no la uso.
        * Ducharme máximo 5 minutos. Las duchas cortas no solo ahorran agua, sino que también ahorran la energía que se necesita para calentarla.
        * Utilizar más transporte público o compartir mi auto con quienes están en mi ruta.
        * Caminar o usar la bicicleta para distancias cortas.
        * Llevar mi auto al taller regularmente. Esto es para asegurarte que los filtros de combustible, aire y aceite sean reemplazados oportunamente. Cuando tu auto funciona bien genera menos emisiones.
        * Reducir el número de vuelos en avión. El avión es uno de los transportes que más emisiones generan, intenta encontrar un vuelo directo en lugar de uno con escalas.
        """
            print(recomendaciones)
            print("--------------------------------------------------------------")
            print("")


        arregloTotal.append(toncO2)


        # (------- Arreglos -------)
        print("----------------- Lista de cO2 por tonelada ------------------")
        print("El total de arreglos de huella de carbono que se calcularon fue: ", arregloTotal)
        print("")

    elif op == 2:
        
        pop = False


            
print("--------------------------------------------------------------")
print("-------------------- Saliste del programa --------------------")
print("--------------------------------------------------------------")
print("")
            
            
# (------- Propietarios del algoritmo -------)
print("------------------------- Creadores --------------------------")
print("* Alfredo Jose Perez")
print("* Javier Avila Galindo")
print("* Faber Martinez Marrugo")
print("")
    
    


        # Alfredo Jose Perez
        # Javier Avila Galindo
        # Faber Martinez Marrugo

