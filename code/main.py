# main.py

import led

if __name__ == '__main__':
    try:
        led.blink(7)
    finally:
        print('goodbye')
