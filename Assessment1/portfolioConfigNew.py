import sys
import json
import argparse

def argParse():
	parser=argparse.ArgumentParser(description="Descending Order Program")
	if len(sys.argv)>1:
		parser.add_argument("portfoliofile",help="Enter the portfoliofile Path" )
		parser.add_argument("stockpriceFile",help="Enter the Stock Price file Path ")
		parser.add_argument("-m",help="1. USD 2.EURO 3.JPY")		
	else:
		parse.print_help(sys.stdrr)
		sys.exit()
	args = parser.parse_args()
	return args

def readingFileContent(portfolioFilePath):
	fileContent = []
	try:
		file = open(portfolioFilePath, 'rU')
		for row in file:
			fileContent.append(row.rstrip())
		file.close()
	except:
		print " Enter the Correct Path for Portfoliofile"
	return fileContent	

def stockPriceFileContent(stockPriceFilePath):
	try :
		stockPriceFileContent = open(stockPriceFilePath,"rU")
		stockPriceList = []
		for i in stockPriceFileContent:
			stockPriceFileContent = i.split(",")
		for i in stockPriceFileContent:
			stockPriceList.append(i.split("-"))
		stockPriceProfile = dict(stockPriceList)
		return stockPriceProfile
	except :
		print "Enter the Correct Path for StockPricefile"

def changeInRupees(configFileContent,symbol):
	dictConversion = json.loads(configFileContent)
	if symbol is None:
		return None		
	else:
		return dictConversion.get(symbol)	

def findStockValues(stockProfile,priceOfStockList,moneyConversion):
	stockPrice = {}
	num=0
	for stockQuantity in stockProfile:
		stocks = stockQuantity.split(", ")		
		initialStockValue = 0
		for stock in stocks:
			stockValuePair = stock.split(' - ')
			stockName,stockCount = stockValuePair[0],stockValuePair[1]
			stockprice=priceOfStockList.get(stockName)
			if moneyConversion is not None :
				initialStockValue += int(stockprice) * int(stockCount) * int(moneyConversion) 
			else:
				initialStockValue += int(stockprice) * int(stockCount) 
		stockPrice[str(num)+'='+stockQuantity] = initialStockValue
		num = num+ 1
	return stockPrice

def sortingOrder(totalStockPrice):
	sortingValues = []
	valuesList = totalStockPrice.values()
	valuesListSort = valuesList.sort(reverse = True)
	changeKeyValues = dict([(value, key) for key, value in totalStockPrice.items()]) 
	sortingValuesInList =  []
	for i in valuesList:
		sortingValuesInList.append(changeKeyValues.get(i))
	for stockName in sortingValuesInList:
		sortingValues.append(str(stockName)[str(stockName).index("=")+1:])
	return sortingValues

def main():
	args = argParse()
	portfolioFile = readingFileContent(args.portfoliofile)
	print "<------------- STOCK LIST -------------->\n",portfolioFile
	
	stockPriceFile = stockPriceFileContent(args.stockpriceFile)
	print "<---------- STOCK PRICE LIST ----------->\n",stockPriceFile
	
	configFile = open('config.txt',"r")
	configFileContent = configFile.read()
	conversionValueOfMoney = changeInRupees(configFileContent,args.m)
	print "<--------- INDIAN RUPEES VALUE --------->\n",conversionValueOfMoney
	
	totalPriceList = findStockValues(portfolioFile,stockPriceFile,conversionValueOfMoney)
	print "<----------- SORTING STOCKS ------------>"
	
	for order in sortingOrder(totalPriceList): print order

if __name__ == '__main__':
	main()
