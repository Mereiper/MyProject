import time

print("Welcome to basic timer!")
print(f"Now -> Day: {time.strftime('%A')}, Month: {time.strftime('%B')}, Year: {time.strftime('%Y')}")

duration = input("Enter the time in seconds: ")
while True:
    if duration.isdigit():
        break
    else:
        duration = input("Please enter a digit: ")

for x in range(int(duration), 0, -1):
    sec = x % 60
    minute = int(x / 60) % 60
    hr = int(x / 3600)
    print(f"{hr:02}:{minute:02}:{sec:02}")
    time.sleep(1)
print(f"time is over, now time: {time.strftime('%X')}")