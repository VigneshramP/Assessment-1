import argparse
import operator
def argParse():
	parser=argparse.ArgumentParser(description="descending order program")
	parser.add_argument("-p","--portfoliofile",help="Enter the path for portfoliofile and start with -p")
	parser.add_argument("-s","--stockpriceFile",help="Enter the stock Price file path and start with -s")
	args=parser.parse_args()
	return args
def readingFileContent(portfolioFilePath):
	fileContent = []
	file = open(portfolioFilePath, 'rU')
	for row in file:
		fileContent.append(row.rstrip())
	return fileContent
def stockPriceFileContent(stockPriceFilePath):
	stockPriceFileContent = open(stockPriceFilePath,"rU")
	stockPriceList = []
	for i in stockPriceFileContent:
		stockPriceFileContent = i.split(",")
	for i in stockPriceFileContent:
		stockPriceList.append(i.split("-"))
	stockPriceProfile = dict(stockPriceList)
	return stockPriceProfile
def findStockValue(priceOfStockList,stockName):
	individualStockPrice=priceOfStockList.get(stockName)
	return individualStockPrice

def StockValues(stockProfile,priceOfStockList):
	stockPrice = {}
	num=0
	for stockQuantity in stockProfile:
		if ',' in stockQuantity:
			stocks = stockQuantity.split(', ')
		else:
			stocks = [stockQuantity]		
		initialStockValue = 0
		for stock in stocks:
			stockValuePair = stock.split(' - ')
			stockName,stockCount = stockValuePair[0],stockValuePair[1]
			stockprice=findStockValue(priceOfStockList,stockName)
			initialStockValue += int(stockprice) * int(stockCount)
		stockPrice[str(num)+"="+stockQuantity] = initialStockValue 
		num = num+ 1
	print stockPrice
	return stockPrice
def descendingOrder(totalStockPrice):
	sortingValues = []
	sortingValuesInList = sorted(totalStockPrice.items(),key=operator.itemgetter(1), reverse=True)
	for items in sortingValuesInList:
		stockName, stockValue = items
		sortingValues.append(str(stockName)[str(stockName).index('=')+1:])
	return sortingValues			
def main():
	args = argParse()
	portfolioFile = readingFileContent(args.portfoliofile)
	print "<------------- STOCK LIST -------------->\n",portfolioFile
	stockPriceFile = stockPriceFileContent(args.stockpriceFile)
	print "<---------- STOCK PRICE LIST ----------->\n",stockPriceFile
	totalPriceList = StockValues(portfolioFile,stockPriceFile)
	print "<----------- SORTING STOCKS ------------>"
	for order in descendingOrder(totalPriceList):print order
if __name__ == '__main__':
	main()
