from fastapi import FastAPI, Request
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
async def get_notification(car_plate: str):
    car_plate = list(car_plate)
    car_plate = replace_auto_num(car_plate)
    try:
        if not (str(car_plate[0]) in al and (car_plate[1] in numbers) and (car_plate[2] in numbers) and (
                car_plate[3] in numbers) and (car_plate[4] in al) and (car_plate[5] in al) and
                int(car_plate[6:]) < 900):
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


@app.post("/api/login")
async def login_view(request: Request):
    json_data = await request.json()
    session = db_session.create_session()
    user = session.query(Client).filter(Client.phone_number == json_data['phone_number']).first()
    if user:
        if user.check_password(json_data['password']):
            token = user.token
            return {"event": True, "login": True, "message": "Вы залогинены.", "token": token}
        else:
            return {"event": False, "login": False, "message": "Пароль неверный."}
    else:
        return {"event": False, "login": False, "message": "Нет такого пользователя, попробуйте зарегистрироваться."}


@app.get("/api/registration")
async def registration_view(request: Request):

    session = db_session.create_session()

    if login not in users.keys():
        return {"event": True, "login": True, "message": "Вы зарегистрированы."}
    else:
        return {"event": True, "login": True, "message": "Такой пользователь уже есть."}


if __name__ == '__main__':
    db_session.global_init("../db/db.sqlite")
    uvicorn.run(app, port=8080, host='0.0.0.0')
