# -*- coding: utf-8 -*-
#!/usr/bin/python

'''Action Neededd : 1) Please change the filepath as needed (Search for "open" and change the path 2) Please note that this program has been written on a Windows machine'''

'''Assumptions - 1) The file is saved in a .csv file format. 
If the file is saved in .txt format, even then we can get the values since the columns are tab delimited.
2) The corporate actions are limited to the 5 options - stock dividend, cash dividend, stock split, name change and symboange 
3) Currencies are limited to USD, GBP and CAD - for parsing purposes'''



import csv
import re

#Stock Split Function
def stk_splt(s, shares, total_value):
	#blank list
	num = []
	#considering a use case that the split can also be fractional.
	temp_line = s.split()
	num = [s for s in temp_line if s.isdigit()]
	#Formula: Shares = (Number before 'for' in corporate actions * Current no. of shares)/ Number after 'for' in corporate actions
	fin_shares = (float(num[0]) * int(shares))/float(num[1])
	#Change in price captured
	price = float(total_value)/fin_shares
	return price,fin_shares

	
#Stock Dividend Function	
def stk_div(s, shares, total_value):
	temp_line = s.split()
	#getting the value from 'action'
	action_val = re.findall("\d+.\d+", s)
	#yet to verify the rounding error to be considered in this scenario. For now, I'm assuming it is same as the integer rounding of python.
	#Formula for dividend: The value from Corporate action * no. of shares, formula for final no. of shares = Dividend + no. of Shares
	fin_shares = int(float(action_val[0]) * int(shares) + int(shares))
	#Change in price captured
	price = float(total_value)/fin_shares
	
	return price, fin_shares

	
#Reading the Portfolio
l_count = 0
def portfolio_read():
	curline=[]
	portfolio_read = csv.reader(open('\\file1.csv','rb'))
	for idx, l in enumerate(portfolio_read):
		if (symbol == l[0].strip()):
			curline = l	
			l_count = idx
	return curline, l_count

	
#Analysis of the Corporate Actions
def analysis():
	#Reading the Portfolio
	cur_line, l_count = portfolio_read()
	#if the line is not a null/blank line
	if cur_line:
		#if the Corporate action is 'Stock Dividend'
		if 'STOCK DIVIDEND' in action.upper():
			#Consider the current line from the portfolio
			fin_line = list(cur_line)
			#replace the comma in the shares
			cur_line[6] = cur_line[6].replace(",","")	
			#Call the stock dividend function to get the changed value in financial shares and price
			price, fin_shares = stk_div(action, cur_line[3], cur_line[6])
			fin_line[3] = fin_shares
			fin_line[4] = price
			#get the position of the value in the line of the portfolio
			pos = 3
			#get the line of the portfolio
			counts = l_count
		#if the Corporate action is 'Stock Split'
		if 'STOCK SPLIT' in action.upper():
			#Consider the current line from the portfolio
			fin_line = list(cur_line)
			#replace the comma in the shares
			cur_line[6] = cur_line[6].replace(",","")	
			#Call the stock split function to get the changed value in financial shares and price
			price, fin_shares = stk_splt(action, cur_line[3], cur_line[6])
			fin_line[3] = fin_shares
			fin_line[4] = price
			#get the position of the value in the line of the portfolio
			pos = 3
			#get the line of the portfolio
			counts = l_count
		if 'NAME CHANGE' in action.upper():
			#Consider the current line from the portfolio
			fin_line = list(cur_line)
			#Get the description value
			desc = action.strip().split()[-1].strip('\"')
			fin_line[1] = desc
			pos = 1
			counts = l_count
		if 'SYMBOL CHANGE' in action.upper():
			#Consider the current line from the portfolio
			fin_line = list(cur_line)
			#Get the symbol value
			sym = action.strip().split()[-1]
			fin_line[0] = sym
			#get the position of the value in the line of the portfolio
			pos = 0
			#get the line of the portfolio
			counts = l_count
		#As of now it does nothing but just copies the line as is ,but giving this option in case things change in future for future tables/columns
		if'CASH DIVIDEND' in action.upper():
			fin_line = list(cur_line)
			#get the line of the portfolio
			counts = l_count
			#get the position of the value in the line of the portfolio
			pos = 100
		return fin_line, counts, pos

		
