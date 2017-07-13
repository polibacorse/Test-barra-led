from ADCPi import ADCPi
import time
import os
import neopixel

LED_COUNT = 16
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTENESS = 200
LED_INVERT = False

#i2c_helper = ABEHelpers() #inizializzazioni standard
#bus = i2c_helper.get_smbus()
adc = ADCPi.ADCPi(0x68, 0x69, 12)

def main():
        strip = neopixel.Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTENESS)
        strip.begin()

        while (True):
                rpm = adc.read_voltage(1)
                print(rpm) # debug tensione
                if rpm > 1 and rpm < 2:
                        for j in range(1):
                                strip.setPixelColorRGB(j, 0, 255, 0)
                                strip.setPixelColorRGB(LED_COUNT-j-1,0, 255, 0)
                        for i in range(2,15):
                                strip.setPixelColorRGB(i,0,0,0)
                if rpm > 2 and rpm < 3:
                        for j in range(1,2):
                                strip.setPixelColorRGB(j, 0, 255, 0)
                                strip.setPixelColorRGB(LED_COUNT-j-1,0, 255, 0)
                        for x in range (2,4):
                                strip.setPixelColorRGB(x,255,0,0)
                                strip.setPixelColorRGB(LED_COUNT-x-1,255,0,0)
                        for i in range(4,12):
                                strip.setPixelColorRGB(i,0,0,0)
                if rpm > 3 and rpm < 4:
                        for i in  range(1,2):
                                strip.setPixelColorRGB(j, 0, 255, 0)
                                strip.setPixelColorRGB(LED_COUNT-j-1,0, 255, 0)
                        for x in range (2,4):
                                strip.setPixelColorRGB(x,255,0,0)
                                strip.setPixelColorRGB(LED_COUNT-x-1,255,0,0)
                        for j in range(5,6):
                                strip.setPixelColorRGB(j, 0, 0, 255)
                                strip.setPixelColorRGB(LED_COUNT-j-1,0, 0, 255)
                        for i in range (7,11):
                                strip.setPixelColorRGB(i,0,0,0)
                if rpm > 4 and rpm < 6:
                        for i in  range(1,2):
                                strip.setPixelColorRGB(i, 0, 255, 0)
                                strip.setPixelColorRGB(LED_COUNT-i-1,0, 255, 0)
                        for x in range (2,4):
                                strip.setPixelColorRGB(x,255,0,0)
                                strip.setPixelColorRGB(LED_COUNT-x-1,255,0,0)
                        for j in  range(5,6):
                                strip.setPixelColorRGB(j, 0, 0, 255)
                                strip.setPixelColorRGB(LED_COUNT-j-1,0, 0, 255)
                        for p in  range(7,8):
                                strip.setPixelColorRGB(p, 0, 0, 255)
                                strip.setPixelColorRGB(LED_COUNT-p-1,0, 0, 255)
                strip.show()

if __name__ == '__main__':
        main()
