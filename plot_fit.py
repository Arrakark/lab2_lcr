##################################
####        Load Data         ####
##################################

from numpy import genfromtxt

data = genfromtxt('freq_sweep.csv', delimiter=',', skip_header=1)
freq = data[:,0]
magnitude = data[:,1]
phase = data[:,2]

##################################
####        Curve Fit         ####
##################################