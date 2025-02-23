from aiogram.fsm.state import StatesGroup, State

class Order(StatesGroup):
    category = State()
    cost_uan = State()
    photo = State()
    delivery = State()
    link = State()
    size = State()
    get_order = State()

class Calc(StatesGroup):
    cost = State()