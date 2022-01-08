from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from scipy.optimize import linprog
from sys import exit
from itertools import islice
from kalkulator import kalkulator


app = Flask(__name__)

x = pd.read_excel("TablicaNamirnica.xlsx")

categories = x["Kategorija"].drop_duplicates()

meats = x.loc[x["Kategorija"] == "MESO"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
fish = x.loc[x["Kategorija"] == "RIBA"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
eggs = x.loc[x["Kategorija"] == "JAJA"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
dairy = x.loc[x["Kategorija"] == "MLIJEČNI PROIZVODI"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
vegetables = x.loc[x["Kategorija"] == "POVRĆE"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
grains = x.loc[x["Kategorija"] == "ŽITARICE"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
fruit = x.loc[x["Kategorija"] == "VOĆE"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
nuts = x.loc[x["Kategorija"] == "ORAŠASTI PLODOVI"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
seeds = x.loc[x["Kategorija"] == "SJEMENKE"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
snacks = x.loc[x["Kategorija"] == "SLATKIŠI/SLANIŠI"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]


meats = [tuple(y) for y in meats.to_numpy()]
fish = [tuple(y) for y in fish.to_numpy()]
eggs = [tuple(y) for y in eggs.to_numpy()]
dairy = [tuple(y) for y in dairy.to_numpy()]
vegetables = [tuple(y) for y in vegetables.to_numpy()]
grains = [tuple(y) for y in grains.to_numpy()]
fruit = [tuple(y) for y in fruit.to_numpy()]
nuts = [tuple(y) for y in nuts.to_numpy()]
seeds = [tuple(y) for y in seeds.to_numpy()]
snacks = [tuple(y) for y in snacks.to_numpy()]

tuples = [tuple(y) for y in x.to_numpy()] 

@app.route('/')
def index():
    return render_template('index.html', data = [categories, meats, fish, eggs, dairy, vegetables, grains, fruit, nuts, seeds, snacks ,tuples])

@app.route('/callIndex')
def callIndex():
    return render_template('index.html')

@app.route('/callKatalog')
def callKatalog():
    meats = x.loc[x["Kategorija"] == "MESO"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
    meats = [tuple(y) for y in meats.to_numpy()]
    meats = iter(meats)
    meats = [list(islice(meats, elem)) for elem in [4,4,4,4,4,1]]
    return render_template('katalog.html', data = [categories, meats, fish, eggs, dairy, vegetables, grains, fruit, nuts, seeds, snacks ,tuples])
    #return render_template('katalog.html')

@app.route('/callRiba')
def callRiba():
    fish = x.loc[x["Kategorija"] == "RIBA"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
    fish = [tuple(y) for y in fish.to_numpy()]
    fish = iter(fish)
    fish = [list(islice(fish, elem)) for elem in [4,4,4,4,4,4,1]]
    return render_template('riba.html', data = [categories, meats, fish, eggs, dairy, vegetables, grains, fruit, nuts, seeds, snacks ,tuples])

@app.route('/callPovrce')
def callPovrce():
    vegetables = x.loc[x["Kategorija"] == "POVRĆE"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
    vegetables = [tuple(y) for y in vegetables.to_numpy()]
    vegetables = iter(vegetables)
    vegetables = [list(islice(vegetables, elem)) for elem in [4,4,4,4,4,4,4,4,4,2]]
    return render_template('povrce.html', data = [categories, meats, fish, eggs, dairy, vegetables, grains, fruit, nuts, seeds, snacks ,tuples])

@app.route('/callJaja')
def callJaja():
    eggs = x.loc[x["Kategorija"] == "JAJA"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
    eggs = [tuple(y) for y in eggs.to_numpy()]
    eggs = iter(eggs)
    eggs = [list(islice(eggs, elem)) for elem in [4,3]]
    return render_template('jaja.html', data = [categories, meats, fish, eggs, dairy, vegetables, grains, fruit, nuts, seeds, snacks ,tuples])

@app.route('/callZitarice')
def callZitarice():
    grains = x.loc[x["Kategorija"] == "ŽITARICE"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
    grains = [tuple(y) for y in grains.to_numpy()]
    grains = iter(grains)
    grains = [list(islice(grains, elem)) for elem in [4,4,4,4,4,4,4,2]]

    return render_template('zitarice.html', data = [categories, meats, fish, eggs, dairy, vegetables, grains, fruit, nuts, seeds, snacks ,tuples])


@app.route('/callSjemenke')
def callSjemenke():
    seeds = x.loc[x["Kategorija"] == "SJEMENKE"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
    seeds = [tuple(y) for y in seeds.to_numpy()]
    seeds = iter(seeds)
    seeds = [list(islice(seeds, elem)) for elem in [4,1]]
    return render_template('sjemenke.html',data = [categories, meats, fish, eggs, dairy, vegetables, grains, fruit, nuts, seeds, snacks ,tuples])

@app.route('/callOrasasti')
def callOrasasti():
    nuts = x.loc[x["Kategorija"] == "ORAŠASTI PLODOVI"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
    nuts = [tuple(y) for y in nuts.to_numpy()]
    nuts = iter(nuts)
    nuts = [list(islice(nuts, elem)) for elem in [4,2]]
    return render_template('orasasti.html', data = [categories, meats, fish, eggs, dairy, vegetables, grains, fruit, nuts, seeds, snacks ,tuples]) 

@app.route('/callVoce')
def callVoce():
    fruit = x.loc[x["Kategorija"] == "VOĆE"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
    fruit = [tuple(y) for y in fruit.to_numpy()]
    fruit = iter(fruit)
    fruit = [list(islice(fruit, elem)) for elem in [4,4,4,4,4,4,4,4,4]]
    return render_template('voce.html', data = [categories, meats, fish, eggs, dairy, vegetables, grains, fruit, nuts, seeds, snacks ,tuples]) 

@app.route('/callMlPro')
def callMlPro():
    dairy = x.loc[x["Kategorija"] == "MLIJEČNI PROIZVODI"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
    dairy = [tuple(y) for y in dairy.to_numpy()]
    dairy = iter(dairy)
    dairy = [list(islice(dairy, elem)) for elem in [4,4,4,4,4,4,4,4]]
    return render_template('mlpro.html',  data = [categories, meats, fish, eggs, dairy, vegetables, grains, fruit, nuts, seeds, snacks ,tuples]) 

@app.route('/callGrickalice')
def callGrickalice():
    snacks = x.loc[x["Kategorija"] == "SLATKIŠI/SLANIŠI"][["Naziv","Kalorije","Proteini","Ugljikohidrati","Masti","Kalij", "VitaminC", "Magnezij", "Kolesterol", "Natrij", "Željezo", "Kalcij", "Količina (g)", "Cijena (kn)", "Link"]]
    snacks = [tuple(y) for y in snacks.to_numpy()]
    snacks = iter(snacks)
    snacks = [list(islice(snacks, elem)) for elem in [4,4,4,4,4,4,1]]
    
    return render_template('grickalice.html', data = [categories, meats, fish, eggs, dairy, vegetables, grains, fruit, nuts, seeds, snacks ,tuples]) 


@app.route('/callRezultat')
def callRezultat():
    return render_template('error.html')

@app.route('/callCalculator')
def callCalculator():
    return render_template('calculator.html', data = [categories, meats, fish, eggs, dairy, vegetables, grains, fruit, nuts, seeds, snacks ,tuples])

    
@app.route('/getResult', methods =['POST'])
def getResult():
    userGoal = request.form.get('goalPick')
    checkedFoods = request.form.getlist('check')
    inputOption = request.form.get('option')
  
    n = len(checkedFoods)
   
    if inputOption == "custom":

        cijena = request.form.getlist('cijena')
        kalorije = request.form.getlist('kalorije')
        proteini = request.form.getlist('proteini')
        ugljikohidrati = request.form.getlist('ugljikohidrati')
        masti = request.form.getlist('masti')
        kalij = request.form.getlist('kalij')
        vitaminc = request.form.getlist('vitaminc')
        magnezij = request.form.getlist('magnezij')
        kolesterol = request.form.getlist('kolesterol')
        natrij = request.form.getlist('natrij')
        zeljezo = request.form.getlist('zeljezo')
        kalcij = request.form.getlist('kalcij')

        condNumb = 0
        condVals = []
        slackVars = []
        condCols = []

        if userGoal == "1": # minimizacija cijene
            c = x.loc[x["Naziv"].isin(checkedFoods)][["Cijena (kn)"]]
            c = np.array(c)

            if kalorije[0] != '3':
                condNumb += 1
                condVals.append(float(kalorije[1]))
                slackVars.append(float(kalorije[0]))
                condCols.append("Kalorije")

            if proteini[0] != '3':
                condNumb += 1
                condVals.append(float(proteini[1]))
                slackVars.append(float(proteini[0]))
                condCols.append("Proteini")

            if ugljikohidrati[0] != '3':
                condNumb += 1
                condVals.append(float(ugljikohidrati[1]))
                slackVars.append(float(ugljikohidrati[0]))
                condCols.append("Ugljikohidrati")

            if masti[0] != '3':
                condNumb += 1
                condVals.append(float(masti[1]))
                slackVars.append(float(masti[0]))
                condCols.append("Masti")

            if kalij[0] != '3':
                condNumb += 1
                condVals.append(float(kalij[1]))
                slackVars.append(float(kalij[0]))
                condCols.append("Kalij")

            if vitaminc[0] != '3':
                condNumb += 1
                condVals.append(float(vitaminc[1]))
                slackVars.append(float(vitaminc[0]))
                condCols.append("VitaminC")

            if magnezij[0] != '3':
                condNumb += 1
                condVals.append(float(magnezij[1]))
                slackVars.append(float(magnezij[0]))
                condCols.append("Magnezij")

            if kolesterol[0] != '3':
                condNumb += 1
                condVals.append(float(kolesterol[1]))
                slackVars.append(float(kolesterol[0]))
                condCols.append("Kolesterol")

            if natrij[0] != '3':
                condNumb += 1
                condVals.append(float(natrij[1]))
                slackVars.append(float(natrij[0]))
                condCols.append("Natrij")

            if zeljezo[0] != '3':
                condNumb += 1
                condVals.append(float(zeljezo[1]))
                slackVars.append(float(zeljezo[0]))
                condCols.append("Željezo")

            if kalcij[0] != '3':
                print("condition is different than 3")
                condNumb += 1
                condVals.append(float(kalcij[1]))
                slackVars.append(float(kalcij[0]))
                condCols.append("Kalcij")

            condNumb += 1
            condVals.append(1200.0)
            slackVars.append(-1)
            condNumpy = np.zeros((condNumb,1))
            condCols.append('Kalorije')

            c = np.concatenate((c, condNumpy)).T 
            c = np.squeeze(c)
            B = np.eye(condNumb)
            B = B * np.array(slackVars)
            b = np.array(condVals)
            print(condVals)

            A = np.zeros((condNumb,n+condNumb))
            for i in range(len(condCols)):
                A[i] = np.concatenate((np.squeeze(x.loc[x["Naziv"].isin(checkedFoods)][[condCols[i]]]), B[i]))

            lp = linprog(c, A_eq = A, b_eq = b)
            print(lp.x)
            print(lp.fun)

        elif userGoal == "2": # minimizacija kalorija
            c = x.loc[x["Naziv"].isin(checkedFoods)][["Kalorije"]]
            c = np.array(c)

            if cijena[0] != '3':
                condNumb += 1
                condVals.append(float(cijena[1]))
                slackVars.append(float(cijena[0]))
                condCols.append("Cijena (kn)")

            if proteini[0] != '3':
                condNumb += 1
                condVals.append(float(proteini[1]))
                slackVars.append(float(proteini[0]))
                condCols.append("Proteini")

            if ugljikohidrati[0] != '3':
                condNumb += 1
                condVals.append(float(ugljikohidrati[1]))
                slackVars.append(float(ugljikohidrati[0]))
                condCols.append("Ugljikohidrati")

            if masti[0] != '3':
                condNumb += 1
                condVals.append(float(masti[1]))
                slackVars.append(float(masti[0]))
                condCols.append("Masti")

            if kalij[0] != '3':
                condNumb += 1
                condVals.append(float(kalij[1]))
                slackVars.append(float(kalij[0]))
                condCols.append("Kalij")

            if vitaminc[0] != '3':
                condNumb += 1
                condVals.append(float(vitaminc[1]))
                slackVars.append(float(vitaminc[0]))
                condCols.append("VitaminC")

            if magnezij[0] != '3':
                condNumb += 1
                condVals.append(float(magnezij[1]))
                slackVars.append(float(magnezij[0]))
                condCols.append("Magnezij")

            if kolesterol[0] != '3':
                condNumb += 1
                condVals.append(float(kolesterol[1]))
                slackVars.append(float(kolesterol[0]))
                condCols.append("Kolesterol")

            if natrij[0] != '3':
                condNumb += 1
                condVals.append(float(natrij[1]))
                slackVars.append(float(natrij[0]))
                condCols.append("Natrij")

            if zeljezo[0] != '3':
                condNumb += 1
                condVals.append(float(zeljezo[1]))
                slackVars.append(float(zeljezo[0]))
                condCols.append("Željezo")

            if kalcij[0] != '3':
                condNumb += 1
                condVals.append(float(kalcij[1]))
                slackVars.append(float(kalcij[0]))
                condCols.append("Kalcij")

            condNumb += 1
            condNumpy = np.zeros((condNumb,1))
            condVals.append(1200.0)
            condCols.append('Kalorije')
            slackVars.append(-1)

            c = np.concatenate((c, condNumpy)).T 
            c = np.squeeze(c)
            B = np.eye(condNumb)
            B = B * np.array(slackVars)
            b = np.array(condVals)

            A = np.zeros((condNumb,n+condNumb))
            for i in range(len(condCols)):
                A[i] = np.concatenate((np.squeeze(x.loc[x["Naziv"].isin(checkedFoods)][[condCols[i]]]), B[i]))

            lp = linprog(c, A_eq = A, b_eq = b)
            print(lp.x)
            print(lp.fun)


        elif userGoal == "3": # maksimizacija željeza
            c = x.loc[x["Naziv"].isin(checkedFoods)][["Željezo"]]
            c = np.array(c)

            if kalorije[0] != '3':
                condNumb += 1
                condVals.append(float(kalorije[1]))
                slackVars.append(float(kalorije[0]))
                condCols.append("Kalorije")

            if proteini[0] != '3':
                condNumb += 1
                condVals.append(float(proteini[1]))
                slackVars.append(float(proteini[0]))
                condCols.append("Proteini")

            if ugljikohidrati[0] != '3':
                condNumb += 1
                condVals.append(float(ugljikohidrati[1]))
                slackVars.append(float(ugljikohidrati[0]))
                condCols.append("Ugljikohidrati")

            if masti[0] != '3':
                condNumb += 1
                condVals.append(float(masti[1]))
                slackVars.append(float(masti[0]))
                condCols.append("Masti")

            if kalij[0] != '3':
                condNumb += 1
                condVals.append(float(kalij[1]))
                slackVars.append(float(kalij[0]))
                condCols.append("Kalij")

            if vitaminc[0] != '3':
                condNumb += 1
                condVals.append(float(vitaminc[1]))
                slackVars.append(float(vitaminc[0]))
                condCols.append("VitaminC")

            if magnezij[0] != '3':
                condNumb += 1
                condVals.append(float(magnezij[1]))
                slackVars.append(float(magnezij[0]))
                condCols.append("Magnezij")

            if kolesterol[0] != '3':
                condNumb += 1
                condVals.append(float(kolesterol[1]))
                slackVars.append(float(kolesterol[0]))
                condCols.append("Kolesterol")

            if natrij[0] != '3':
                condNumb += 1
                condVals.append(float(natrij[1]))
                slackVars.append(float(natrij[0]))
                condCols.append("Natrij")

            if cijena[0] != '3':
                condNumb += 1
                condVals.append(float(cijena[1]))
                slackVars.append(float(cijena[0]))
                condCols.append("Cijena (kn)")

            if kalcij[0] != '3':
                print("condition is different than 3")
                condNumb += 1
                condVals.append(float(kalcij[1]))
                slackVars.append(float(kalcij[0]))
                condCols.append("Kalcij")

            condNumb += 1
            condNumpy = np.zeros((condNumb,1))
            condVals.append(1200.0)
            condCols.append('Kalorije')
            slackVars.append(-1)

            c = np.concatenate((c, condNumpy)).T 
            c = np.squeeze(c)
            B = np.eye(condNumb)
            B = B * np.array(slackVars)
            b = np.array(condVals)

            A = np.zeros((condNumb,n+condNumb))
            for i in range(len(condCols)):
                A[i] = np.concatenate((np.squeeze(x.loc[x["Naziv"].isin(checkedFoods)][[condCols[i]]]), B[i]))

            lp = linprog(-c, A_eq = A, b_eq = b)
            print(lp.x)
            print(lp.fun)


        else: # minimiziramo Na
            c = x.loc[x["Naziv"].isin(checkedFoods)][["Natrij"]]
            c = np.array(c)

            if kalorije[0] != '3':
                condNumb += 1
                condVals.append(float(kalorije[1]))
                slackVars.append(float(kalorije[0]))
                condCols.append("Kalorije")

            if proteini[0] != '3':
                condNumb += 1
                condVals.append(float(proteini[1]))
                slackVars.append(float(proteini[0]))
                condCols.append("Proteini")

            if ugljikohidrati[0] != '3':
                condNumb += 1
                condVals.append(float(ugljikohidrati[1]))
                slackVars.append(float(ugljikohidrati[0]))
                condCols.append("Ugljikohidrati")

            if masti[0] != '3':
                condNumb += 1
                condVals.append(float(masti[1]))
                slackVars.append(float(masti[0]))
                condCols.append("Masti")

            if kalij[0] != '3':
                condNumb += 1
                condVals.append(float(kalij[1]))
                slackVars.append(float(kalij[0]))
                condCols.append("Kalij")

            if vitaminc[0] != '3':
                condNumb += 1
                condVals.append(float(vitaminc[1]))
                slackVars.append(float(vitaminc[0]))
                condCols.append("VitaminC")

            if magnezij[0] != '3':
                condNumb += 1
                condVals.append(float(magnezij[1]))
                slackVars.append(float(magnezij[0]))
                condCols.append("Magnezij")

            if kolesterol[0] != '3':
                condNumb += 1
                condVals.append(float(kolesterol[1]))
                slackVars.append(float(kolesterol[0]))
                condCols.append("Kolesterol")

            if cijena[0] != '3':
                condNumb += 1
                condVals.append(float(cijena[1]))
                slackVars.append(float(cijena[0]))
                condCols.append("Cijena (kn)")

            if zeljezo[0] != '3':
                condNumb += 1
                condVals.append(float(zeljezo[1]))
                slackVars.append(float(zeljezo[0]))
                condCols.append("Željezo")

            if kalcij[0] != '3':
                condNumb += 1
                condVals.append(float(kalcij[1]))
                slackVars.append(float(kalcij[0]))
                condCols.append("Kalcij")

            condNumb += 1
            condNumpy = np.zeros((condNumb,1))
            condVals.append(1200.0)
            condCols.append('Kalorije')
            slackVars.append(-1)

            c = np.concatenate((c, condNumpy)).T 
            c = np.squeeze(c)
            B = np.eye(condNumb)
            B = B * np.array(slackVars)
            b = np.array(condVals)

            A = np.zeros((condNumb,n+condNumb))
            for i in range(len(condCols)):
                #print(B[i].shape)
                #print(x.loc[x["Naziv"].isin(checkedFoods)][[condCols[i]]].shape)
                A[i] = np.concatenate((np.squeeze(x.loc[x["Naziv"].isin(checkedFoods)][[condCols[i]]]), B[i]))
            
            lp = linprog(c, A_eq = A, b_eq = b)
            
            print(lp.x)
            print(lp.fun)


    
    else: # po defaultu računanje 
        spol = request.form.get('spol')
        tezina = request.form.get('tezina')
        godine = request.form.get('godine')
        aktivnost = request.form.get('aktivnost')
        tjMasa = request.form.get('tjMasa')
        values = kalkulator(aktivnost, tjMasa, spol, godine, tezina)

        
        
        if userGoal == "1": # minimizacija cijene
            b = [values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], values[10],1200]
            b = np.array(b)
            condCols = ['Kalorije', 'Proteini', 'Ugljikohidrati', 'Masti', 'Kalij', 'VitaminC', 'Magnezij', 'Kolesterol', 'Natrij', 'Željezo', 'Kalcij','Kalorije']
            c = x.loc[x["Naziv"].isin(checkedFoods)][["Cijena (kn)"]]
            c = np.array(c)
            condNumpy = np.zeros((len(condCols),1))
            c = np.concatenate((c, condNumpy)).T 
            c = np.squeeze(c)
            A = np.zeros((len(condCols),n+len(condCols)))
            B = np.eye(len(condCols))
            B[B.shape[0]-1, B.shape[0]-1] = -1 
            for i in range(len(condCols)):
                    A[i] = np.concatenate((np.squeeze(x.loc[x["Naziv"].isin(checkedFoods)][[condCols[i]]]), B[i]))

            print("A=",A)
            print("b=",b)
            print("c=",c)
            lp = linprog(c, A_eq = A, b_eq = b)
            print("lp.x=",lp.x)

        elif userGoal == "2" : # minimizacija kalorija
            b = [values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], values[10],1200]
            b = np.array(b)
            condCols = ['Proteini', 'Ugljikohidrati', 'Masti', 'Kalij', 'VitaminC', 'Magnezij', 'Kolesterol', 'Natrij', 'Željezo', 'Kalcij' ,'Kalorije']
            c = x.loc[x["Naziv"].isin(checkedFoods)][["Kalorije"]]
            c = np.array(c)
            condNumpy = np.zeros((len(condCols),1))
            c = np.concatenate((c, condNumpy)).T 
            c = np.squeeze(c)
            A = np.zeros((len(condCols),n+len(condCols)))
            B = np.eye(len(condCols))
            B[B.shape[0]-1, B.shape[0]-1] = -1 
            for i in range(len(condCols)):
                A[i] = np.concatenate((np.squeeze(x.loc[x["Naziv"].isin(checkedFoods)][[condCols[i]]]), B[i]))

            lp = linprog(c, A_eq = A, b_eq = b)

        elif userGoal == "3" : # maksimizacija željeza
            b = [values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[10],1200]
            b = np.array(b)
            condCols = ['Kalorije', 'Proteini', 'Ugljikohidrati', 'Masti', 'Kalij', 'VitaminC', 'Magnezij', 'Kolesterol', 'Natrij', 'Kalcij','Kalorije']
            c = x.loc[x["Naziv"].isin(checkedFoods)][["Željezo"]]
            c = np.array(c)
            condNumpy = np.zeros((len(condCols),1))
            c = np.concatenate((c, condNumpy)).T 
            c = np.squeeze(c)
            A = np.zeros((len(condCols),n+len(condCols)))
            B = np.eye(len(condCols))
            B[B.shape[0]-1, B.shape[0]-1] = -1 
            for i in range(len(condCols)):
                A[i] = np.concatenate((np.squeeze(x.loc[x["Naziv"].isin(checkedFoods)][[condCols[i]]]), B[i]))

            lp = linprog(-c, A_eq = A, b_eq = b)

        else : # minimizacija Na
            b = [values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[9], values[10], 1200]
            b = np.array(b)
            condCols = ['Kalorije', 'Proteini', 'Ugljikohidrati', 'Masti', 'Kalij', 'VitaminC', 'Magnezij', 'Kolesterol', 'Željezo', 'Kalcij','Kalorije']
            c = x.loc[x["Naziv"].isin(checkedFoods)][["Natrij"]]
            c = np.array(c)
            condNumpy = np.zeros((len(condCols),1))
            c = np.concatenate((c, condNumpy)).T 
            c = np.squeeze(c)
            A = np.zeros((len(condCols),n+len(condCols)))
            B = np.eye(len(condCols))
            B[B.shape[0]-1, B.shape[0]-1] = -1 
            for i in range(len(condCols)):
                A[i] = np.concatenate((np.squeeze(x.loc[x["Naziv"].isin(checkedFoods)][[condCols[i]]]), B[i]))
            
            lp = linprog(c, A_eq = A, b_eq = b)
    
    if lp.status != 0:
        return render_template("error.html")
    

    print("A=",A)
    print("b=", b)
    print("c =",c)
    
    cijene = x.loc[x["Naziv"].isin(checkedFoods)][["Cijena (kn)"]]
    kalorije = x.loc[x["Naziv"].isin(checkedFoods)][["Kalorije"]]
    slike = x.loc[x["Naziv"].isin(checkedFoods)][["Link"]]

    uk_cijena = 0
    uk_kalorije = 0

    cijene = np.array(cijene)
    kalorije = np.array(kalorije)
    slike = np.array(slike)
    kolicina = []
    namirnice = []
    lpString = ""
    lpArray = []

    for i in range(n):
        lpString += str(c[i]) + " x" + str(i) + " + "
        lpx = lp.x[i]
        if lpx > 0:
            if lpx < 0.1:
                lpx = 0.1
            namirnice.append(checkedFoods[i])
            kolicina.append(int(np.ceil(lpx * 100)))

        uk_cijena += lpx * cijene[i]
        print("lpx", lpx, "kalorije", kalorije[i])
        uk_kalorije += lpx * kalorije[i]

    if uk_kalorije < 1199:
        return render_template("error.html")

    print("UKUPNA CIJENA",uk_cijena)

    uk_cijena = round(uk_cijena[0],2)
    uk_kalorije = round(uk_kalorije[0],2)


    lpString = lpString[:len(lpString) - 3]

    if userGoal != "3" : # jedina maksimizacija
        lpString += " -> min"
    else:
        lpString += " -> max"

    lpArray.append(lpString)
    lpString = ""
    lpString += "uz uvjete"
    lpArray.append(lpString)

    print("B=",B)

    for row in range(len(condCols)):
        lpString = ""
        for col in range(n):
            lpString += str(A[row,col]) + " x" + str(col) + " + "
        lpString = lpString[:len(lpString) - 3] 
        print(B[row,row]) 
        if B[row,row] == -1.0:
            lpString += " >= "
        else:
            lpString += " <= "
        lpString += str(b[row])
        lpArray.append(lpString)
        
    lpString = ""
    for ind in range(n):
        lpString += "x"+str(ind)+", "

    lpString = lpString[:len(lpString) - 2]
    lpString += " >= 0"
    lpArray.append(lpString)

    duljina = len(namirnice)

    print("REZULTAT:")         
    print(namirnice)
    print(kolicina)
    print(slike)
    print(uk_cijena)
    print(uk_kalorije)
    print( lpArray)
    print(duljina)
    return render_template('rezultat.html', data = [namirnice, kolicina, slike, uk_cijena, uk_kalorije, lpArray, duljina])
    
    
    
    
    
    