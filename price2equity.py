import pandas as pd 
import os
import time 
from datetime import datetime 


path = './Data/intraQuarter/'

def Key_Stats(gather = "Total Debt/Equity (mrq)"):
	statspath = path + '_KeyStats'
	stock_list = [x[0] for x in os.walk(statspath)]
	print(stock_list)

Key_Stats()
