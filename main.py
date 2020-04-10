from flask import Flask,render_template
import json,requests
countries_api = requests.get("https://api.covid19api.com/summary")
# confirmed_api = requests.get(f"/dayone/country/{country}/status/{status}/live")
country_list = json.loads(countries_api.text)
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', country_name = [ cname for  cname in (country_list['Countries'])] )
if  __name__ == "__main__":
    app.run(debug=True)