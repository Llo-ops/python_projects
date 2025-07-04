from pynput import keyboard
import time

list_confirmation_yes = ['y', 'yes', 'Yes', 'yEs', 'yeS', 'YES']
list_confirmation_no = ['n', 'no', 'No', 'nO']

def set_stopwatch():
    stopwatch_is_running = True
    start_time = time.time()

    print("The timer will start shortly, Press Enter at anytime time to stop")
    print("Timer has started!")

    def on_key_press(key):
        nonlocal stopwatch_is_running
        if key == keyboard.Key.enter:

            if current_stopwatch < 60:
                print(f"The elapsed time is: {current_stopwatch} second(s)")
            elif current_stopwatch < 3600:
                minute = int(current_stopwatch // 60)
                print(f"The elapsed time is: " + str(minute) + " minute(s)")
            else:
                hour = int(current_stopwatch // 3600)
                print(f"" + str(hour) + " hour(s) have passed.")
            stopwatch_is_running = False
            return

    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()

    while stopwatch_is_running:
        current_stopwatch = int(time.time() - start_time)
        hours = current_stopwatch // 3600
        minutes = (current_stopwatch % 3600) // 60
        seconds = current_stopwatch % 60
        time.sleep(1)
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

def main():
    stopwatch_time = input("Would you like to start the timer? (y/n): ")
    if stopwatch_time in list_confirmation_yes:
        set_stopwatch()
    elif stopwatch_time == list_confirmation_no:
        print("Alright. Thanks for using the StopWatch. Goodbye!")
        exit()

main()