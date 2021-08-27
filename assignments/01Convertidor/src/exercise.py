# Escribe tus funciones abajo de esta línea
def pies_cm(pies): 
    r1 = (pies*30.48)
    return(r1)

def pulgadas_cm(pulgadas):
    r2 = (pulgadas*2.54)
    return (r2)

def yardas_cm(yardas): 
    r3 = (yardas*91.44)
    return(r3)

def main():
    # Escribe tu código abajo de esta línea
    print('1. pies a cm, 2. pulgadas a cm, 3. yardas a cm')
    operacion = str(input('Introduce una opcion: '))
    cantidad = int(input('Introduce la cantidad: '))
    if cantidad > 0 : 
        if operacion == '1': 
            r1 = pies_cm(cantidad)
            print(r1)
        elif operacion == '2': 
            r2 = pulgadas_cm(cantidad)
            print(r2)
        elif operacion == '3':
            r3 = yardas_cm(cantidad)
            print(r3)
        else:
            print('Error')
    else: 
        print('Error')
   

if __name__ == '__main__':
    main()
