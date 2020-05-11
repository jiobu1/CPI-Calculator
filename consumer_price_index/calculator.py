# calculator.py

import numpy as np 

# https://www.usinflationcalculator.com/frequently-asked-questions-faqs/#HowInflationCalculatorWorks

cpi = {1992: 140.3,
       1993: 144.5,
       1994: 148.2,
       1995: 152.4,
       1996: 156.9,
       1997: 160.5,
       1998: 163.0,
       1999: 166.6,
       2000: 172.2,
       2001: 177.1,
       2002: 179.9,
       2003: 184.0,
       2004: 188.9,
       2005: 195.3,
       2006: 201.6,
       2007: 207.3,
       2008: 215.303,
       2009: 214.537,
       2010: 218.056,
       2011: 224.939,
       2012: 229.594,
       2013: 232.957,
       2014: 236.736,
       2015: 237.017,
       2016: 240.007,
       2017: 245.120,
       2018: 251.107,
       2019: 255.657}

baseline_year = 2019
baseline_inflation = cpi[baseline_year]

amount = int(input("Please choose a number (e.g. 10540) "))
year = int(input("Choose a year between 1992 and 2018 "))


def inflation_adjustment(amount, year):
    """
    Converts dollar amounts to past values (1992-2018) or current value (2019)

    Params:
        amount and year must be inputted 
        the year pulls the consumer price index information 

    Returns:
        Converted  dollar amount
    """

    inflation_rate = cpi[year]
    output = amount * (baseline_inflation/inflation_rate)
    return (f' If you had ${amount} in {year}, you would have ${output:.2f} in 2019 dollars.')


print(inflation_adjustment(amount, year))
