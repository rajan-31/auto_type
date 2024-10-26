import pyautogui
import time

print("Put \"code.txt\" file in same dircetory.")

# Read the string from code.txt
with open("code.txt", "r") as file:
    string_to_type = file.read()

print("You have 5 seconds to put your cusrsor at intended place!")
# Set the delay in seconds
delay = 5

# Wait for the specified delay
time.sleep(delay)

# Type the string with a slight delay between each character to simulate human typing
for char in string_to_type.strip():
    pyautogui.typewrite(char)
    # time.sleep(0.001)  # Adjust the delay as needed