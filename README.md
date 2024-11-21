# Spice-Of-Terminal

Install with
python -m pip install git+https://github.com/Aethelryth/Spice_Of_Terminal.git#egg=Spice_Of_Terminal

A simple python library to add ANSI escape codes to add colo(u)r to text

This supports foreground and background, for 3-bit, 4-bit and 8-bit colo(u)rs.

An example use case:
```py
from Spice_Of_Terminal import FG, BG

print(f"{FG.Green}3-Bit colo(u)r is great, {FG.BrightGreen}and so is 4-bit.{FG.Clear}")
print(f"{FG.rgb(0,200,100)}But I prefer the full colo(u)r spectrum{FG.Clear}")
```

