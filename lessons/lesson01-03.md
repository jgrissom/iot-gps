## Blink LED Using Indefinite Repetition

#### Materials
 - Assembled circuit from previous lesson

#### Code A
```Python
from machine import Pin
from time import sleep
led = Pin(9, Pin.OUT)
while True:
    led.on()
    sleep(.5)
    led.off()
    sleep(.5)
```

#### Code B
```Python
    led.off()
```

#### Instructions
 - Enter the code A using the REPL prompt
 - Press Enter twice to run
 - Press Ctrl + C to quit
 - If needed turn the LED off using code B
