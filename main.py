from Calculations import Calculations
from Portfolio import Portfolio
from Security import Security

#TODO implement kurtosis and skewness in the plotting

if __name__ == "__main__":
    Amazon = Security("AMZN")
    print(Amazon.get_trailing_eps())
    print(Amazon.get_beta())
    print(Amazon.get_security_mean((2022, 4, 30), (2023, 4, 30)))
    print(Amazon.get_security_variance((2022, 4, 30), (2023, 4, 30)))
    print(Amazon.get_std((2022, 4, 30), (2023, 4, 30)))

    portfolio = Portfolio()
    print(portfolio.get_portfolio())
    #TODO use numbers of shares as input
    weight_dict = Calculations.calculate_weighting({"BIGG.CN": 89.78, "DWAC":155.07, "EMAN" : 200.6, "GBML.V": 61.69, "INTC" : 248.6, "LCID": 139.23, "LITH.V": 51.10, "LUN.TO":501.49, "PBL.TO" :243.55, "PYPL.NE":154.71, "RBLX": 350.40, "SNDL" : 8.65, "USM" : 103.44})
    weight_dict = portfolio.addWeightedSecurity(weight_dict)
    print(portfolio.get_portfolio())
    print(portfolio.get_portfolio_variance(weight_dict, (2018, 4, 30), (2023, 4, 30)))
    print(portfolio.get_portfolio_mean(weight_dict, (2018, 4, 30), (2023, 4, 30)))
    portfolio.plot_portfolio()

