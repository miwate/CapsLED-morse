import time
import keyboard

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

dot_duration = 0.1
dash_duration = 0.3
space_duration = 0.7

def convert_to_morse(text):
    morse_text = ""
    for char in text.upper():
        if char in morse_code:
            morse_text += morse_code[char] + " "
    return morse_text

def control_caps_lock_led(state):
    if state:
        keyboard.press('caps lock')
        keyboard.release('caps lock')
    else:
        keyboard.press('caps lock')
        keyboard.release('caps lock')

def calculate_time(text):
    morse_text = convert_to_morse(text)

    total_time = 0
    for morse_char in morse_text:
        if morse_char == '.':
            total_time += dot_duration
        elif morse_char == '-':
            total_time += dash_duration
        elif morse_char == ' ':
            total_time += space_duration

        total_time += dot_duration

    return round(total_time, 1)

with open('prompt.txt', 'r') as file:
    text = file.read()

print("Original Text: ", text)

morse_text = convert_to_morse(text)

print("Morse Code: ", morse_text)

estimated_time = calculate_time(text)
print("Estimated Time: ", estimated_time, " seconds")

keyboard.press('caps lock')

for morse_char in morse_text:
    if morse_char == '.':
        control_caps_lock_led(True)
        time.sleep(dot_duration)
        control_caps_lock_led(False)
        time.sleep(dot_duration)
    elif morse_char == '-':
        control_caps_lock_led(True)
        time.sleep(dash_duration)
        control_caps_lock_led(False)
        time.sleep(dot_duration)
    elif morse_char == ' ':
        time.sleep(space_duration)

control_caps_lock_led(False)
keyboard.press('caps lock')
keyboard.release('caps lock')

print("Finished")
