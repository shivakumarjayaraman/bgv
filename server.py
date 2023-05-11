#!/usr/bin/env python3

from flask import *
import pandas as pd
import numpy as np
import re

app = Flask(__name__)

partOne = """
<html>
    <body>
"""


partTwo="""
    <h2>Enter the name of the employer/college</h2>
    <form method="post">
        <input name="value" type="text"/>
	<input type="submit" name="Check" />
    </form>
    </body>
</html>
"""

employers = pd.read_excel('Fraud.xlsx', sheet_name=0).to_numpy();
colleges = pd.read_excel('Fraud.xlsx', sheet_name=1).to_numpy();

badEmps = set()
badColleges = set()

for row in employers:
    badEmps.add(re.sub("[,-.& ']", "", row[0].strip()).lower())
for row in colleges:
    badColleges.add(re.sub("[,-.& ']", "", row[0].strip()).lower())


@app.route("/", methods=['GET'])
def home() :
    return partOne + partTwo

@app.route("/", methods=['POST'])
def search() :
    origval = request.form['value']
    val = re.sub("[,-.& ']", "", origval.strip().lower())
    partMid = ""
    if val in badEmps :
        partMid = f"<font color='red'>{origval} is a shady employer</font><br>"
    elif val in badColleges :
        partMid = f"<font color='red'>{origval} is a shady college</font><br>"
    else  :
        partMid = f"<font color='green'>{origval} sounds legit</font><br>"
    return partOne + partMid + partTwo
        

if __name__ == '__main__' :
    app.run(host="0.0.0.0")
