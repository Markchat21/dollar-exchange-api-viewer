import requests
import api_url
from requests.exceptions import HTTPError, ConnectionError, Timeout


class DollarExchangeAPI:
    def __init__(self, url=api_url.url, status_message=None, raw_api_data=None, clean_api_data=None, dolar_type_index=None):
        self.url = url
        self.status_message = status_message
        self.raw_api_data = raw_api_data
        self.clean_api_data = clean_api_data
        self.dolar_type_index = dolar_type_index

    # Hacemos el request a la url y manejamos las posibles excepciones
    def call(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            self.status_message = http_err
        except ConnectionError as conn_err:
            print(f'Connection error occurred: {conn_err}')
            self.status_message = conn_err
        except Timeout as timeout_err:
            print(f'Timeout error occurred: {timeout_err}')
            self.status_message = None
        except Exception as other_err:
            print(f'Other error ocurred: {other_err}')
            self.status_message = other_err
        else:
            print('Success!')
            self.status_message = None
            self.raw_api_data = response.json()
            self.clean_api_data = self.process_api_data(self.raw_api_data)

    def info_buy(self):
        # Devuelve el precio de compra del tipo de cambio deseado
        return self.clean_api_data[self.dolar_type_index]['compra']

    def info_sell(self):
        # Devuelve el precio de venta del tipo de cambio deseado
        return self.clean_api_data[self.dolar_type_index]['venta']

    def process_api_data(self, raw_data):
        clean_data = {}
        for item in raw_data:
            exchange_type_id = item['casa']
            clean_data[exchange_type_id] = item
        return clean_data


class DollarExchangeTypes(DollarExchangeAPI):
    def __init__(self):
        DollarExchangeAPI.__init__(self, url=api_url.url, status_message=None)

    def dollar_oficial(self):
        self.dolar_type_index = exchange_types['Oficial']

    def dollar_blue(self):
        self.dolar_type_index = exchange_types['Blue']
        
    def dollar_bolsa(self):
        self.dolar_type_index = exchange_types['Bolsa']

    def dollar_mayorista(self):
        self.dolar_type_index = exchange_types['Mayorista']


# Definimos los tipos de cambio disponibles
exchange_types = dict(Oficial='oficial',
                      Blue='blue',
                      Bolsa='bolsa',
                      Mayorista='mayorista'
                      )
