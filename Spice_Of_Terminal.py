from types import SimpleNamespace

FG = SimpleNamespace()
BG = SimpleNamespace()

ANSII_Codes = {
    "Black": 0,
    "Red": 1,
    "Green": 2,
    "Yellow": 3,
    "Blue": 4,
    "Magenta": 5,
    "Cyan": 6,
    "White": 7,
}

for key, value in ANSII_Codes.items():
    # Set standard codes
    setattr(FG, key, f"\033[{30+value}m")
    setattr(BG, key, f"\033[{40+value}m")
    # Set bright codes
    setattr(FG, f"Bright{key}", f"\033[{90+value}m")
    setattr(BG, f"Bright{key}", f"\033[{100+value}m")
# Clear will clear both FG and BG, there is no single clear
FG.Clear = "\033[0m"
BG.Clear = "\033[0m"
# Set 8-bit codes
FG.rgb = lambda r,g,b: f"\033[38;2;{r};{g};{b}m"
BG.rgb = lambda r,g,b: f"\033[48;2;{r};{g};{b}m"