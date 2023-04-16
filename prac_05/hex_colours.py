import json
import requests

URL = "http://www.color-hex.com/color-names.html"

COLOR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aqua": "#00ffff", "aquamarine": "#7fffd4",
          "azure": "#f0ffff", "beige": "#f5f5dc", "bisque": "#ffe4c4", "black": "#000000",
          "blanchedalmond": "#ffebcd", "blue": "#0000ff"}
print(COLOR_CODES)
color_name = input("Enter a color name: ").lower()
while color_name != " ":
    print(f"The code for {color_name} is {COLOR_CODES[color_name]}")
    color_name = input("Enter a color name: ").lower()
