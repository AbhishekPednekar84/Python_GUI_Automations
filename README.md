## GUI automations using `pyauogui`

1. **dangermouse-py** :mouse: - moves the mouse cursor around fixed coordinates for a specified amount of time, This is particularly useful if you need to be away from your computer but keep it unlocked. The script accepts two parameters - *amount of time* and *unit of time* (hours, minutes or seconds). For example, the parameters `1 m` will run the script for 1 minute or `3 h` will run the script for 3 hours. To stop the script, either use `Ctrl + C` / `Cmd + C` or drag the cursor to the top left of the screen.

```
usage: dangermouse [-h] duration time_unit

Keep the mouse busy for a specified duration

positional arguments:
  duration    Amount of time for program to run
  time_unit   Time units - h, m, s
```
**Example** - `python dangermouse.py 30 s` will run the script for 30 seconds
