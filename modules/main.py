import sys
import json
import cv2

from SLAM.car import Car
from COMCS import clientRobot

imgPath = "/tmp/cv2-img.png"

car = Car(debug=True)
rawStudents = json.loads(clientRobot.initConnexion())

nbEleves = rawStudents["numberOfStudents"]
students = {}
for i in range(nbEleves):
    students[rawStudents["ids"][i]] = rawStudents["firstnames"], rawStudents["lastnames"]

count = 20
try:
    for _ in range(count):
        car.randomMove()
        img = car.capture()
        if img is None:
            print("Photo error", file=sys.stderr)
        else:
            cv2.imwrite(imgPath, img)
            rep = json.loads(clientRobot.sendFile(imgPath))
            if not rep:
                continue
            for trash, pos in rep.items():
                if len(pos) != 2:
                    print("Invalid coordinates (two values needed)", file=sys.stderr)
                    continue
                x = int(pos[0])
                y = int(pos[1])
                width = img.size
                height = img[0].size
                print(trash, x, y, width, height)
                car.goNear(width, height, x, y, 0, 0)
                # appelle coque pour dire qu'il y a un déchet
                # récupérer les infos de l'interaction
                # id bracelet, type proposé par la coque, bool réponse enfant
                # clientRobot.sendInfoCoque(ident, trash, type_rand, rep)
                break

except KeyboardInterrupt:
    print("Interrupted !", file=sys.stderr)
finally:
    car.speed = 0
    car.turn_straight()
    car.stop()
    clientRobot.stopConnexion()