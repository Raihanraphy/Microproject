import time
import os

while True:
    now = time.strftime("%H:%M:%S")
    os.system('cls' if os.name == 'nt' else 'clear')  # clear screen
    print("🕒 Digital Clock 🕒\n")
    print(f"     {now}     ")
    print("\nPress Ctrl+C to stop")
    time.sleep(1)
