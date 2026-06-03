# Funkcija attēlo šaha dēli

def paradit_deli(delis):
    print()

    for rinda in delis:
        for lauks in rinda:
            print(lauks, end=" ")
        print()

    print()


# Funkcija pārvieto figūru

def parvietot_figuru(delis, r1, c1, r2, c2):

    # Saglabājam izvēlēto figūru
    figura = delis[r1][c1]

    # Pārvietojam figūru
    delis[r2][c2] = figura

    # Atbrīvojam veco vietu
    delis[r1][c1] = " "
