import unittest
import sys
sys.path.append("../")

import finData.load

class load_finData(unittest.TestCase):

    def setUp(self):
        self.ticker = ["ADS"]
        self.url = "https://en.wikipedia.org/wiki/DAX"

    def tearDown(self):
        self.ticker = None

    def test_getHistoricalPrices(self):
        self.histPrices = finData.load.getHistoricPrices(self.ticker)

    def test_scrapeWikiTable(self):
        self.table = finData.load.scrapeWikiTable(self.url)

if __name__ == '__main__':
    unittest.main()
