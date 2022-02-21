from distutils.log import debug
from itertools import count
from flask import Flask,render_template
from flask_redis import FlaskRedis

count = 0

app = Flask(__name__)
app.config['REDIS_URL']  = "redis://redis-server:6379/0"
#app.config['REDIS_DB'] = 0
redisclient = FlaskRedis(app)

@app.route("/")
def helloworld():
#    exit(1)     #1 means with error 0 is with error
    global count
    count = count +1
    redisclient.set("value1",count) 
    return "HelloWorld: {0}".format(redisclient.get("value1").decode("utf-8"))

@app.route("/hello")
def hello():
    return render_template("index.html", placeholder = "hello demo for Panos")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
