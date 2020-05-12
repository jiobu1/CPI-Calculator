# calculator_class.py


class Year:
    """
    This is a Year class
    
    Params:
        This takes a year value and then looks up consumer price index for the year  

    Returns:
        It returns the inflation rate for the year selected
    """
    def __init__(self, value):
        self.year = value
        self.inflation_rate = self.get_inflation_rate()

    def get_inflation_rate(self):
        cpi_dictionary = {1992: 140.3,
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
               2019: 255.657
               }
        return cpi_dictionary[self.year]


class Conversion_Year(Year):
    """
    This is the conversion year class. This class inherits from the year class. 

    Params:
        This utilizes the year's cpi get inflation rate function and needs an dollar famount.

    Returns:
        A literal that converts dollar amounts using inflation rate.
    """
    def __init__(self, value, amount):
        super().__init__(value)
        self.amount = amount

    def get_dollars(self, year_instance):
        output = self.amount * \
            (year_instance.inflation_rate / self.inflation_rate)
        return (f' If you had ${self.amount} in {self.year}, you would have ${output:.2f} in {year_instance.year} dollars.')


amount = int(input("Please choose a number (e.g. 10540) "))
starting_year = int(input("[Start] Choose a year between 1992 and 2019 "))
conversion_year = int(input("[Conversion] Choose a year between 1992 and 2019 "))

conversion_year_instance = Year(conversion_year)
year_instance =Conversion_Year(starting_year, amount)
dollars = year_instance.get_dollars(conversion_year_instance)
print(dollars)
