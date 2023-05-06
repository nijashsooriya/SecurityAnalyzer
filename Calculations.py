###########################################################################################
#This file was made by Nijash Sooriya and is not intended for replication
###########################################################################################
import math

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from itertools import combinations

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

    def plot_gaussian(self, security_name, mean, std):
        mean *= 100
        std *= 100
        mean_string = str(mean)[:6]
        x = np.linspace(mean - 2 * std , mean + 2 * std, 100)
        plt.plot(x, stats.norm.pdf(x, mean, std))
        peak = 1/(std*pow(2*math.pi, 1/2))
        plt.text(mean, peak, f" <--- Mean: {mean_string}%",)
        plt.xlabel("Daily Return Percentage")
        plt.ylabel("Density")
        plt.title(f"Standard Normal Distribution of {security_name}'s Daily Returns")
        plt.show()
    @staticmethod
    def combinations(array):
        comb = list(combinations(array, 2))
        return comb
    @staticmethod
    def calculate_weighting(portfolio_dict):
        total = 0
        for key in portfolio_dict:
            total += portfolio_dict[key]
        weight_dict = dict()
        for key in portfolio_dict:
            weight_dict[key] = (portfolio_dict[key]/total)
        return weight_dict