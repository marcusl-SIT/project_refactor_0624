import base64
from io import BytesIO

import pandas as pd

from flask import Flask, request, jsonify

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello world!"

@app.route('/plot')
def list_cols():
	return 'Columns available:\n'+','.join(df.columns.to_list())

@app.route('/plot/<col>')
def plot(col):
    if col in df.columns:
        fig, ax = plt.subplots()
        df[col].plot(ax=ax)
        fig.savefig(f'static/{col}_plot.png', format="png")
        plt.close(fig)
        img_tag = f"<img src='/static/{col}_plot.png'/>"
        return img_tag
    else:
        return f"Column '{col}' not found in DataFrame."

@app.route('/add_data', methods = ['GET', 'POST'])
def add_data():
	if request.method == 'POST':
		#data = request.form
		data = request.get_json()
		#return str(data)
		global df
		for k,v in data.items():
			df[k] = v
		return jsonify(df.to_dict())

	elif request.method == 'GET':
		return 'Use this endpoint w/ POST to add data to DF.'

if __name__ == "__main__":
   df = pd.read_csv('data.csv')
   df = df.astype(int)
   app.run(host='0.0.0.0', port=5001, debug=True)
