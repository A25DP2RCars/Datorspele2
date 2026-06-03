# Importējam funkcijas no citiem failiem

from board import izveidot_deli
from chess_functions import paradit_deli
from chess_functions import parvietot_figuru


# Galvenā programma

def spele():

    # Izveidojam šaha dēli
    delis = izveidot_deli()

    print("Šaha spēles apmācības programma")
    print("Lai izietu, ievadi -1")

    while True:

        # Parādām dēli
        paradit_deli(delis)

        # Lietotājs izvēlas figūru
        r1 = int(input("Figūras rinda: "))

        # Programmas beigšana
        if r1 == -1:
            print("Spēle pabeigta!")
            break

        c1 = int(input("Figūras kolonna: "))

        # Lietotājs izvēlas jauno vietu
        r2 = int(input("Jaunā rinda: "))
        c2 = int(input("Jaunā kolonna: "))

        # Pārvietojam figūru
        parvietot_figuru(delis, r1, c1, r2, c2)

        print("Gājiens veikts!")


# Palaižam programmu
spele()
