from PIL import Image
from pathlib import Path

INPUT_FILE = "jumpscare.gif"

im = Image.open(f"{Path(__file__).parent.resolve()}/input/{INPUT_FILE}")

i = 0
while True:
    try:
        im.save(f"test{i}.png")
        im.seek(im.tell() +1)
        i+=1
        
    except EOFError:
        print("End of gif reached, finished!")
