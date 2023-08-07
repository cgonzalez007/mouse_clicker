# region imports
import sys
import win32api
import win32con
import time
from datetime import datetime
# endregion

# region functions


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def right_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)


def right_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

# endregion

# region prompts


def get_interval():
    response = ""
    while not response.isnumeric():
        response = input("Please enter the time interval to use in seconds: ")
    return int(response)

# endregion

# region main


def main():
    input("Minimize/close windows you do not want to accidently click on. Press ENTER when this is completed.")
    interval = get_interval()
    print("Press CTRL+C to exit.")
    while True:
        print(f"{datetime.now()}|Waiting...")
        time.sleep(interval)
        print("Clicking!")
        click()


if __name__ == "__main__":
    main()

# endregion
