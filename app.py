from flask import Flask
from random import choice
from ast import literal_eval
app = Flask(__name__)
file = open("bad.txt", "r")
bad = file.readlines()
file.close()
file = open("duration.txt", "r")
duration = file.readlines()
file.close()
file = open("good.txt", "r")
good = file.readlines()
file.close()
file = open("instant.txt", "r")
instant = file.readlines()
file.close()
file = open("target.txt", "r")
target = file.readlines()
file.close()
file = open("types.txt", "r")
types = list(map(literal_eval, file.readlines()))
file.close()

things = {
    "bad":bad,
    "duration":duration,
    "good":good,
    "instant":instant,
    "target":target
}

@app.route('/')
def hello():
    template = choice(types)
    output = []
    for x in template:
        if x in things.keys():
            output.append(choice(things[x]))
        else: output.append(x)
    return " ".join(output)

if __name__ == '__main__':
    app.run()