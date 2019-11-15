import sys
import argparse

def argParse():
	parser=argparse.ArgumentParser(description="Sorting Program")
	parser.add_argument("-p","--stockFile",help="Enter the path for portfoliofile and start with -p")
	parser.add_argument("-s","--priceFile",help="Enter the stock Price file path and start with -s")
	args=parser.parse_args()
	return args

def getStock(stockProfile):
	fileContent = []
	try:
		file = open(stockProfile, 'rU')
		for row in file:
			fileContent.append(row.rstrip())
		return fileContent
	except IOError as err:
		print "\nEnter Correct PortFolioFile Path \n",err
		exit()
	
def getStockPrice(priceList):
	try :
		stockPriceFileContent = open(priceList,"rU")
		stockPriceList = []
		for i in stockPriceFileContent:
			stockPriceFileContent = i.split(",")
		for i in stockPriceFileContent:
			stockPriceList.append(i.split("-"))
		stockPriceProfile = dict(stockPriceList)
		return stockPriceProfile
	except IOError as err :
		print "\nEnter Correct StockPricefile Path\n",err
		exit()

def findStockValues(stockProfile,priceOfStockList):
	stockPrice = {}
	num=0
	for stockQuantity in stockProfile:
		stocks = stockQuantity.split(", ")		
		initialStockValue = 0
		for stock in stocks:
			stockValuePair = stock.split(' - ')
			stockName,stockCount = stockValuePair[0],stockValuePair[1]
			stockprice=priceOfStockList.get(stockName)
			initialStockValue += int(stockprice) * int(stockCount) 
		stockPrice[str(num)+'='+stockQuantity] = initialStockValue
		num = num + 1
	return stockPrice

def sortStockPrice(totalStockPrice):
	sortedValues = []
	valuesList = totalStockPrice.values()
	sortValues = valuesList.sort(reverse = True)
	changeKeyValues = dict([(value, key) for key, value in totalStockPrice.items()]) 
	sortValuesInList =  []
	for i in valuesList:
		sortValuesInList.append(changeKeyValues.get(i))
	for stockName in sortValuesInList:
		sortedValues.append(str(stockName)[str(stockName).index("=")+1:])
	return sortedValues

def main():
	args = argParse()
	stocks = getStock(args.stockFile)
	stockPrice = getStockPrice(args.priceFile)
	totalPriceList = findStockValues(stocks,stockPrice)
	print "\n<------------- STOCK LIST -------------->\n",stocks
	print "\n<---------- STOCK PRICE LIST ----------->\n",stockPrice
	print "\n<----------- SORTING STOCKS ------------>"
	for order in sortStockPrice(totalPriceList): print order
	
if __name__ == '__main__':
	main()