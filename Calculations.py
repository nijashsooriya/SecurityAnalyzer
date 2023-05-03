###########################################################################################
#This file was made by Nijash Sooriya and is not intended for replication
###########################################################################################

import matplotlib.pyplot as plt
import numpy

class Calculations:

    def __init__(self):
        self.mean = 0
        self.variance = 0

    #This returns an array of daily return percentages
    def return_operator(self, array1, array2):
        returns = list()

        for i in range(len(array1)):
            returns.append(((array2[i] - array1[i])/(array1[i]))*100)
        return returns
    def mean_operator(self, array):
        self.mean  = sum(array)/len(array)
        return self.mean
    #TODO fix the errors that result from percentage conversions
    def variance_operator(self, array, mean):
        summation = 0
        for i in range(len(array)):
            summation += (array[i] - mean)**2
        self.variance = summation/(len(array)-1)
        return self.variance

    #Plot Gaussian function


