## MicroPython Driven LED Circuit

#### Materials
 - Assembled circuit from previous lessone

#### Code A
```Python
from machine import Pin
led = Pin(9, Pin.OUT)
led.on()
```

#### Code B
```Python
led.off()
```

#### Instructions
 - Connect LED cathod to MCU pin GPIO9
 - Connect MCU to computer using USB connector
 - Launch Thonny
 - Update to Micropython 1.23.0 ([micropython.org](https://micropython.org/))
 - Connect to MCU - Run - Select Interpreter ...
 - Show the MicroPython REPL (Read Evaluate Print Loop) prompt - View - Focus Shell
 - Enter the code A using the REPL prompt
 - Enter the code B using the REPL prompt
 