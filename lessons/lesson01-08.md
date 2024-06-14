## Momentary Switch Driven LED

#### Materials
 - Assembled circuit from previous lesson

#### Code
```Python
from machine import Pin
from time import sleep
btn = Pin(8, Pin.IN, Pin.PULL_UP)
led = Pin(9, Pin.OUT)
while True:
    led.value(btn.value())
    sleep(.01)
```

#### Instructions
 - Enter the code using the REPL prompt
