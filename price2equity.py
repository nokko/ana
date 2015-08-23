import pandas as pd 
import os
import time 
from datetime import datetime 


path = "/Users/Nikolas/Documents/Programming/Projects/2 Much learn/ana/Data/intraQuarter/_KeyStats"

def Key_Stats(gather = "Total Debt/Equity (mrq)"):
	statspath = path
	stock_list = [x[0] for x in os.walk(path)]
	print(stock_list)

Key_Stats()
