from flask import Flask, render_template, request, redirect
import matplotlib.pyplot as plt
import openpyxl
import pandas as pd
import numpy as np
import array

app = Flask(__name__)

#Initial loading page
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

#Function to read excel file
@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        try:
            df = pd.read_excel(request.form['excel-file'])       
            return render_template('data.html', data=df.to_html())      
        except:
            return 'ERROR: can not process the excel file, return to the main page'
    else:
        return render_template('index.html')

#GET FUNCTION: stats test type

#df = pd.read_excel('Price.xlsx')

#for row in range(df.shape[0]):     --iterates rows (change to col for column)
#    print(df.iat[row,0])           --prints cell value
#print(df)

if __name__ == '__main__':
    app.run(debug=True)