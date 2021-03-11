#Nim_Nama_TGx
import numpy as r
import statistics as rd
from numpy.linalg import inv
import matplotlib.pyplot as rdm

def lin_reg(X,Y):
    '''
    Melakukan linear regresi
    params:
    X: variabel bebas(independent), r.array 1D
    Y: variabel terikat(independent), r.array 1D
    return:
    (b_0, b_1): b_0 = konstanta, b_1 = gradien, tuple
    '''
    covXY = rd.cov_data(X,Y)
    std_X = rd.std_data(X)
    avg_X = rd.mean_data(X)
    avg_Y = rd.mean_data(Y)

    b_1 = covXY / (std_X ** 2)
    b_0 = avg_Y - b_1* avg_X

    return (b_0, b_1)

def goodness_fit(b_0, b_1, X,Y):
    '''
    Menghitung koefisien determinasi
    params:
    X: variabel bebas, r.array 1D
    Y: variabel terikat, r.array 1D
    return:
    r_2 = koefisien determinasi
    '''
    avg_Y = rd.mean_data(Y)
    N = len(Y)

    ss_t = 0
    ss_r = 0
    for i in range(N):
        ss_t = ss_t + (Y[i] - avg_Y)**2

        Y_cal_i = b_0 + b_1*X[i]
        ss_r = ss_r + (Y_cal_i - avg_Y)**2

    r_2 = ss_r / ss_t
    return r_2
def lsq_reg(X,Y):
    '''
    Menghitung koefisien determinasi
    params:
    X: variabel bebas, r.array 1D
    Y: variabel terikat, r.array 1D
    return:
    b = matriks koefisien regresi
    '''
    #00_buat matriks kernel --> A
    N = len(X)

    A = r.ones((N,2))
    A[:,1] = X

    Y = Y.T
    b = inv(A.T@A)@A.T@Y
    return b

if __name__=="__main__":
    #00_import data temperatur
    data = r.loadtxt('temperatur.txt', skiprows=1)

    #01_linear regresi dg statistika dasar
    b_0, b_1 = lin_reg(data[:,0],data[:,1])
    Y_kalkulasi = b_0 + b_1*data[:,0]

    #02_linear regresi dg LSE
    b = lsq_reg(data[:,0], data[:,1])
    Y_kalkulasi_lse = b[0] + b[1]*data[:,0]
    
    #03_plot data
    rdm.scatter(data[:,1], data[:,0], label='Data Observasi')
    rdm.plot(Y_kalkulasi, data[:,0], label='Regresi-Kovariansi')
    rdm.plot(Y_kalkulasi_lse, data[:,0], '--r', label='Regresi LSE')
    rdm.xlabel('Temperatur [.deg]')
    rdm.ylabel('Kedalaman [m]')
    rdm.ylim(max(data[:,0]), 0)
    rdm.legend()
    rdm.show()