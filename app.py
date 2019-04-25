# @Author: Caillon Antoine <antoine>
# @Date:   2019-04-25T22:50:21+02:00
# @Email:  caillonantoine@gmail.com
# @Last modified by:   antoine
# @Last modified time: 2019-04-26T00:06:46+02:00



from flask import Flask, request, render_template, send_file
from os import system
from time import time

app = Flask(__name__)

names = [
    "antoine",
    "gabriel",
    "valentin",
    "macron",
    "brigitte",
    "adele"
]

@app.route("/convert", methods=["POST"])
def convert():
    print(f"Converting audio file to {request.form['gin']}")
    audio = request.files["sound"]

    filename = f"audio_{int(time())}.wav"

    audio.save(f"static/{audio.filename}")

    system(f"ffmpeg -i \"static/{audio.filename}\" -ar 22050 -y static/{filename}.wav")

    return render_template("index.html", gin=names, audio=f"static/{filename}.wav")

@app.route("/")
def main():
    return render_template("index.html", gin=names)
