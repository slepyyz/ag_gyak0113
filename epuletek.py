from Epulet import Epulet


def beolvasas():
    epuletek = []
    f = open("epulet.txt", "r", encoding="utf8")
    f.readline()
    sorok = f.readlines()
    f.close()
    for sor in sorok:
        soradatok = sor.split("$")
        epulet = Epulet(soradatok[0], soradatok[1], soradatok[2], soradatok[3], soradatok[4], soradatok[5])
        epuletek.append(epulet)
    return epuletek


def adatok_szama(epuletek):
    print(f"III/A\n\tAz épületek száma: {len(epuletek)}.")

# def kiir(epuletek):
#     for epulet in epuletek:
#         print(epulet)

def magasabb(epuletek):
    print("III/C:")
    magasabb=0
    for epulet in epuletek:
        magassag=epulet.magassag*3.280839895
        if magassag>555:
            magasabb+=1
    print(f"\tAz 555 lábnál magasabb épületek száma: {magasabb}")

def legoregebb(epuletek):
    print("III/D:")
    legoregebb=0
    legoregebbnev=" "
    for epulet in epuletek:
        jelenlegido = 2025-epulet.epult
        if jelenlegido > legoregebb:
            legoregebb=jelenlegido
            legoregebbnev=epulet.orszag
    print(f"\tA legöregebb épület országa: {legoregebbnev}")