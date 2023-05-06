###########################################################################################
# This file was made by Nijash Sooriya and is not intended for replication
###########################################################################################
import yfinance
import datetime
from Calculations import Calculations
from Security import Security


class Portfolio():
    security_Obj = Calculations()
    def __init__(self):
        self.portfolio = list()
        self.weighted_portfolio = dict()
        self.portfolio_variance = 0
        self.portfolio_mean = 0
        self.portfolio_std = 0

    def addSecurity(self, array):
        for i in range(len(array)):
            newSecurity = Security(array[i])
            self.portfolio.append(newSecurity)
    def addWeightedSecurity(self, weighted_securities):
        #name, weighting
        #Wipe old portfolio
        self.portfolio = list()
        self.weighted_portfolio = weighted_securities
        weight_dict = list()
        for key in weighted_securities:
            newSecurity = Security(key)
            self.portfolio.append(newSecurity)
            weight_dict.append(weighted_securities[key])
        return weight_dict


    def get_portfolio(self):
        return_array = list()
        for i in range(len(self.portfolio)):
            return_array.append(self.portfolio[i].get_name())
        return return_array


    #Rewrite this to take pair
    def get_portfolio_covariance(self, security1, security2, firstDate, secondDate):

            security1 = Security(security1)
            security2 =  Security(security2)
            security1.get_security_mean(firstDate, secondDate)
            security1.get_security_variance(firstDate, secondDate)
            mean1 = Security.security_Obj.mean
            variance1 = Security.security_Obj.variance

            security2.get_security_mean(firstDate, secondDate)
            security2.get_security_variance(firstDate, secondDate)
            mean2 = Security.security_Obj.mean
            variance2 = Security.security_Obj.variance
            cov = 0
            while (len(security1.security_list) > len(security2.security_list)):
                security1.security_list.pop()
            while (len(security2.security_list) > len(security1.security_list)):
                security2.security_list.pop()

            for i in range(len(security1.security_list)):
                cov1 = (security1.security_list[i]/100) - mean1/100
                cov2 = (security2.security_list[i]/100) - mean2/100
                cov += cov1 * cov2
            cov /= (len(security1.security_list) - 1)
            return cov, variance1, variance2

    def get_portfolio_variance(self, weight_dict, firstDate, secondDate):
            variance_dict = dict()
            weight_variance_prod = 0
            for i in range(len(self.portfolio)):
                self.portfolio[i].get_security_variance(firstDate, secondDate)
                variance = Security.security_Obj.variance
                variance_dict[self.portfolio[i].get_name()] = variance
            counter = 0
            for key in variance_dict:
                weight_variance_prod += (variance_dict[key]/100)*(weight_dict[counter]**2)
                counter += 1
            names = self.get_portfolio()
            unique_combos =  Calculations.combinations(names)
            covariance = 0
            progress = 1
            for set_id in unique_combos:
                print(f"Progress: {int((progress/len(unique_combos))*100)}% ")
                covariance += 2*self.weighted_portfolio[set_id[0]]*self.weighted_portfolio[set_id[1]]*self.get_portfolio_covariance(set_id[0], set_id[1], firstDate, secondDate)[0]
                progress +=1
            portfolio_variance = covariance + weight_variance_prod
            self.portfolio_variance = portfolio_variance
            portfolio_std = pow(portfolio_variance, 1/2)
            self.portfolio_std = portfolio_std
            return f"The portfolio's variance on daily return from {firstDate} to {secondDate} is {portfolio_variance*100}% " \
                   f"and it's standard deviation is {portfolio_std*100}% ."


    def get_portfolio_mean(self, weight_dict, firstDate, secondDate):
        try:
            mean_dict = dict()
            for i in range(len(self.portfolio)):
                self.portfolio[i].get_security_mean(firstDate, secondDate)
                mean =  Security.security_Obj.mean
                mean_dict[self.portfolio[i].get_name()] = mean
            mean_weight_prod = 0
            counter = 0
            for key in mean_dict:
                mean_weight_prod += (mean_dict[key]/100)*weight_dict[counter]
                counter += 1
            self.portfolio_mean = mean_weight_prod
            return f"The mean daily return on the portfolio from {firstDate} to {secondDate} is {mean_weight_prod*100}% ."
        except:
            return "Please recheck the parameters for formatting issues."
    def plot_portfolio(self):
        self.security_Obj.plot_gaussian("Portfolio", self.portfolio_mean, self.portfolio_std)

