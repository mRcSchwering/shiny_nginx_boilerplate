"""Short Description.

Detailed Description
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pandas_datareader as pdr
import datetime
import urllib2
from bs4 import BeautifulSoup



def getHistoricPrices(tickers_arr,
                      prefix="",
                      suffix="",
                      start=datetime.datetime(1990, 1, 1),
                      verbose=False):
    """Download financial data from yahoo! using ticker symbol"""
    data = {}
    for tick in tickers_arr:
        symbol = prefix + tick + suffix
        if verbose:
            print("\nDownloading %s from yahoo!..." % symbol)
        try:
            data[tick] = pdr.get_data_yahoo(symbol, start=start)
        except:
            print("%s could not be downloaded!" % symbol)
    return data


def extractText(contents):
    """Extract text from soup contents arr recursively"""
    text = []
    for cont in contents:
        try:
            newConts = cont.contents
            text.append(extractText(newConts))
        except AttributeError:
            text.append(cont.string)
    return "".join(text)


def scrapeWikiTable(url_chr, class_chr="wikitable sortable"):
    """Used for getting info about indices like DAX or so"""
    soup = BeautifulSoup(urllib2.urlopen(url_chr), "lxml")
    table = soup.find("table", class_=class_chr)
    tabRows = table.find_all("tr")

    header = []
    for cell in tabRows[0].find_all("th"):
        header.append(extractText(cell.contents))

    body = []
    for row in tabRows[1:]:
        rowText = []
        for cell in row.find_all("td"):
            rowText.append(extractText(cell.contents))
        body.append(rowText)

    return {"head": header, "body": body}



def main():
    dax = "https://en.wikipedia.org/wiki/DAX"
    return scrapeWikiTable(dax)
