from pony.orm import Database, Required, Json
from settings import DB_CONFIG
db = Database()
db.bind(**DB_CONFIG)
# TODO стиль кода
class UserState(db.Entity):
    '''Состояние пользователя внутри сценария'''
    user_id = Required(str, unique=True)
    scenario_name = Required(str)
    step_name = Required(str)
    context = Required(Json)

class Ticket(db.Entity):
    '''Заявка на регистрацию'''
    city_out = Required(str)
    city_in = Required(str)
    flight_date = Required(str)
    flight_number = Required(str)

db.generate_mapping(create_tables=True)