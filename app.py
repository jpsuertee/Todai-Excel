from flask import Flask, render_template, request, redirect
import openpyxl
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/')


#GET FUNCTION: excel file from webapp 

#GET FUNCTION: stats test type

#df = pd.read_excel('Price.xlsx')

#for row in range(df.shape[0]):     --iterates rows (change to col for column)
#    print(df.iat[row,0])           --prints cell value

#print(df)

if __name__ == '__main__':
    app.run(debug=True)