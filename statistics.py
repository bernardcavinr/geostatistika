#Nim_Nama_TGx

def mean_data(X):
    '''
    Params:
    X : Sekeuens data,np.array 1D
    Return:
    avg : Nilai rata-rata, float
    '''
    N = len(X) #menghitung banyak data
    sum_X = 0
    for i in range(N):
        sum_X = sum_X + X[i] #menjumlahkan tiap elemen data
    avg = sum_X/N #menghitung nilai rata-rata, jumlah dibagi banyak data
    return avg



def min_data(X):
    '''
    Params:
    X: Sekuens data, np.array 1D
    Return:
    min_X : Nilai X paling kecil
    '''
    N = len(X)
    min_X = X[0]
    for i in range(1,N):
        if X[i] < min_X :
            min_X = X[i]
    return min_X

def max_data(X):
    '''
    Params :
    X: Sekuens data, np.aray 1D
    Return :
    min_X : Nilai X paling Besar
    '''
    N = len(X)
    max_X = X[0]

    for i in range(1,N):
        if X[i] > max_X:
            max_X = X[i]
    return max_X

def var_data(X, mode ='populasi'):
    '''
    Params :
    X: Sekuens data, np.array 1D
    mode : populasi(default) dan sampel
    Return :
    var_X : Nilai variasi X
    '''
    N = len(X)
    avg_X = mean_data(X)

    sum_X = 0
    for i in range(N):
        sum_X = sum_X + (X[i]-avg_X)**2

    if mode == 'populasi':
        var_X = sum_X/N
    elif mode == 'sampel' :
        var_X = sum_X/(N-1)
    else:
        print('Pastikan hanya memilihmode populasi atau sampel')
    return var_X

def std_data(X):
    '''
    Params:
    X : Sekuens data, np.array 1D
    mode : populasi(default) dan sampel
    Return :
    std_X : Nilai standard deviasi X
    '''
    var_X = var_data(X, mode='populasi') #variasi data X
    std_X = var_X**(0.5)
    return std_X

def median_data(X):
    '''
    Params:
    X:Sekuens data, np.array 1D
    Return :
    M : Nilai median X
    '''
    X = sorted(X)
    N = len(X)
    if N%2 ==0:
        n = int(N/2 - 1)
        m = int(N/2)
        M = (X[n] + X[m])/2
    else :
        i = int((N)/2)
        M = X[i]
    return M

def cov_data(X,Y):
    '''
    Params :
    X : Sekuens data 1, np.array 1D
    Y : Sekuens data 2, np.array 1D
    Return:
    cov_XY : Nilai covariansi XY
    '''
    N = len(X)
    avg_X = mean_data(X)
    avg_Y = mean_data(Y)
    sum_cov = 0
    for i in range(N):
        sum_cov = sum_cov + (X[i] - avg_X)*(Y[i] - avg_Y)
        cov_XY = sum_cov / (N)

    return cov_XY

def corr_coeff(X,Y):
    '''
    Params:
    X : Sekuens data 1, np.array 1D
    Y : Sekuens data 2, np.array 1D
    Return:
    r_xy : koefisien Korelasi XY
    '''
    cov_XY = cov_data(X,Y)
    std_X = std_data(X)
    std_Y = std_data(Y)

    r_xy = cov_XY / (std_X * std_Y)

    return r_xy

if __name__ == "__main__":
    import numpy as np

    data = np.loadtxt('brachiopod.txt',skiprows=1)
    X = data[:, 0]
    Y = data[:, 1]

    #00_mean
    X_avg = mean_data(X)
    Y_avg = mean_data(Y)
    print('Mean X :{0}, mean Y :{1}'. format(X_avg,Y_avg))

    #01_Min_Max
    X_min = min_data(X)
    Y_min = min_data(Y)
    X_max = max_data(X)
    Y_max = max_data(Y)
    print('Min X :{0}, Max X :{1}'. format(X_min,X_max))
    print('Min Y :{0}, Max Y :{1}'. format(Y_min,Y_max))

    #02_median
    X_med = median_data(X)
    Y_med = median_data(Y)
    print('Med X :{0}, Med Y :{1}'. format(X_med,Y_med))

    #03_variansi
    X_var = var_data(X)
    Y_var = var_data(Y)
    print('Var X :{0}, Var Y :{1}'. format(X_var,Y_var))

    #04_Standard_Deviasi
    X_std = std_data(X)
    Y_std = std_data(Y)
    print('Std X :{0}, Std Y :{1}'. format(X_std,Y_std))

    #05_Kovariansi
    XY_cov = cov_data(X,Y)
    print('Kovariansi XY :', XY_cov)

    #06_Korelasi
    koef_kor = corr_coeff(X,Y)
    print('Koefisien Korelasi XY :', koef_kor)