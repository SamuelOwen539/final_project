from yelp import Yelp
from mapquest import MapQuest
from db import DB
from secrets import key
from flask import Flask, request, render_template, Response
import jinja2

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def home():

    return '''
    <style>
        h1 {text-align: center; font-size: 35px text-color: #565994;}
        h2 {text-align: left; font-size: 25px;}
        p {margin-left: 25px; text-indent: 15px; font-size: 22px}
        body {background-color: #ffd9d9;}
    </style>
<h1> <p> Welcome to Sushi Search!</p> </h1>
<h2> <p> Please enter a city to search for sushi restaurants in it </p> </h2>
    <form action="/project" method="POST" >
        <input type="string" name="location" />
        <input type="submit" name="name" value="Go to project page" />
    </form>
    '''


@app.route("/project", methods=['GET','POST'])
def project():
    db = DB()
    location = request.form['location']
    results = db.query(location)
    mapquest.yelp_data = results
    if results:
        # Using cached data
        pass
    else:
        # No cached data present, using data from Yelp API
        results = yelp.call(location)
        for result in results:
            db.entry(result)

    output = 'Name/Rating/Price<br>'
    index = 0
    for result in results:
        output+= f'{index}, {result[1]}, {result[2]}, {result[3]}<br>'
        index += 1
        if index == 10:
            break
    return f'''
    Results equal {output}
    <form action="/restaurants" method="POST" >
        <input type="number" name="restaurant" />
        <input type="submit" name="name" value="Go to restaurant's page" />
    </form>
    '''
@app.route("/restaurants", methods=['GET','POST'])
def restaurants():
    index = request.form['restaurant']
    print(mapquest.yelp_data)
    #yelp = Yelp()
    results = mapquest.call(int(index))
    return results

if __name__ == "__main__":
    # Don't forget to turn debug to False when launching
    yelp = Yelp()
    mapquest = MapQuest()
    app.run(host='0.0.0.0', port=8080, debug=True)

















