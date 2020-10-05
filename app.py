from flask import Flask, request, jsonify
import joblib
from flasgger import Swagger

model = joblib.load("final_rf_solar.pkl")

app = Flask(__name__)
Swagger(app)

@app.route('/')
def wel():
    return "Welcome sdfsfsfsdfsdfsdf!!!"

@app.route('/predict', methods=['POST'])
def prediction():
    """Lets predict the solar radiance!
    ---
    parameters:
        - name: Temperature (Celcius)
          in: query
          type: number
          required: true
        - name: Pressure (Hg)
          in: query
          type: number
          required: true
        - name: Humidity (%)
          in: query
          type: number
          required: true    
        - name: Speed (kph)
          in: query
          type: number
          required: true
        - name: Day (out of 365)
          in: query
          type: number
          required: true
        - name: Month (out of 12)
          in: query
          type: number
          required: true
        - name: WindDirections (degrees)
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output value          
    """
    
    s_temp = request.args.get("Temperature (Celcius)")
    s_pre = request.args.get("Pressure (Hg)")
    s_hum = request.args.get("Humidity (%)")
    s_win = request.args.get("WindDirections (degrees)")
    s_spe = request.args.get("Speed (kph)")
    s_day = request.args.get("Day (out of 365)")
    s_mon = request.args.get("Month (out of 12)")

    ds = [[s_temp, s_pre, s_hum, s_win, s_spe, s_day, s_mon]]

    pre = model.predict(ds)

    return str(round(pre[0],2))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
