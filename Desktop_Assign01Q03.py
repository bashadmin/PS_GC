def check_speed(speed):
    if speed <= 0:
        points = 0
    kmph_above = abs(speed - 70)
    points = 0
    points = kmph_above // 5
    if kmph_above % 5 != 0:
        points += 1
    if speed <= 0:
        print("OK")
    elif points == 0:
        print("OK")
    elif points <= 12 and points != 0:
        print("\"Points: " + str(points) + "\"")
    else:
        print("\"License suspended\"")

check_speed(69)
check_speed(71)
check_speed(76)
check_speed(131)
check_speed(0)