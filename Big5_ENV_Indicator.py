""" Created by Cyou """
# 04/15/2022
# -*-encoding:utf-8-*-

import pandas as pd
from prettytable import PrettyTable

# Specify the Column Names while initializing the Table
myTable = PrettyTable(["Ordinals", "Big5-ENV Indicator"])


env_keyword = ["sidewalk", "floodway", "rice field", "flame", "fire", "warehouse", "air filter", "planted forest", "energy", "smoke"]
big5_indicator = ["Gregariousness", "Assertiveness", "Activity", "Excitement - seeking", "Positive emotions", "Warmth", "Trust",
                  "Straightforwardness", "Altruism", "Compliance", "Modesty", "Tender - mindedness", "Competence", "Order",
                  "Dutifulness", "Achievement striving", "Self - discipline", "Deliberation", "Anxiety", "Angry hostility",
                  "Depression", "Self - consciousness", "Impulsiveness", "Vulnerability", "Ideas", "Fantasy", "Aesthetics", "Actions",
                  "Feelings", "Values"]

big5_env_indicator = []
def get_indicator():
	for key in env_keyword:
			for big in big5_indicator:
				indicator = key.capitalize() + " " + big 
				big5_env_indicator.append(indicator)

def view_indicator():
	for i, indicator in enumerate(big5_env_indicator):	
		# print(indicator)
		myTable.add_row([i+1, indicator])
	print(myTable)

if __name__ == '__main__':
	get_indicator()
	view_indicator()