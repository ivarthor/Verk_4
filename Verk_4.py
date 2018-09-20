from sys import argv
import bottle
from bottle import *
import urllib.request, json


#with open("gengi.json","r") as skra:
 #   gogn = json.load(skra)



@route("/")
def index():
    return """
        <h2>Verkefni 4</h2
        <p><a href="/a">Json local</a></p>
        <p><a href="/b">json af APIs.is</a></p>
    """


@route("/a")
def index():
    return template("index.tpl")

with urllib.request.urlopen("http://apis.is/currency/") as url:
    data = json.loads(url.read().decode())

@route("/b")
def index():
    return template("index2.tpl", data = data)



###############################################
@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root = "./static")

@error(404)
def error404(error):
    return "ERROR"


bottle.run(host="0.0.0.0",port=argv[1])
#bottle.run(host="localhost", port=7000, debug=True)
