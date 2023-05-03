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
        self.portfolio.append(name)

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
                (pow(self.security_Obj.variance/100, 0.5))*100) + "%"
        except:
            return "This is an invalid date"

    def get_portfolio(self):
        return self.portfolio

    def get_portfolio_covariance(self, security1, security2, firstDate, secondDate):
        security1.get_security_mean(firstDate, secondDate)
        security1.get_security_variance(firstDate, secondDate)
        mean1 = self.security_Obj.mean
        variance1 = self.security_Obj.variance

        security2.get_security_mean(firstDate, secondDate)
        security2.get_security_variance(firstDate, secondDate)
        mean2 = self.security_Obj.mean
        variance2 = self.security_Obj.variance
        cov = 0

        for i in range(len(security1.security_list)):
            cov1 = (security1.security_list[i]) - mean1
            cov2 = (security2.security_list[i]) - mean2
            cov += cov1 * cov2
        cov /= (len(security1.security_list) - 1)
        return cov, variance1, variance2

    def get_portfolio_variance(self, security1, weight1, security2, weight2, firstDate, secondDate):
        try:
            covariance_list = self.get_portfolio_covariance(security1, security2, firstDate, secondDate)
            covariance = covariance_list[0]
            variance1 = covariance_list[1]
            variance2 = covariance_list[2]
            portfolio_variance = (weight1 ** 2) * variance1 + (
                        weight2 ** 2) * variance2 + 2 * weight1 * weight2 * covariance
            portfolio_std = pow(portfolio_variance / 100, 1 / 2) * 100
            return f"The resulting portfolio variance is {portfolio_variance}% and the standard deviation of the portfolio is {portfolio_std}% and" \
                   f" the covariance of the pair is {covariance}"
        except:
            return "There was an error in the parameters. Please ensure that the dates line up"


if __name__ == "__main__":
    Amazon = Security("AMZN")
    print(Amazon.get_trailing_eps())
    print(Amazon.get_beta())
    print(Amazon.get_security_mean((2022, 4, 30), (2023, 4, 30)))
    print(Amazon.get_security_variance((2022, 4, 30), (2023, 4, 30)))
    print(Amazon.get_std((2022, 4, 30), (2023, 4, 30)))
    print(Amazon.get_portfolio())
    Roblox = Security("RBLX")
    print(Roblox.get_portfolio())
    print(Roblox.get_trailing_eps())
    print(Roblox.get_beta())
    print(Roblox.get_security_mean((2022, 4, 30), (2023, 4, 30)))
    print(Roblox.get_security_variance((2022, 4, 30), (2023, 5, 30)))
    print(Roblox.get_std((2022, 4, 30), (2023, 4, 30)))
    print(Roblox.get_portfolio())
    print(Roblox.get_portfolio_variance(Amazon, 0.5, Roblox, 0.5, (2022, 4, 30), (2023, 4, 30)))
