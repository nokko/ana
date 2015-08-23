import pandas as pd 
import os
import time 
from datetime import datetime 


path = os.path.join(os.getcwd(), "/Data/intraQuarter/")

def Key_Stats(gather = "Total Debt/Equity (mrq)"):
	statspath = os.path.join('_KeyStats')
	stock_list = [x[0] for x in os.walk(statspath)]
	print(stock_list)

Key_Stats()
