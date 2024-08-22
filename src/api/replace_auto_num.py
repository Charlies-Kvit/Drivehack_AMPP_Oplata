def replace_auto_num(car_plate: list):
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
    return "".join(car_plate)
