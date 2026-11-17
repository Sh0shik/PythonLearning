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
        return self.__getDateLib()+ timedelta(days=NumDays)

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
    def month(self, day):
        if day > 0 and day < 31:
            self.__day= day
        else:
            print("Uncorrrect day")

curr = Rate('shortNote')
print(curr.usd())