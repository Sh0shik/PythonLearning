import pprint
import datetime
import locale

diary = {'понедельник': {
 'утро': ['погулять с собакой'],
 'день': [],
'вечер': ['погулять с собакой']
 },
 'вторник': {
 'утро': ['погулять с собакой'],
 'день': [],
'вечер': ['погулять с собакой']
 },
 'среда': {
 'утро': ['погулять с собакой'],
 'день': [],
'вечер': ['погулять с собакой']
 },
 'четверг': {
 'утро': ['погулять с собакой'],
 'день': [],
'вечер': ['погулять с собакой']
 },
 'пятница': {
 'утро': ['заехать в шиномонтаж', 'помыть машину'],
 'день': [],
'вечер': ['поход в театр', 'ужин в кафе']
 },
 'суббота': {
 'утро': [],
'день': [],
'вечер': []
 },
 'воскресенье': {
 'утро': [],
'день': [],
'вечер': []
 }}

diary[('суббота', 'воскресенье')] = {'посадить цыеты на даче'}
del diary['суббота']
del diary['воскресенье']

diary['вторник']['утро'].append('поход к зубному')

indexTeatr = diary['пятница']['вечер'].index('поход в театр')
diary['пятница']['вечер'].remove('поход в театр')
diary['пятница']['вечер'].insert(indexTeatr, 'поход в кино')

for dayTime in diary['четверг']:
    if 'погулять с собакой' in diary['четверг'][dayTime]:
        diary['четверг'][dayTime].remove('погулять с собакой')

if len(diary['пятница']['утро']) > 1:
    print(diary['пятница']['утро'][1])

del diary['понедельник']
#Выйдет ошибка KeyError: 'понедельник'

# Day = input('Введите день недели: ')
# if Day in diary:
#     if len(diary[Day]) > 0:
#         pprint.pprint(diary[Day])
#     else:
#         pprint.pprint('Свободный день')
# else:
#     print('Такого дня недели нет в расписании')

days_rus = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
day_name = days_rus[datetime.datetime.now().weekday()]
day_name = 'вторник'
if day_name in diary:
    for dayTime, tasks in diary[day_name].items():
        print(dayTime + ': ' + ', '.join(tasks))

def resetShaduale():
    for day in diary:
        diary[day] = {'утро': [], 'день': [], 'вечер': []}
resetShaduale()
pprint.pprint(diary)    

def addTaskInShaduale(day, dayTime, task):
    if day in diary:
        if dayTime in diary[day]:
            diary[day][dayTime].append(task)
        else:
            print('Такого времени суток нет в расписании')
    else:
        print('Такого дня недели нет в расписании')

day = input('Введите день недели: ')
dayTime = input('Введите время суток (утро, день, вечер): ')
task = input('Введите задачу: ')
addTaskInShaduale(day, dayTime, task)
pprint.pprint(diary)