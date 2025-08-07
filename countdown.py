import time

def countdown(t: int):
    while t > 0:
        mins, sec = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, sec)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("00:00")

if __name__ == "__main__":
    countdown(61)