#class_test.py

from consumer_price_index.calculator_class import Reference_Year

amount = int(input("Please choose a number (e.g. 10540) "))
baseline_year = int(input("[Baseline] Choose a year between 1992 and 2019 "))
reference_year = int(input("[Reference] Choose a year between 1992 and 2019 "))

baseline_year_instance = Year(baseline_year)
reference_year_instance = Reference_Year(reference_year, amount)
dollars = reference_year_instance.get_dollars(baseline_year_instance)
print(dollars)
