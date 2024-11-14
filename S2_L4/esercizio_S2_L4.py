#Calcoliamo il perimetro delle figure

x = input("Vuoi calcolare il perimetro di una figura?: (y/n) ")

while x == "y":
    figura = input("Di quale figura vuoi calcolare il perimetro?: ")
    if figura == "quadrato":
        x = int(input("Inserisci il lato del tuo quadrato: "))
        p1 = x * 4
        print(f"Il perimetro del tuo quadrato è: ", p1)
        break
    elif figura == "cerchio":
        y = int(input("Inserisci il raggio del tuo cerchio: "))
        pGreco = 3.14
        p2 = float(2 * y * pGreco)
        print(f"Il perimetro del tuo cerchio è: ", p2)
        break
    elif figura == "rettangolo":
        a = int(input("Inserisci la base del tuo rettangolo: "))
        b = int(input("Ora inserisci l'altezza del tuo rettangolo: "))
        p3 = a * 2 + b * 2
        print(f"Il perimetro del tuo rettangolo è: ", p3)
        break
    else:
        y = input("Puoi scegliere un altra figura?: (y/n) ")
        if y == "y":
            print("Facciamo un passo indietro")
        else:
            print("Arrivederci!")
            break
