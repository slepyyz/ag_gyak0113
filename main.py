import epuletek
import bevezetes
import sorozat

bevezetes.bekeres()
ermek=sorozat.ermedobas()
sorozat.kiiras(ermek)
fejek=sorozat.fejek_szama(ermek)
sorozat.konzol_kiir(fejek)
sorozat.file_kiir(fejek)
lista = epuletek.beolvasas()
epuletek.adatok_szama(lista)
epuletek.magasabb(lista)
epuletek.legoregebb(lista)