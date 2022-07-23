while True:
    try:
        num=int(input("Inserte un numero entero: "))
        divisor=0
        for i in range(num):
            if num%(i+1)==0:
                divisor+=1
        if divisor>2:
            print(num,"es un numero compuesto\n")
        else:
            print(num,"es un numero primo\n")
    except(ValueError):
        print("Ha introducido un valor invalido\n")
