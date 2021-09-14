"""" crear lista q contenga los numeros del 1 al 300 de 3 en 3"""

def run():
    mi_lista = [i for i in range(1,300,3)]
    #for i in range(1, 300,3):
    #mi_lista.append(i)     

    print(mi_lista)

if __name__ == "__main__":
    run()