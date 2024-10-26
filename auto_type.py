#!/usr/bin/env python3

import pyautogui
import time
import sys

print('Put "code.txt" file in the same directory.')

try:
    # Try to open and read "code.txt"
    with open("code.txt", "r") as file:
        string_to_type = file.read().strip()
except FileNotFoundError:
    print("Error: 'code.txt' file not found. Please ensure it is in the same directory as this script.")
    sys.exit(1)  # Exit the program if the file is missing
except PermissionError:
    print("Error: Permission denied. Check read permissions for 'code.txt'.")
    sys.exit(1)

print("You have 5 seconds to put your cursor at the intended place!")
delay = 5

# Wait for the specified delay
time.sleep(delay)

try:
    # Type the string with a delay to simulate human typing
    for char in string_to_type:
        pyautogui.typewrite(char)
        # Optional delay to slow down typing
        # time.sleep(0.001)  # Adjust the delay as needed
except pyautogui.FailSafeException:
    print("Typing interrupted by moving the mouse to a corner.")
except KeyboardInterrupt:
    print("\nTyping interrupted manually.")
finally:
    print("\nTyping complete or interrupted.")
