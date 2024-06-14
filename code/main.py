# main.py

from machine import Pin
import asyncio

async def main():
    while True:
        led.value(btn.value())
        await asyncio.sleep(.1)

if __name__ == '__main__':
    try:
        btn = Pin(8, Pin.IN, Pin.PULL_UP)
        led = Pin(9, Pin.OUT)
        asyncio.run(main())
    finally:
        print('goodbye')