#Function to print the portfolio lines		
def portfolio_print():
	for i in range(len(lines)):
		print lines[i]
	print '\n'

	
#Reading the Portfolio
r = csv.reader(open('\\file1.csv', 'rb'))
#saving it in a different lisst
lines = [l for l in r]
#printing it for the first time
portfolio_print()

''' The below lines can be made into a function but leaving it as is because it's simple to understand like this and doesn't affect performance in a big way'''

#reading the Corporate Actions file
reader = csv.reader(open('\\file2.csv','rb'))
#iterating through Corporate Actions file
for row in reader:
	#On finding the right weekday
	if 'Monday' in row[0].strip():
		#Get the symbol
		symbol = row[1]
		#Get the action
		action = row[2]
		#Get the analysis done to understand how the corporate action is impacting the portfolio
		final_line,counts,pos = analysis()
		#Depending on the analysis, the impact on portfolio and the position - change the portfolio lines
		if pos == 3:
			lines[counts][3] = final_line[3]
			lines[counts][4] = final_line[4]
		if pos == 1:
			lines[counts][1] = final_line[1]
		if pos == 0:
			lines[counts][0] = final_line[0]
print "After Monday:\n"
portfolio_print()

#reading the Corporate Actions file
reader = csv.reader(open('\\file2.csv','rb'))
#iterating through Corporate Actions file
for row in reader:
	#On finding the right weekday
	if 'Tuesday' in row[0].strip():
		#Get the symbol
		symbol = row[1]
		#Get the action
		action = row[2]
		#Get the analysis done to understand how the corporate action is impacting the portfolio
		final_line,counts,pos = analysis()
		#Depending on the analysis, the impact on portfolio and the position - change the portfolio lines
		if pos == 3:
			lines[counts][3] = final_line[3]
			lines[counts][4] = final_line[4]
		if pos == 1:
			lines[counts][1] = final_line[1]
		if pos == 0:
			lines[counts][0] = final_line[0]
print "After Tuesday:\n"
portfolio_print()

#reading the Corporate Actions file
reader = csv.reader(open('\\file2.csv','rb'))
#iterating through Corporate Actions file
for row in reader:
	#On finding the right weekday
	if 'Wednesday' in row[0].strip():
		#Get the symbol
		symbol = row[1]
		#Get the action
		action = row[2]
		#Get the analysis done to understand how the corporate action is impacting the portfolio
		final_line,counts,pos = analysis()
		#Depending on the analysis, the impact on portfolio and the position - change the portfolio lines
		if pos == 3:
			lines[counts][3] = final_line[3]
			lines[counts][4] = final_line[4]
		if pos == 1:
			lines[counts][1] = final_line[1]
		if pos == 0:
			lines[counts][0] = final_line[0]
print "After Wednesday:\n"
portfolio_print()

#reading the Corporate Actions file
reader = csv.reader(open('\\file2.csv','rb'))
#iterating through Corporate Actions file
for row in reader:
	#On finding the right weekday
	if 'Thursday' in row[0].strip():
		#Get the symbol
		symbol = row[1]
		#Get the action
		action = row[2]
		#Get the analysis done to understand how the corporate action is impacting the portfolio
		final_line,counts,pos = analysis()
		#Depending on the analysis, the impact on portfolio and the position - change the portfolio lines
		if pos == 3:
			lines[counts][3] = final_line[3]
			lines[counts][4] = final_line[4]
		if pos == 1:
			lines[counts][1] = final_line[1]
		if pos == 0:
			lines[counts][0] = final_line[0]
print "After Thursday:\n"
portfolio_print()

#reading the Corporate Actions file
reader = csv.reader(open('\\file2.csv','rb'))
#iterating through Corporate Actions file
for row in reader:
	#On finding the right weekday
	if 'Friday' in row[0].strip():
		#Get the symbol
		symbol = row[1]
		#Get the action
		action = row[2]
		#Get the analysis done to understand how the corporate action is impacting the portfolio
		final_line,counts,pos = analysis()
		#Depending on the analysis, the impact on portfolio and the position - change the portfolio lines
		if pos == 3:
			lines[counts][3] = final_line[3]
			lines[counts][4] = final_line[4]
		if pos == 1:
			lines[counts][1] = final_line[1]
		if pos == 0:
			lines[counts][0] = final_line[0]
print "After Friday:\n"
portfolio_print()





