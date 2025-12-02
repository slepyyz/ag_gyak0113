import random

def ermedobas():
    print("II/A, B, C")
    ermedobas = []
    for i in range(7):
        dobas = random.randint(0, 1)
        ermedobas.append(dobas)
    return ermedobas

def kiiras(ermedobas):
    fejvagyiras = []
    for dobas in ermedobas:
        if dobas==1:
            fejvagyiras.append("FEJ")
        else:
            fejvagyiras.append("ÍRÁS")
    print(f"\t{"-".join(fejvagyiras)}")
    return fejvagyiras

def fejek_szama(fejvagyiras):
    print("II/D, E")
    fejek=0
    for erme in fejvagyiras:
        if erme==1:
            fejek+=1
    return fejek

def konzol_kiir(fejek):
    print(f"\tA fejek száma: {fejek}")

def file_kiir(fejek):
    file=open("fejek.txt", "w", encoding="UTF-8")
    file.write(f"II/F\n\tA fejek száma: {fejek}")