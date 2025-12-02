#név$város$ország$magasság(m)$emelet$épült

class Epulet:
    def __init__(self, nev, varos, orszag, magassag, emelet, epult):
        self.nev = str(nev)
        self.varos = str(varos)
        self.orszag = str(orszag)
        self.magassag= float(magassag.replace(",","."))
        self.emelet= int(emelet)
        self.epult= int(epult)

    def __str__(self):
        return f"név: {self.nev}\nváros: {self.varos}\nország: {self.orszag}\nmagasság: {self.magassag}\nemelet: {self.emelet}\népült: {self.epult}\n"