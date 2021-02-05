from financialmodelingprep import financialmodelingprep


class fin_valuation():

    fmp = None

    def __init__(self):
        self.fmp = financialmodelingprep('aca3ba578e4bd100a2f057d384972cf6')

    def cash_to_marketcap(self, ticker):
        '''
        Cash/MarketCap
        '''
        balance_sheet_response = self.fmp.company_valuation.quarterly_balance_sheet_statement(
            ticker=ticker, limit=1)
        marketcap_response = self.fmp.company_valuation.market_capitalization(
            ticker=ticker, limit=1)
        print(balance_sheet_response, marketcap_response)
        if len(balance_sheet_response) > 0 and len(marketcap_response) > 0:
            return balance_sheet_response[0]['cashAndCashEquivalents'] / marketcap_response[0]['marketCap']

    def iv_to_stock_price(self, ticker):
        '''
        IV/Stock Price
        '''
        dcf_response = self.fmp.company_valuation.discounted_cash_flow(
            ticker=ticker, limit=1)
        stock_price_response = self.fmp.company_valuation.discounted_cash_flow(
            ticker=ticker, limit=1)
        if len(dcf_response) > 0 and len(stock_price_response) > 0:
            return dcf_response[0]['dcf'] / stock_price_response[0]['Stock Price']

    # For Financial/Real Estate Companies Only. Otherwise, comment out.
    def price_to_book_times_BVPS(self, ticker):
        '''
        P/Bk * BVPS
        '''
        price_to_book_response = self.fmp.company_valuation.ratios - \
            ttm(ticker=ticker, limit=1)
        BVPS_response = self.fmp.company_valuation.key - \
            metrics - ttm(ticker=ticker, limit=1)
        if len(price_to_book_response) > 0 and len(BVPS_response) > 0:
            return price_to_book_response[0]['priceToBookRatioTTM'] * BVPS_response[0]['bookValuePerShareTTM']

    # For IT, Communications, Consumers, and Healthcare Companies Only. Otherwise, comment out.
    def price_to_earnings_times_eps(self, ticker):
        '''
        PE * EPS
        '''
        pe_response = self.fmp.company_valuation.ratios - \
            ttm(ticker=ticker, limit=1)
        eps_response = self.fmp.company_valuation.income-statement-as-reported(
            ticker=ticker, limit=1)
        if len(pe_response) > 0 and len(eps_response) > 0:
            return pe_response[0]['priceEarningsRatioTTM'] * eps_response[0]['earningspersharebasic']

    # Use Equity Value/Shares Outstanding For Industrials, Materials, Energy, and Utilities Companies Only. Otherwise, comment out.
    def equity_value_to_SO(self, ticker):
        '''
        Equity Value / SO -- (Equity Value = Enterprise Value - Total Debt)
        '''
        enterprise_value_response = self.fmp.company_valuation.enterprise-values - \
            ttm(ticker=ticker, limit=1)
        total_debt_response = self.fmp.company_valuation.balance-sheet-statement(
            ticker=ticker, limit=1)
        shares_outstanding_response = self.fmp.company_valuation.income-statement-as-reported(
            ticker=ticker, limit=1)
        if len(enterprise_value_response) > 0 and len(total_debt_response) > 0 and len(shares_outstanding_response) > 0:
            return [enterprise_value_response[0]['enterpriseValue'] - total_debt_response[0]['totalDebt']] / shares_outstanding_response[0]['weightedaveragenumberofsharesoutstandingbasic']

    def beta(self, ticker):
        '''
        Beta Check
        '''
        beta_response = self.fmp.company_valuation.cash-flow-statement{betaMoreThan} - \
            ttm(ticker=ticker, limit=1)
        if len(beta_response) > 0.7:
            return beta_response[0]['beta']

    def revenue_growth(self, ticker):
        '''
        3 Year Revenue Growth/Share
        '''
        revenue_growth_response = self.fmp.company_valuation.financial-growth - \
            ttm(ticker=ticker, limit=1)
        if len(revenue_growth_response) > 0.3:
            return revenue_growth_response[0]['threeYRevenueGrowthPerShare']