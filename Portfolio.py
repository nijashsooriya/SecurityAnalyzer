###########################################################################################
# This file was made by Nijash Sooriya and is not intended for replication
###########################################################################################
import yfinance
import datetime
from Calculations import Calculations
from Security import Security

class Portfolio:
    def __init__(self):
        self.portfolio = list()

    def addSecurity(self, array):
        for i in range(len(array)):
            newSecurity = Security(array[i])
            self.portfolio.append(newSecurity)

    def get_portfolio(self):
        return_array = list()
        for i in range(len(self.portfolio)):
            return_array.append(self.portfolio[i].get_name())
        return return_array


    def get_portfolio_covariance(self, firstDate, secondDate):
        self.portfolio[0].get_security_mean(firstDate, secondDate)
        self.portfolio[0].get_security_variance(firstDate, secondDate)
        mean1 = Security.security_Obj.mean
        variance1 = Security.security_Obj.variance

        self.portfolio[1].get_security_mean(firstDate, secondDate)
        self.portfolio[1].get_security_variance(firstDate, secondDate)
        mean2 = Security.security_Obj.mean
        variance2 = Security.security_Obj.variance
        cov = 0

        for i in range(len(self.portfolio[1].security_list)):
            cov1 = (self.portfolio[0].security_list[i]) - mean1
            cov2 = (self.portfolio[1].security_list[i]) - mean2
            cov += cov1 * cov2
        cov /= (len(self.portfolio[0].security_list) - 1)
        return cov, variance1, variance2



    def get_portfolio_variance(self, weight1, weight2, firstDate, secondDate):
            covariance_list = self.get_portfolio_covariance(firstDate, secondDate)
            covariance = covariance_list[0]
            variance1 = covariance_list[1]
            variance2 = covariance_list[2]
            portfolio_variance = (weight1 ** 2) * variance1 + (
                        weight2 ** 2) * variance2 + 2 * weight1 * weight2 * covariance
            portfolio_std = pow(portfolio_variance / 100, 1 / 2) * 100
            return f"The resulting portfolio variance is {portfolio_variance}% and the standard deviation of the portfolio is {portfolio_std}% and" \
                   f" the covariance of the pair is {covariance}"
