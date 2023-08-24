import json
import os
import requests
import pandas as pd


"""
This is a wrapper for the fintel api.
"""


def request_data(endpoint):
    """
    This function requests data from the API.

    :param endpoint: string containing the api endpoint (eg. 'https://api.fintel.io/web/v/0.0/so/us/tsla')
    :return: response from the request.
    """

    header = {"accept": "application/json", "X-API-KEY": os.environ['FINTEL-KEY']}
    try:
        return requests.request("GET", endpoint, headers=header)
    except json.decoder.JSONDecodeError as err:
        print(err)


def get_shorts(syms: list = ['tsla', 'aapl']) -> pd.DataFrame:
    """
    This function takes a list of symbols and retrieves short data.

    :param syms: list of symbols for which to retrieve data
    :return: dataframe with ownership data for list of symbols
    """

    def clean_df(df: pd.DataFrame, ticker: str) -> pd.DataFrame:
        """

        :param df:
        :param ticker:
        :return:
        """

        df['Ticker'] = ticker
        df.columns = ['date', 'short_volume', 'volume', 'short_volume_ratio', 'ticker']
        df = df[['date', 'ticker', 'short_volume', 'volume', 'short_volume_ratio']]
        return df

    print(f'Retrieving ownership data from fintel for tickers {syms}')
    short_data = pd.DataFrame([])

    for sym in syms:
        sym = sym.upper()
        url = 'https://api.fintel.io/web/v/0.0/ss/us/%s' % sym
        response = request_data(url)

        if response.status_code == 200 and response.json()['data']:
            df = pd.DataFrame(response.json()['data'])
            df = clean_df(df, sym)
            short_data = pd.concat([short_data, df], axis=0).reset_index(drop=True)
            return short_data
        elif response.status_code == 404:
            print(f'{sym} not found.')
        else:
            print(f'No data found for {sym}.')


def get_ownership(syms: list = ['tsla', 'aapl']) -> pd.DataFrame:
    """
    This function takes a list of symbols and retrieves ownership data.

    :param syms: list of symbols for which to retrieve data
    :return: dataframe with ownership data for list of symbols
    """

    def clean_ownership_data(df: pd.DataFrame, tickers: str) -> pd.DataFrame:
        df.insert(0, 'ticker', tickers)
        df.rename(columns={'name': 'owner_name'}, inplace=True)
        return df

    print(f'Retrieving ownership data from fintel for tickers {syms}')
    ownership_data = pd.DataFrame()

    for sym in syms:
        sym = sym.upper()
        url = "https://api.fintel.io/web/v/0.0/so/us/%s" % sym
        response = request_data(url)

        if response.status_code == 200 and response.json()['owners']:
            df = pd.DataFrame(response.json()['owners'])
            df = clean_ownership_data(df, sym)
            ownership_data = pd.concat([ownership_data, df], axis=0).reset_index(drop=True)
            return ownership_data
        elif response.status_code == 404:
            print(f'{sym} not found.')
        else:
            print(f'No data found for {sym}.')


def get_all_data(syms: list = ['tsla', 'aapl']) -> pd.DataFrame:
    """
    This function takes a list of symbols and retrieves all available data from the fintel api.

    :param syms: list of symbols for which to retrieve data
    :return: dataframes for short and ownership data
    """
    print(f'Retrieving all data from fintel for tickers {syms}')

    short_data = get_shorts(syms)
    ownership_data = get_ownership(syms)

    return short_data, ownership_data
