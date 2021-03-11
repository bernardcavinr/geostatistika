#Nim_Nama_TGx
import numpy as rd
import matplotlib.pyplot as rdm
data = rd.loadtxt('porositas.txt')
N_bins = 5
frekuensi, bins, patches = rdm.hist(data, N_bins, density=True, facecolor='g', alpha=0.75)
rdm.ylabel('Frekuensi')
rdm.xlabel('Porositas [v/v]')
rdm.grid(True)
rdm.show()