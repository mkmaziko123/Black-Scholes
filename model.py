import math
import random
from statistics import NormalDist
import pandas as pd
StockPrice = 20
ExercisePrice = 40
RiskFreeInterest = 0.5
ExpirationTime = 5
Volatility = 2
N = NormalDist(0,1)
def europeanmodel(StockPrice,ExercisePrice,RiskFreeInterest,ExpirationTime,Volatility):
    optiontype = str(input("call or put"))
    if optiontype == "call":
        d1_ = (RiskFreeInterest+ ((Volatility**2)/2)) * ExpirationTime
        d2_ = (RiskFreeInterest - ((Volatility**2)/2)) * ExpirationTime
        d1 = (math.log(StockPrice/ExercisePrice) + d1_  ) / (Volatility*math.sqrt(ExpirationTime))
        d2 = (math.log(StockPrice/ExercisePrice) + d2_  ) / (Volatility*math.sqrt(ExpirationTime))


        CallPrice = StockPrice*N.cdf(d1) - ExercisePrice*math.exp(-RiskFreeInterest*ExpirationTime)*N.cdf(d2)
        return CallPrice
    
def montecarloption(StockPrice,NumTrials):
    results = []
    for i in range(NumTrials):
        Z = N.inv_cdf(random.random())
        TerminalStockPrice = StockPrice * math.exp(RiskFreeInterest-0.5*math.pow(Volatility,2)*ExpirationTime + Volatility*math.sqrt(ExpirationTime))
        PayoffMaturity = max(TerminalStockPrice-ExercisePrice,0)
        Price = PayoffMaturity*math.exp(-RiskFreeInterest*ExpirationTime)

        results.append({
            "Trial": i,
            "Z": Z,
            "S_T": TerminalStockPrice,
            "Payoff": PayoffMaturity,
            "DiscountedPayoff": Price
        })

        df = pd.DataFrame(results)
        return d