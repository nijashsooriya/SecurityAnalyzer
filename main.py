from Calculations import Calculations
from Portfolio import Portfolio
from Security import Security


if __name__ == "__main__":
    Amazon = Security("AMZN")
    print(Amazon.get_trailing_eps())
    print(Amazon.get_beta())
    print(Amazon.get_security_mean((2022, 4, 30), (2023, 4, 30)))
    print(Amazon.get_security_variance((2022, 4, 30), (2023, 4, 30)))
    print(Amazon.get_std((2022, 4, 30), (2023, 4, 30)))

    portfolio = Portfolio()
    portfolio.addSecurity(["AMZN", "RBLX", "KO", "LITH.V"])
    print(portfolio.get_portfolio())
    print(portfolio.get_portfolio_variance_multi({"AMZN": 0.25, "RBLX":0.25,"KO": 0.25, "LITH.V": 0.25}, (2022, 4, 30), (2023, 4, 30)))
    Calculations.combinations(portfolio.get_portfolio())

