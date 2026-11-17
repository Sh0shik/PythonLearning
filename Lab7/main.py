from datetime import date, timedelta
from Currency import Rate

class Date:
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    #гетер форматированой даты 
    def __getDateLib(self):
        return date(self.__year, self.__month, self.__day)
    
    def getSpecNumberDaysDate(self, NumDays = -1):
        return self.__getDateLib() + timedelta(days=NumDays)

    @property
    def Season(self):
        if self.__month in (12, 1, 2):
            return "winter"
        elif self.__month in (3, 4, 5):
            return "spring"
        elif self.__month in (6, 7, 8):
            return "summer"
        else:
            return "autumn"
    
    #Свойсто гетера-сетера для атрибута year
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year):
        if year > 0:
            self.__year = year
        else:
            print("Uncorrrect year")

    #Свойсто гетера-сетера для атрибута month
    @property
    def month(self):
        return self.__month
    @month.setter
    def month(self, month):
        if month > 0 and month < 13:
            self.__month = month
        else:
            print("Uncorrrect month")

    #Свойсто гетера-сетера для атрибута day
    @property
    def day(self):
        return self.__day
    @day.setter
    def day(self, day):
        if day > 0 and day < 32:
            self.__day= day
        else:
            print("Uncorrrect day")

first = Date(2024, 3, 1)
second = Date(2026, 12, 31)

print('Предыдущий день:', first.getSpecNumberDaysDate())
print('Через 10 дней:', first.getSpecNumberDaysDate(10))
print('Сезон:', first.Season)
print('Следующий год:', second.getSpecNumberDaysDate(1))

first.day = 31
print('После изменения дня:', first.year, first.month, first.day)


def show(label, method, *args):
    print(label, method(*args))
    sleep(1.1)  # Пауза между запросами к сайту


rate = Rate()
show('Полная информация о USD:', Rate('full').usd)
show('Кратко о USD:', Rate('shortNote').usd)
show('Курс EUR:', rate.eur)
show('Изменение EUR:', rate.eur, True)
show('Курс AMD:', rate.exchange_rate, 'AMD')
show('1000 рублей в USD:', rate.currency_conversion, 1000, 'USD')
show('Неизвестная валюта:', rate.exchange_rate, 'XXX')
show('USD на 07.11.2026:', rate.exchange_date_rates, date(2026, 11, 7))
