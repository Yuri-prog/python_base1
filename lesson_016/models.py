import peewee
#import sqlite3
database = peewee.SqliteDatabase('weather.db')

class BaseTable(peewee.Model):
    # В подклассе Meta указываем подключение к той или иной базе данных
    class Meta:
        database = database

class Weather(BaseTable):
    date = peewee.DateTimeField()
    temp_d = peewee.CharField()
    cloud_d = peewee.CharField()
    wind_d = peewee.CharField()
    pres_d = peewee.CharField()
    temp_n = peewee.CharField()
    cloud_n = peewee.CharField()
    wind_n = peewee.CharField()
    pres_n = peewee.CharField()


database.create_tables([Weather])
