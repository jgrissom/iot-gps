## Momentary Switch

#### Materials
 - Assembled circuit from previous lesson
 - Jumper wires
 - 10K resistor
 - Momentary switch x 1
 - Button cap x 1

#### Code
```Python
from machine import Pin
btn = Pin(8, Pin.IN, Pin.PULL_UP)
btn.value()
```

#### Instructions
 - Assemble circuit as demonstrated
 - Enter the code using the REPL prompt
 - Press and hold button
```Python
 # press and hold button
btn.value()
```
 - Release button
```Python
 # release button
btn.value()
```
