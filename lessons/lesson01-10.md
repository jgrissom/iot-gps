## Momentary Switch Driven LED - async

#### Materials
 - Assembled circuit from previous lesson
 - [async_button.py](../code/async_button.py)

#### Code
```Python
# main.py

from machine import Pin
import asyncio
from async_button import Pushbutton

def handle_press():
    print('press')
    led.on()

async def main():
    while True:
        await asyncio.sleep(.1)

if __name__ == '__main__':
    try:
        btn = Pushbutton( Pin(8, Pin.IN, Pin.PULL_UP) )
        btn.press_func(handle_press)
        
        led = Pin(9, Pin.OUT)
        asyncio.run(main())
    finally:
        led.off()
        print('goodbye')
```

#### Instructions
 - Modify the code in main.py and test in Thonny
