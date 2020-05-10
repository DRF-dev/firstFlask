#!/usr/bin/python
# -*- coding: Utf-8 -*-
from flask import Flask, render_template
import platform
import netifaces

app = Flask(__name__)

@app.route('/')
def hello_world():
    data={
        'user':"DRF",
        'machine':platform.node(),
        'os':platform.system(),
        'dist':platform.linux_distribution(),
        'interface':netifaces.interfaces()
    }
    return render_template('hello.html', name="hello", data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)