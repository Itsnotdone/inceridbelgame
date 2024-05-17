import os

print("// HINT: C:/Program Files (x86)/Steam/steam.exe")
steam_path = input("Enter steam executable path: ")

try:
    os.system(f"{steam_path} -applaunch 394360")
except:
    print("Could not find HEARTS OF IRON 4 installed, plz install it imediately, if not u will be destroyed now, good luck :OOOOOO")