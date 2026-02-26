"""
Script to press the Num Lock key every 10 seconds indefinitely.
Press Ctrl+C to stop the script.
"""

import time
from pynput.keyboard import Key, Controller

def main():
    keyboard = Controller()
    
    print("Starting Num Lock key press automation...")
    print("The Num Lock key will be pressed every 10 seconds.")
    print("Press Ctrl+C to stop the script.\n")
    
    try:
        counter = 1
        while True:
            # Press and release the Num Lock key
            keyboard.press(Key.num_lock)
            keyboard.release(Key.num_lock)
            
            print(f"Num Lock key pressed (Count: {counter})")
            counter += 1
            
            # Wait for 10 seconds
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("\n\nScript stopped by user.")
        print(f"Total presses: {counter - 1}")

if __name__ == "__main__":
    main()
