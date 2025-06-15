import time
def countdown(n):
    for x in range(n , 0 , -1):
        second=x%60
        min=int(x/60)%60
        hour=int(x/3600)
        print(f"{hour:02}:{min:02}:{second:02}")
        time.sleep(1)
    print("Time's up!")

def main():
    n=int(input("Enter the time in seconds:"))
    countdown(n)
main()