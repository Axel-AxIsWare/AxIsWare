from machine import Pin, Timer
import time

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                  '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' '}

led_pin = Pin(25, Pin.OUT)

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += ' '
    return morse_code

def flash_morse_code(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            led_pin.on()
            time.sleep(0.2)
            led_pin.off()
            time.sleep(0.2)
        elif symbol == '-':
            led_pin.on()
            time.sleep(0.6)
            led_pin.off()
            time.sleep(0.2)
        elif symbol == ' ':
            time.sleep(0.4)

text_to_translate = "Morse translator"
morse_translation = text_to_morse(text_to_translate)
flash_morse_code(morse_translation)
