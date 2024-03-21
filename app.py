from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    weather_data = get_weather(city)
    return render_template('weather.html', weather_data=weather_data)

def get_weather(city):
    API_KEY = "9bcb85d1907b1dae50d2b8a598805ed0"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data.")
        return None

if __name__ == "__main__":
    app.run(debug=True)
