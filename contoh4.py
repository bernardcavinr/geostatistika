#Nim_Nama_TGx
import numpy as r
import statistics as rd
import matplotlib.pyplot as rdm

def cross_corr(Y1, Y2, lag):
    Y1_bar = r.mean(Y1)
    Y2_bar = r.mean(Y2)

    T = len(Y1)

    s_y1 = rd.var_data(Y1)
    s_y2 = rd.var_data(Y2)

    lag_k = []
    r_y1y2 = []
    for k in range(-lag, lag+1, 1):
        c_y1y2 = 0
        if k>=0:
            for t in range(T-k):
                c_y1y2 = c_y1y2 + (Y1[t] - Y1_bar) * (Y2[t+k] - Y2_bar)
       
        else:
            for t in range(T+k):
                c_y1y2 = c_y1y2 + (Y2[t] - Y2_bar) * (Y1[t-k] - Y1_bar)
       
        r_y1y2.append(c_y1y2 / (s_y1 * s_y2))
        lag_k.append(k)

    return r_y1y2, lag_k

if __name__=="__main__":
    ##00_Input Data
    data = r.loadtxt('poroperm.txt', skiprows=1)
    ##01_Cross-correlation antara data
    r_y1y2, lag_k = cross_corr(data[:,1],data[:,2], 25)
    ##02_Plot data
    rdm.figure(1)
    rdm.plot(lag_k, r_y1y2)
    rdm.xlabel('Lag')
    rdm.ylabel('Cross-correlation')
    rdm.grid()
    rdm.show()
