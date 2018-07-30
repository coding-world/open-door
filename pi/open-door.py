from flask import Flask
import csv
from gpiozero import LED
from time import sleep

door = LED(26)
membersNumbers = []
with open('members.csv', 'r') as csvfile:
    global membersNumbers
    csvRead = csv.reader(csvfile, delimiter=',')
    for singleNumber in csvRead:
        membersNumbers.append(singleNumber)

def checkNumber(number, numbers):
    print(type(numbers))
    for row in numbers:
        print(row[0])
        if row[0] == number:
            return True
    return False

def openDoor():
    door.on()
    sleep(1)
    door.off()
app = Flask(__name__)

@app.route("/")
def hello():
    print('hello world')
    return "Hello World!"

@app.route('/number/<caller_number>')
def show_post(caller_number):
    global membersNumbers
    print(caller_number)
    if checkNumber(caller_number, membersNumbers):
        openDoor()
        return "ok"
    else:
        return "401"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
