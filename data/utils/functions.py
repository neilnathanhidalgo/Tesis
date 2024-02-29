import numpy as np


def mean(x):
    return np.nanmean(x)

#    return x.mean()


def max(x):
    return np.nanmax(x)
   # return x.max()


def rango(x):
    return np.nanmax(x)-np.nanmin(x)
    #return x.max()-x.min()


def std(x):
    return np.nanstd(x)
    #return x.std()


def min(x):
    return np.nanmin(x)
    #return x.min()


def var(x):
    return np.nanvar(x)
    #return x.var()


def median(x):
    return np.nanmedian(x)


def sem(x):
    return x.std()/np.sqrt(x.shape[0])
