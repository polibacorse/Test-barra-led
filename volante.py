import paho.mqtt.client as mqtt
from neopixel import *
import time
import struct
import json

LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

def update_rpm(x):
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    if x > 1500:
        for j in range(1):
            strip.setPixelColorRGB(j,0,255,0)
            strip.setPixelColorRGB(LED_COUNT-j-1,0,255,0)
    if x > 3000:
        for j in range(1,2):
            strip.setPixelColorRGB(j,0,255,0)
            strip.setPixelColorRGB(LED_COUNT-j-1,0,255,0)
    if x > 4500:
        for j in range(2,3):
            strip.setPixelColorRGB(j,255,0,0)
            strip.setPixelColorRGB(LED_COUNT-j-1,255,0,0)
    if x > 6000:
        for j in range(3,4):
            strip.setPixelColorRGB(j,255,0,0)
            strip.setPixelColorRGB(LED_COUNT-j-1,255,0,0)
    if x > 7500:
        for j in range(4,5):
            strip.setPixelColorRGB(j,0,0,255)
            strip.setPixelColorRGB(LED_COUNT-j-1,0,0,255)
    if x > 9000:
        for j in range(5,6):
            strip.setPixelColorRGB(j,0,0,255)
            strip.setPixelColorRGB(LED_COUNT-j-1,0,0,255)
    if x > 10500:
        for j in range(6,7):
            strip.setPixelColorRGB(j,0,0,255)
            strip.setPixelColorRGB(LED_COUNT-j-1,0,0,255)
    if x > 12000:
        for j in range(7,9):
            strip.setPixelColorRGB(j,0,0,255)
            strip.setPixelColorRGB(LED_COUNT-j-1,0,0,255)
    """
    if x > 12500:
        for j in range (0,LED_COUNT):
            strip.setPixelColorRGB(j,255,255,255)
            time.sleep(0.2)
        for j in range (0,LED_COUNT):
            strip.setPixelColorRGB(j,0,0,0)
            time.sleep(0.2)
        for j in range (0,LED_COUNT):
            strip.setPixelColorRGB(j,255,255,255)
            
    """
    strip.show()

def on_connect(client, userdata, flags, rc):
    client.subscribe("$SYS/formatted/rpm")

def on_message(client, userdata, msg):
    json_msg = msg.payload.decode('utf-8') # se ricevi solo il valore direttamente
    json_msg = json.loads(json_msg)
    # print(str(rpm), ord(rpm.decode('utf-8')), len(rpm)) # per il debug, stampa a schermo
    update_rpm(json_msg['value'])

def main():
    client = mqtt.Client()
    client.on_connect = on_connect # ti sottoscrivi al topic appena ti connetti a MQTT
    client.on_message = on_message # ricevi in modo asincrono gli rpm e aggiorni il volante

    client.connect("localhost", 1883, 60)
    client.loop_forever()

if __name__ == '__main__':
    main()
