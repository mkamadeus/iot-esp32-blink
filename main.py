import time
from machine import Timer, Pin
from umqtt.robust import MQTTClient

# constants
LED_PIN = 19
BUTTON_PIN = 21
POLL_INTERVAL_MS = 5000
MQTT_SERVER = "192.168.0.129"

# mqtt client
client = MQTTClient("esp32-blink", MQTT_SERVER, port=1883)
print("connecting to mqtt broker")
client.reconnect()

led = Pin(LED_PIN, Pin.OUT)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

print("blinking lights")

frequency = 10

last_tick_blink = 0
last_tick_poll = 0
last_button_state = False

while True:
    # calculation
    period = 1/frequency
    current_tick = time.ticks_ms()
    
    # blink
    if(time.ticks_diff(current_tick, last_tick_blink) > period*1000):
        if(led.value() == 0):
            led.on()
        else:
            led.off()
        last_tick_blink = current_tick
    
    # poll
    if(time.ticks_diff(current_tick, last_tick_poll) > POLL_INTERVAL_MS):
        msg = b'%s:%s' % ("13518035", frequency)
        print('publishing message to broker')
        client.publish("13518035", msg)
        last_tick_poll = current_tick
    
    # button
    button_state = button.value()
    if(last_button_state == button_state):
        pass
    else:
        if(button_state):
            frequency += 1
        last_button_state = button_state
            