
class Calculations:

    def __init__(self):
        self.mean = 0
        self.variance = 0

    def mean_operator(self, array):
        self.mean  = sum(array)/len(array)
        return self.mean

    def variance_operator(self, array, mean):
        summation = 0
        for i in range(len(array)):
            summation += (array[i] - mean)**2
        self.variance = summation/len(array)
        return self.variance