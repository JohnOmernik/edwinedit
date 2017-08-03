#!/usr/bin/python3
import time
import re
from flask import Flask, request, render_template, jsonify, make_response
from wtforms import Form, BooleanField, HiddenField, TextField, TextAreaField, widgets, SelectMultipleField, RadioField
import hashlib
import re
import json
import os
import random
from collections import OrderedDict
from time import strftime
# Flask setup
app = Flask(__name__)

try:
    app_root = os.environ["EDWIN_BASE"]
except:
    app_root = "/app/edwin"


@app.route('/', methods=['GET', 'POST'])
def index():
    curval = loaddata(app_root + "/edwin.json")
    return render_template('index.html', curval=json.dumps(curval))

@app.route('/save_edwin', methods=['POST'])
def save_edwin():

    output = request.json
    j_out = json.loads(output, object_pairs_hook=OrderedDict)
    arc = archivedata()
    if arc == 0:
        print("Archive Successful!")
        result = savedata(app_root + "/edwin.json", j_out)
        if result == 0:
            print("Save Successful!")
            curval = loaddata(app_root + "/edwin.json")
        else:
            print("Save Failed!")
            curval = j_out
    else:
        print("Archive Failed!")
        curval = j_out
    return render_template('index.html', curval=json.dumps(curval))

def archivedata():
    retval = 0
    curtime = strftime("%Y%m%d%H%M%S")
    archive_file = app_root + "/archive/edwin_" + str(curtime) + ".json"
    try:
        curdata = loaddata(app_root + "/edwin.json")
    except:
        retval = -1 # -1 can't load file
    if retval == 0:
        result = savedata(archive_file, curdata)
        if result != 0:
            retval = 1
    return retval

def fixdata(indata):

    u = indata
    u = u.replace("&lt;empty&gt;", "")
    u = u.replace("&gt;", ">")
    u = u.replace("&lt;", "<")
    return u


def savedata(jsonfile, jdata):
    retval = 0
    try:
        u = open(jsonfile, 'w')
        u.write(fixdata(json.dumps(jdata, sort_keys=False, indent=4, separators=(',', ': '))) + "\n")
        u.close()
    except:
        retval = 1
        print("Error saving json data to %s" % jsonfile)
    return retval


def loaddata(jsonfile):
    try:
        u = open(jsonfile, 'r')
    except:
        retj = {"error": "file could not be opened"}
    try:
        j = u.read()
        u.close()
    except:
        retj = {"error": "file could not be read"}
    try:
        retj = json.loads(j, object_pairs_hook=OrderedDict)
    except:
        retj = {"error": "json parsing error"}
    return retj



if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=5000)





