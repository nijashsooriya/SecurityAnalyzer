import yfinance
import datetime

class Security:

    def __init__(self):
        self.security = None

    def get_security_dict(self, name):
        self.security = yfinance.Ticker(name)
        return self.security.info

    def get_trailing_eps(self):
        return self.security.info['trailingEps']

    def get_beta(self):
        try:
            return self.security.info['beta']
        except:
            return "There is no data on the beta value"

    def get_security_values(self, firstDate, secondDate):
        try:
            startDate = datetime.datetime(firstDate[0], firstDate[1], firstDate[2])
            endDate = datetime.datetime(secondDate[0], secondDate[1], secondDate[2])
            return self.security.history(start = startDate, end = endDate)["Open"].tolist()
        except:
            return "This is an invalid date"

if __name__ == "__main__":
    Amazon = Security()
    print(Amazon.get_security_dict("AMZN"))
    print(Amazon.get_trailing_eps())
    print(Amazon.get_beta())
    print(Amazon.get_security_values((2022,4,30), (2023, 4, 30)))