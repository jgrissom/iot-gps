# main.py

from machine import Pin, UART
import asyncio
from async_button import Pushbutton

def handle_press():
    print('press')
    led.on()

def handle_long():
    print('long')
    led.off()

async def main():
    while True:
        length = gps_module.any()
        if length > 0:
            b = gps_module.read(length)
            print(b)
            break
        
        await asyncio.sleep(.5)

if __name__ == '__main__':
    try:
        btn = Pushbutton( Pin(8, Pin.IN, Pin.PULL_UP) )
        btn.press_func(handle_press)
        btn.long_func(handle_long)
        
        led = Pin(9, Pin.OUT)
        
        gps_module = UART(1, baudrate=9600, rx=Pin(44))
        
        asyncio.run(main())
    finally:
        led.off()
        print('goodbye')
