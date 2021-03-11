#Nim_Nama_TGx
import numpy as r
import matplotlib.pyplot as rdm
import statistics as rd #import modul statistika yg dibuat sebelumnya

def auto_corr(Y, lag):
    '''
    Melakukan korelasi diri
    params:
    Y : Sekuen data, r.array 1D
    maks_lag: jumlah lag yang akan dilakukan
    '''
    nn = len(Y) #panjang data Y
    ac = [] #list untuk simpan hasil korelasi
    arr_lag = [] #list untuk simpan lag
    for i in range(0, lag):
        trace_a = Y[i:nn] #sekuen data 1
        trace_b = Y[:(nn-i)] #sekuen data 2
        ac.append(rd.corr_coeff(trace_a, trace_b)) #hitung korelasi antar trace
        arr_lag.append(i) #simpan lag
    return arr_lag, ac

if __name__== "__main__":
    t = r.arange(0, 2*r.pi, r.pi/100)
    f1 = 25
    f2 = 25.5
    Y = r.sin(2*r.pi*f1*t) + r.sin(2*r.pi*f2*t)

    r.random.seed(1000)
    noise = r.random.uniform(0,1,size=(len(Y)))
    
    Y_n = Y + noise
    maks_lag = 190
    lag, ac = auto_corr(Y_n, maks_lag)

    fig, ax = rdm.subplots(nrows=1, ncols=4, figsize=(10,12), sharey=False)
    fig.subplots_adjust(wspace=0.3)
    for axis in ax:
        axis.invert_yaxis()

    ax[0].plot(Y, t, linewidth=0.75)
    ax[0].set_xlabel('Amplitudo')
    ax[0].set_ylabel('Waktu')

    ax[1].plot(noise, t, 'r', linewidth=0.75)
    ax[1].set_xlabel('Amplitudo')
    ax[1].set_ylabel('Waktu')

    ax[2].plot(Y_n, t)
    ax[2].set_xlabel('Amplitudo')
    ax[2].set_ylabel('Waktu')

    ax[3].plot(ac, lag, linewidth=0.75)
    ax[3].set_xlabel('Koefisien Korelasi')
    ax[2].set_ylabel('Lag')

    rdm.show()