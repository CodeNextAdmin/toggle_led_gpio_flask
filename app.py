from flask import Flask , render_template
import datetime
from gpiozero import LED


led = LED(4)
led.off()
led_state = ""

app = Flask(__name__)

@app.route("/")
def index():
    global led, led_state
    
    led.on()

    print(led.is_lit )
    if led.is_lit == True:
        led_state = "on"
         
         
    elif led.is_lit == False:
        led_state = "off"
         
    print(led_state)
    message = led.pin
    templateData = {

    'title' : "LED Toggle",
    'led_state' : led_state,
    'msg' : message
    }

    return render_template('lights.html' , **templateData)


@app.route("/<state>")
def toggle_led(state):
    global led, led_state

    try:      
        if  state == "off":
            led.off()
            led_state = state
        elif  state == "on":
            led.on()
            led_state = state

        
        
    except:
        response = "There was an error"

    message = led.pin

    print("led_state " + led_state)
    print(message)
    
    templateData = {

    'title' : "LED Toggle",
    'msg' : message,
    'led_state' : led_state
    }
    
    return render_template('lights.html' , **templateData)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    

 