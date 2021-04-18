from yelp import Yelp
from mapquest import MapQuest

from flask import Flask, request, render_template, Response
import jinja2

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():

    return '''
    <form action="/project" method="POST" >
        <input type="string" name="location" />
        <input type="submit" name="name" value="Go to project page" />
    </form>
    '''


@app.route("/project", methods=['GET','POST'])
def project():
    location = request.form['location']
    print(location)
    yelp = Yelp()
    yelp.call(location)


    return f'''
    
    Results equal {yelp.store_data}
    <form action="/restaurants" method="POST" >
        <input type="string" name="restaurant" />
        <input type="submit" name="name" value="Go to restaurant's page" />
    </form>
    '''
@app.route("/restaurants", methods=['GET','POST'])
def restaurants():
    restaurant_name = request.form['restaurant']
    return restaurant_name

if __name__ == "__main__":
    # Don't forget to turn debug to False when launching
    app.run(host='0.0.0.0', port=8080, debug=True)















