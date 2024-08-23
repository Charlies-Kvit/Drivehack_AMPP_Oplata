import json

from fastapi import FastAPI
from src.data import db_session
from src.data.client import Client
from src.api.replace_auto_num import replace_auto_num
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World, and Moscow State Transport in particular"}


al = ["А", "В", "С", "Т", "У", "Р", "М", "О", "Е", "К", "Х", "Н"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
plates = {"А100НЕ199": "водила дебил", "В092АУ199": "крутой водитель", "А001АА77": "ахахах мажор"}


@app.get("/api/{car_plate}")
def get_notification(car_plate: str):
    car_plate = list(car_plate)
    car_plate = replace_auto_num(car_plate)
    try:
        if not (str(car_plate[0]) in al and (car_plate[1] in numbers) and (car_plate[2] in numbers) and (
                car_plate[3] in numbers) and (car_plate[4] in al) and (car_plate[5] in al) and int(
            car_plate[6:]) < 900):
            return {"event": False, "error": "несуществующий номер"}
        session = db_session.create_session()
        in_database = session.query(Client).filter(Client.auto_number.upper() == car_plate.upper())
        session.close()
        if not in_database:
            return {"event": False}
        elif car_plate.upper() in plates.keys():
            return {"event": True, "message": plates[car_plate.upper()]}
        else:
            return {"event": False}
    except:
        return {"event": False, "error": "несуществующий номер"}


@app.get("/api/login")
def login_view(login: str, password: str):
    if login in users.keys():
        if users[login]["password"] == password:
            return {"event": True, "login": True, "message": "Вы залогинены."}
        else:
            return {"event": False, "login": False, "message": "Пароль неверный."}
    else:
        return {"event": False, "login": False, "message": "Нет такого пользователя, попробуйте зарегистрироваться."}


@app.get("/api/registration")
def registration_view(phone_number: int, car_number: str, login: str, password: str):
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            users = json.load(f)
    else:
        users = dict()
    if login not in users.keys():
        return {"event": True, "login": True, "message": "Вы зарегистрированы."}
    else:
        return {"event": True, "login": True, "message": "Такой пользователь уже есть."}


if __name__ == '__main__':
    db_session.global_init("../db/db.sqlite")
    uvicorn.run(app, port=8080, host='0.0.0.0')
