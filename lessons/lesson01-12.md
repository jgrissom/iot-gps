## Momentary Switch Driven LED - async

#### Materials
 - Assembled circuit from previous lesson
 - 128 x 64 OLED screen
 - Jumper wires
 - [ssd1306.py](../code/ssd1306.py)

#### Code
```Python
from machine import SoftI2C, Pin
import ssd1306
i2c = SoftI2C(scl=Pin(6), sda=Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text('Hello', 0, 0)
oled.show()
oled.invert(True)
oled.text('World', 0, 11)
oled.show()
oled.invert(False)
oled.fill(0)
oled.show()
```

#### Instructions
 - Enter the code using the REPL prompt

