###########################################################################################
# This file was made by Nijash Sooriya and is not intended for replication
###########################################################################################
import yfinance
import datetime
from Calculations import Calculations
import matplotlib.pyplot as plt
import numpy


class Security:
    security_Obj = Calculations()
    # Array of securities, a portfolio
    portfolio = list()

    def __init__(self, name):
        self.security = yfinance.Ticker(name)
        self.security_list = None

    def get_name(self):
        return self.security.info["symbol"]

    def get_trailing_eps(self):
        return "The trailing EPS is: " + str(self.security.info['trailingEps'])

    def get_beta(self):
        try:
            return "The beta value is: " + str(self.security.info['beta'])
        except:
            return "There is no data on the beta value"

    def get_security_mean(self, firstDate, secondDate):

        startDate = datetime.datetime(firstDate[0], firstDate[1], firstDate[2])
        endDate = datetime.datetime(secondDate[0], secondDate[1], secondDate[2])
        self.security_list = self.security_Obj.return_operator(
            self.security.history(start=startDate, end=endDate)["Open"].tolist(),
            self.security.history(start=startDate, end=endDate)["Close"].tolist())
        self.security_Obj.mean_operator(self.security_list)
        return f'The mean daily return of this security from {firstDate} to {secondDate} was: ' + str(
            self.security_Obj.mean) + "%"

    def get_security_variance(self, firstDate, secondDate):
        try:
            startDate = datetime.datetime(firstDate[0], firstDate[1], firstDate[2])
            endDate = datetime.datetime(secondDate[0], secondDate[1], secondDate[2])
            self.security_list = self.security_Obj.return_operator(
                self.security.history(start=startDate, end=endDate)["Open"].tolist(),
                self.security.history(start=startDate, end=endDate)["Close"].tolist())
            self.security_Obj.variance_operator(self.security_list, self.security_Obj.mean_operator(self.security_list))
            return f"The variance of this security's return from {firstDate} to {secondDate} was: " + str(
                self.security_Obj.variance) + "%"
        except:
            return "This is an invalid date"

    def get_std(self, firstDate, secondDate):
        try:
            self.get_security_variance(firstDate, secondDate)
            return f"The standard deviation of this security's return from {firstDate} to {secondDate} was: " + str(
                (pow(self.security_Obj.variance / 100, 0.5)) * 100) + "%"
        except:
            return "This is an invalid date"

    def plot_security(self, firstDate, secondDate):
        self.get_security_mean(firstDate, secondDate)
        self.get_std(firstDate, secondDate)
        mean = self.security_Obj.mean
        std = pow((self.security_Obj.variance / 100), 1 / 2)
        self.security_Obj.plot_gaussian(self.security.info["symbol"], mean, std)
