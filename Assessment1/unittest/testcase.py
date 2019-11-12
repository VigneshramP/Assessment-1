import unittest
from PortfolioTracker import readingFileContent,findStockValue,descendingOrder,stockPriceFileContent
class PortfolioTrackerTest(unittest.TestCase):
    # POSITIVE TYPE TESTCASE using ASSERTEQUAL
    def testFileContent(self):
        result = readingFileContent('/home/linuxuser/Desktop/python/assessment1/Assessment-1New/portfolio.txt')
        expected = ['GOOG - 100, AMZN - 90, MS - 80','GOOG - 50, MS - 10','INFY - 100, GOOG - 50, MS - 10']
        self.assertEqual(result, expected)
    def teststockPriceFileContent(self):
        result = stockPriceFileContent('/home/linuxuser/Desktop/python/assessment1/Assessment-1New/stock_price.txt')
        expected = {'GOOG': '500', 'AMZN': '250\n', 'INFY': '300', 'MS': '200'}
        self.assertEqual(result, expected)
    def testStockValue(self):
        stockValue = findStockValue({'GOOG': '500', 'AMZN': '250', 'INFY': '300', 'MS': '200'},'MS')
        self.assertEqual(stockValue, '200')
    def testDescendingOrder(self):
        sortList = descendingOrder({'0=MS - 10, GOOG - 10':100,'1=GOOG - 50, MS - 100':200,'2=GOOG - 40, MS - 100':150})
        expected = ['GOOG - 50, MS - 100','GOOG - 40, MS - 100','MS - 10, GOOG - 10']
        self.assertEqual(sortList,expected)
    # NEGATIVE TYPE TESTCASE using ASSERTNOTEQUAL
    def test_file_content(self):
        result = readingFileContent('/home/linuxuser/Desktop/python/assessment1/Assessment-1New/portfolio.txt')
        expected = ['GOOG-100,AMZN-90,MS- 80','GOOG-50,MS-10','INFY-100,GOOG-50,MS-10']
        self.assertNotEqual(result, expected)
    def test_Stock_Value(self):
        stockValue = findStockValue({'GOOG': '500', 'AMZN': '250', 'INFY': '300', 'MS': '200'},'INFY')
        self.assertNotEqual(stockValue, '0')
    def test_DescendingOrder(self):
        sortList = descendingOrder({'0=MS - 10, GOOG - 10':100,'1=GOOG - 50, MS - 100':200,'2=GOOG - 40, MS - 100':150})
        expected = ['GOOG - 40, MS - 100','MS - 10, GOOG - 10','GOOG - 50, MS - 100']
        self.assertNotEqual(sortList,expected)
    def test_stockPrice_FileContent(self):
        result = stockPriceFileContent('/home/linuxuser/Desktop/python/assessment1/Assessment-1New/stock_price.txt')
        expected = ['GOOG: 500','AMZN: 250','INFY:300','MS: 200']
        self.assertNotEqual(result, expected)

if __name__ == '__main__':
    unittest.main()