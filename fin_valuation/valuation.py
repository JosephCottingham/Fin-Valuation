
def cash_to_marketcap(self, ticker):
    '''
    Cash/MarketCap
    '''
    balance_sheet_response = self.fmp.company_valuation.quarterly_balance_sheet_statement(ticker=ticker, limit=1)
    marketcap_reponse = self.fmp.company_valuation.market_capitalization(ticker=ticker, limit=1)
    if len(balance_sheet_response) > 0 and len(marketcap_reponse) > 0:
        return balance_sheet_response[0]['cashAndCashEquivalents']/marketcap_reponse[0]['marketCap']

def iv_to_stock_price(self, ticker):
    '''
    IV/Stock Price
    '''
    dcf_response = self.fmp.company_valuation.discounted_cash_flow(ticker=ticker, limit=1)
    stock_price_response = self.fmp.company_valuation.discounted_cash_flow(ticker=ticker, limit=1)
    if len(dcf_response) > 0 and len(stock_price_response) > 0:
        return dcf_response[0]['dcf']/stock_price_response['Stock Price']

#For Financial/Real Estate Companies Only -- ( Use P/E * EPS for IT, Communications, Consumers, and Healthcare -- Use Equity Value/Shares Outstanding for Industrials, Materials, Energy, and Utilities) 
def price_to_book_times_BVPS(self, ticker):
    '''
    P/Bk * BVPS
    '''
    price_to_book_response = self.fmp.company_valuation.ratios-ttm(ticker=ticker, limit=1)
    BVPS_response = self.fmp.company_valuation.key-metrics-ttm(ticker=ticker, limit=1)
    if len(price_to_book_response) > 0 and len(BVPS_response) > 0:
        return price_to_book_response[0]['priceToBookRatioTTM']*BVPS_response[0]['bookValuePerShareTTM']

