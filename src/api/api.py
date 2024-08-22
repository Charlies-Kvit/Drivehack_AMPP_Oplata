from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World, and Moscow State Transport in particular"}


al = ["А", "В", "С", "Т", "У", "Р", "М", "О", "Е", "К", "Х", "Н"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
plates = {"А100НЕ199": "водила дебил", "В092АУ199": "крутой водитель", "А001АА77": "ахахах мажор"}


@app.get("/api/{car_plate}")
def read_item(car_plate: str):
    car_plate = list(car_plate)
    for i in range(len(car_plate)):
        match car_plate[i].upper():
            case "A":
                car_plate[i] = "А"
            case "B":
                car_plate[i] = "В"
            case "C":
                car_plate[i] = "С"
            case "T":
                car_plate[i] = "Т"
            case "Y":
                car_plate[i] = "У"
            case "P":
                car_plate[i] = "Р"
            case "M":
                car_plate[i] = "М"
            case "O":
                car_plate[i] = "О"
            case "E":
                car_plate[i] = "Е"
            case "K":
                car_plate[i] = "К"
            case "X":
                car_plate[i] = "Х"
            case "H":
                car_plate[i] = "Н"
    car_plate = "".join(car_plate)
    print(car_plate[0] in al)
    try:
        if not (str(car_plate[0]) in al and (car_plate[1] in numbers) and (car_plate[2] in numbers) and (
                car_plate[3] in numbers) and (car_plate[4] in al) and (car_plate[5] in al) and int(
                car_plate[6:]) < 900):
            return {"event": False, "error": "несуществующий номер"}
        elif car_plate.upper() in plates.keys():
            return {"event": True, "message": plates[car_plate.upper()]}
        else:
            return {"event": False}
    except:
        return {"event": False, "error": "несуществующий номер"}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
