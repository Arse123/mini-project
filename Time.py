import datetime as dt
# Как и раньше - определяем текущее время UTC
utc_time = dt.datetime.utcnow()
# Создаём промежуток времени в 4 часа
period = dt.timedelta(hours=4)
# И прибавляем к значению времени по UTC поправку в 4 часа:
erevan_time = utc_time + period
# Печатаем
print(erevan_time) 
input('Нажмите ENTER для выхода')