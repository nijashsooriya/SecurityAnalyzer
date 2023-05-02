import yfinance
import datetime
from Calculations import Calculations

class Security:

    security_Obj = Calculations()
    def __init__(self):

        self.security = None
        self.security_list = None

    def get_security_dict(self, name):
        self.security = yfinance.Ticker(name)
        return self.security.info

    def get_trailing_eps(self):
        return "The trailing EPS is: " + str(self.security.info['trailingEps'])

    def get_beta(self):
        try:
            return "The beta value is: " + str(self.security.info['beta'])
        except:
            return "There is no data on the beta value"

    def get_security_mean(self, firstDate, secondDate):
        try:
            startDate = datetime.datetime(firstDate[0], firstDate[1], firstDate[2])
            endDate = datetime.datetime(secondDate[0], secondDate[1], secondDate[2])
            self.security_list = self.security.history(start = startDate, end = endDate)["Open"].tolist()
            self.security_Obj.mean_operator(self.security_list)
            return f'The mean of this security from {firstDate} to {secondDate} is: ' + str(self.security_Obj.mean)
        except:
            return "This is an invalid date"

    def get_security_variance(self, firstDate, secondDate):
        try:
            startDate = datetime.datetime(firstDate[0], firstDate[1], firstDate[2])
            endDate = datetime.datetime(secondDate[0], secondDate[1], secondDate[2])
            self.security_list = self.security.history(start = startDate, end = endDate)["Open"].tolist()
            self.security_Obj.variance_operator(self.security_list, self.security_Obj.mean_operator(self.security_list))
            return f'The variance of this security from {firstDate} to {secondDate} is: ' + str(self.security_Obj.variance)
        except:
            return "This is an invalid date"

    def get_std(self, firstDate, secondDate):
        try:
            self.get_security_variance(firstDate, secondDate)
            return f'The standard deviation of this security from {firstDate} to {secondDate} is: ' + str(self.security_Obj.variance**.5)
        except:
            return "This is an invalid date"


if __name__ == "__main__":
    Amazon = Security()
    print(Amazon.get_security_dict("LITH.V"))
    print(Amazon.get_trailing_eps())
    print(Amazon.get_beta())
    print(Amazon.get_security_mean((2022, 4, 30), (2023, 4, 30)))
    print(Amazon.get_security_variance((2022, 4, 30), (2023, 4, 30)))
    print(Amazon.get_std((2022, 4, 30), (2023, 4, 30)))