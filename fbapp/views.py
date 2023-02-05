
from flask import Flask, render_template, request
import pandas as pd
import dill

app = Flask(__name__)

with (open('model2.pkl', 'rb')) as file:
    model = dill.load(file)


@app.route('/passerTest')
def PasserLeTest():
    return render_template('passerleTest.html')

@app.route('/')
def index():
    return render_template('inde.html')


@app.route('/result' , methods=['POST'])
def route_function():
    df = pd.DataFrame(columns=['ginf1',	'gstr1',	'gsea1',	'ginf2',	'gind1',	'gstr2',	'g3ei1',	'gsea2',	'gind2',	'g3ei2'])
    df.loc[0] = [request.form['ginf1'], request.form['gstr1'], request.form['gsea1'], request.form['ginf2'], request.form['gind1'], request.form['gstr2'], request.form['g3ei1'], request.form['gsea2'], request.form['gind2'], request.form['g3ei2']]
    # etc. for all the questions
    # Open the CSV file for writing
    prediction = model.predict(df)
    if prediction == 0:
        return render_template('gstr.html', name='Votre place est dans la filière "GSTR" ')
    elif prediction == 1:
        return render_template('gsea.html', name='Votre place est dans la filière "GSEA" ')
    elif prediction == 2:
        return render_template('geeei.html', name='Votre place est dans la filière "G3EI" ')
    elif prediction == 3:
        return render_template('gind.html', name='Votre place est dans la filière "GIND" ')
    elif prediction == 4:
        return render_template('ginf.html', name='Votre place est dans la filière "GINF" ')
    else:
        return "Prediction value not in range"




@app.route('/filieres')
def filieres():
    return render_template('filieres.html')


@app.route('/ginf')
def ginf():
    return render_template('ginf.html')
@app.route('/gstr')
def gstr():
    return render_template('gstr.html')
@app.route('/gind')
def gind():
    return render_template('gind.html')
@app.route('/gsea')
def gsea():
    return render_template('gsea.html')
@app.route('/g3ei')
def g3ei():
    return render_template('geeei.html')

if __name__ == "__main__":
    app.run()

    #ginf ; u dont give up , autoformation . 