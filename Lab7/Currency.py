import requests

class Rate:
    def __init__(self, format='value'):
        self.format = format

    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:

        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency, diff = False):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }
                Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                if diff:
                    response[currency]['Value'] = response[currency]['Value'] - response[currency]['Previous']
                return response[currency]

            if self.format == 'value':
                if diff:
                    return response[currency]['Value'] - response[currency]['Previous']
                return response[currency]['Value']
            
            if self.format ==  'shortNote':
                if diff:
                    return str(response[currency]['Name']) + ' ' + str(response[currency]['Value'] - response[currency]['Previous'])
                return str(response[currency]['Name']) + ' ' + str(response[currency]['Value']) + " руб."

        return 'Error'

    def eur(self, diff = False):
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR', diff)

    def usd(self, diff = False):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD', diff)

    def exchange_rate(self, currency, diff = False):
        """Возвращает курс валюты currency на сегодня в формате self.format"""
        return self.make_format(currency, diff)

    def exchange_date_rates(self, date, currency = 'USD', diff = False):
        """
        Возвращает курс валюты currency на дату date в формате self.format
        date - объект класса datetime.date
        """
        r = requests.get(f'https://www.cbr-xml-daily.ru/archive/{date.year}/{date.month:02d}/{date.day:02d}/daily_json.js')
        response = r.json()['Valute']

        if currency in response:
            if self.format == 'full':
                if diff:
                    response[currency]['Value'] = response[currency]['Value'] - response[currency]['Previous']
                return response[currency]

            if self.format == 'value':
                if diff:
                    return response[currency]['Value'] - response[currency]['Previous']
                return response[currency]['Value']
            
            if self.format ==  'shortNote':
                if diff:
                    return str(response[currency]['Name']) + ' ' + str(response[currency]['Value'] - response[currency]['Previous'])
                return str(response[currency]['Name']) + ' ' + str(response[currency]['Value']) + " руб."

        return 'Error'

    def currency_conversion(self, amount, currency):
        rates = self.exchange_rates()

        if currency not in rates:
            return 'Error'

        rate = rates[currency]
        return amount * rate['Nominal'] / rate['Value']
        