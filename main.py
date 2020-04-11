from flask import Flask,render_template
import json,requests
countries_api = requests.get("https://api.covid19api.com/summary")
# confirmed_api = requests.get(f"/dayone/country/{country}/status/{status}/live")
country_list = json.loads(countries_api.text)
app = Flask(__name__)
@app.route('/list')
def list():
    return render_template('list.html', country_name = [ cname for  cname in (country_list['Countries'])] )
@app.route('/')
def home():
    return render_template('index.html', date_raw = [ date for date in (country_list['Date'][0:10])],mm_raw = [ mm for mm in country_list['Countries'] if mm['Country']=="Myanmar"])
@app.route('/contactmap')
def contactmap():
    return render_template('contactmap.html')
@app.route('/patientmap')
def patientmap():
    return render_template('patientmap.html')
if  __name__ == "__main__":
    app.run(debug=True)