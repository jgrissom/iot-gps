# main.py

from machine import Pin, UART, SoftI2C
import ssd1306
from micropyGPS import MicropyGPS
import asyncio
from async_button import Pushbutton

def handle_press():
    print('press')
    led.on()
    my_gps.saved_lat = my_gps.latitude
    my_gps.saved_lon = my_gps.longitude
    my_gps.saved_sat = my_gps.satellites_in_use

def handle_long():
    print('long')
    led.off()
    my_gps.saved_lat = None
    my_gps.saved_lon = None
    my_gps.saved_sat = 0

async def main():
    while True:
        if (my_gps.saved_lat == None or my_gps.saved_lon == None):
            length = gps_module.any()
            if length > 0:
                b = gps_module.read(length)
                for x in b:
                    msg = my_gps.update(chr(x))
            latitude = my_gps.convert(my_gps.latitude)
            longitude = my_gps.convert(my_gps.longitude)
            satellites = my_gps.satellites_in_use
            target = "---NO  TARGET---"
        else:
            latitude = my_gps.convert(my_gps.saved_lat)
            longitude = my_gps.convert(my_gps.saved_lon)
            satellites = my_gps.saved_sat
            target = "--TARGET SAVED--"
        oled.fill(0)
        if (latitude == None or longitude == None):
            oled.text("No Data", 0, 0)
        else:
            oled.text('Lat:'+ latitude, 0, 0)
            oled.text('Lng:'+ longitude, 0, 11)
            oled.text('Satellites:' + str(satellites), 0, 22)
            oled.text(target, 0, 44)
        oled.show()
        
        await asyncio.sleep(.5)

if __name__ == '__main__':
    try:
        btn = Pushbutton( Pin(8, Pin.IN, Pin.PULL_UP) )
        btn.press_func(handle_press)
        btn.long_func(handle_long)
        
        led = Pin(9, Pin.OUT)
        
        gps_module = UART(1, baudrate=9600, rx=Pin(44))
        my_gps = MicropyGPS()
        
        i2c = SoftI2C(scl=Pin(6), sda=Pin(5))
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)
        
        asyncio.run(main())
    finally:
        led.off()
        oled.fill(0)
        oled.show()
        print('goodbye')
