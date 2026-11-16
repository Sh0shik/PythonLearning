import pickle
import shelve
import pprint
from datetime import datetime

class Article:
    def __init__(self, title, category, date):
        self.title = title
        self.category = category
        self.date = date
    def info(self):
        print(f'У СФУ вышла новая статья \"{self.title}\" по теме {self.category} от {self.date}')
    def __repr__(self):
        return f"({self.title!r}, {self.category!r}, {self.date!r})"
    
def filterArticle(articles, category):
        for art in articles:
            if art.category == category:
                art.info()

art1 = Article("Пришли новые учебники", "Новости", "01.01.2026")
art2 = Article("Новые ПК", "Техника", "02.02.2027")
art3 = Article("Вычислительная техника самая крутая", "Правда", "03.03.1900")
art4 = Article("Человек паук в городе", "Удача", "09.09.2029")
art5 = Article("Кто такой Питер Паркер", "Вопрос", "10.12.2100")
lst = [art1, art2, art3, art4, art5]

print("До выгрузки в бинарный файл")
for a in lst:
    a.info()

with open("articles.dat", "wb") as File:
    pickle.dump(lst, File)

with open("articles.dat", "rb") as File:
    listLoad = pickle.load(File)

print("\nПосле")
for a in listLoad:
    a.info()

print("\nСортировка по дате")
sorted_articles = sorted(listLoad, key=lambda article: list(map(int, article.date.split('.')))[::-1])
for article in sorted_articles:
    article.info()

print("\nСортировка по дате через datetime (обратная)")
sorted_articles = sorted(listLoad, key=lambda article: datetime.strptime(article.date, "%d.%m.%Y"), reverse=True)
for article in sorted_articles:
    article.info()

print("\nВывод с фильтрацией по категории")
filterArticle(sorted_articles, "Новости")

with shelve.open('articles') as shelFile:
    shelFile['Статьи'] = sorted_articles
    print("\nИзначальный")
    pprint.pprint(list(shelFile.items()))

# with shelve.open('articles') as shelFile:
#     lstTwoObject = sorted_articles[:2]
#     shelFile['Первые2'] = lstTwoObject
#     print("\nДобавление")
#     pprint.pprint(list(shelFile.items()))

with shelve.open('articles') as shelFile:

    print("\nОбновление")
    shelFile["Статьи"] = "Удалили"
    pprint.pprint(list(shelFile.items()))

    print("\nУдаление")
    del shelFile["Статьи"]
    pprint.pprint(list(shelFile.items()))
    # shelFile.clear()