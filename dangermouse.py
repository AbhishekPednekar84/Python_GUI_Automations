"""
This is a command line tool that takes time duration and unit of time as arguments to keep the mouse cursor moving for the specified duration. This is mainly to prevent screens from locking and to prevent a computer from being rendered as idle. 

For help, run the command - python dangermouse.py -h
Ex: run the script for 30 seconds - python dangermouse.py 30 s
Ex: run the script for 1 minute - python dangermouse.py 1 m
Ex: run the script for 5 hours - python dangermouse.py 5 h
"""

import argparse
import pyautogui
from datetime import datetime, timedelta

pyautogui.FAILSAFE = True

parser = argparse.ArgumentParser(
    prog="dangermouse", description="Keep the mouse busy for a specified duration"
)

parser.add_argument("duration", type=int, help="Amount of time for program to run")

parser.add_argument("time_unit", type=str, help="Time units - h, m, s")

args = parser.parse_args()


def run_mouse_automation(delta):
    dt = datetime.now()

    try:
        while datetime.now() < (dt + delta):
            pyautogui.moveTo(500, 500, duration=0.5)
            pyautogui.moveTo(600, 500, duration=0.5)
            pyautogui.moveTo(600, 600, duration=0.5)
            pyautogui.moveTo(500, 600, duration=0.5)
    except pyautogui.FailSafeException:
        print("User terminated the program. Bye!")
    except KeyboardInterrupt:
        print("User terminated the program. Bye!")

    print()
    print("End of program...")
    return


try:
    duration = args.duration
    assert int(duration) >= 1
except AssertionError:
    print("Durtaion should be a whole number (>= 1)")

try:
    time_unit = args.time_unit
    time_unit = time_unit.lower()
    assert time_unit == "h" or time_unit == "m" or time_unit == "s"
except AssertionError:
    print("Units of time can be either hours (h), minutes (m), or seconds (s)")


if time_unit == "h":
    t_delta = timedelta(hours=duration)
    run_mouse_automation(t_delta)
elif time_unit == "m":
    t_delta = timedelta(minutes=duration)
    run_mouse_automation(t_delta)
elif time_unit == "s":
    t_delta = timedelta(seconds=duration)
    run_mouse_automation(t_delta)
