from flask import Flask, request
import json
import time

app = Flask(__name__)

host_addr = "0.0.0.0"
port_num = "3300"

@app.route("/test", methods = ['POST'])
def test():
    #print("Time:" + str(int(round(time.time() * 1000))) + ", reqeust from client : " + str(request.json['data']))
    print(request.json)
    return str(request.json)

if __name__ == "__main__":
    app.run(host = host_addr, port = port_num)