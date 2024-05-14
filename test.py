import random

def vytvor_nahodne_cislo():
    delka = random.randint(1, 10)  
    return [random.randint(1, 100) for _ in range(delka)]  

def zkontroluj_delku_cisla(cislo):
    print("Hádej délku čísla:", cislo)
    tip = int(input("Zadej délku čísla: "))
    if tip == len(cislo):
        print("Správně!")
        return 1
    else:
        print("Špatně!")
        return 0

def zacni_hru_s_cisly():
    kola = random.randint(1, 15)  
    celkove_body = 0

    print("Vítejte ve hře!")
    print("Budete hrát", kola, "kol.")

    for _ in range(kola):
        cislo = vytvor_nahodne_cislo()
        celkove_body += zkontroluj_delku_cisla(cislo)

    print("Konec hry! Celkový počet bodů:", celkove_body)

zacni_hru_s_cisly()


