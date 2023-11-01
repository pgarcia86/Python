##  Dates

import datetime

now = datetime.datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)

today = datetime.datetime(2023, 10, 31)                 ##  Crea un objeto del tipo Datetime con los parametros AAAA, MM, DD
print(today)

today_hour = datetime.time(23, 10, 14)                  ##  Crea un objeto del tipo Time con los parametros HH, MM, SS

print(today_hour.hour)
print(today_hour.minute)
print(today_hour.second)


current_date = datetime.date.today()                    ##  Crea un objeto del tipo Date con la fecha de hoy
print(current_date)
print(current_date.day)
print(current_date.month)
print(current_date.year)


##  Puedo hacer operaciones dentro de los parametros que paso para crear la fecha
other_date = datetime.date(current_date.year + 1, current_date.month + 2, current_date.day - 1)

print(other_date)


difference = other_date - current_date

print(difference)

start_timedelta = datetime.timedelta(200, 100, 100, weeks=10)       ##  Crea un delta de tiempo con los parametros que paso
end_timedelta = datetime.timedelta(300, 100, 100, weeks=13)

print("start", start_timedelta)

print(end_timedelta - start_timedelta)                              ##  Puedo sumar y restar esos intervalos de tiempo
print(end_timedelta + start_timedelta)





