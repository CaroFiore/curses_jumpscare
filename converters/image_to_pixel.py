from skimage import io
from pyxelate import Pyx, Pal
from pathlib import Path

# Path to the current directory
FILE_PATH = Path(__file__).parent.resolve()

print("-" * 50)
print("Finding IMG..")
image = io.imread(f"{FILE_PATH}/data/sample_scare.png")
print("IMG found, reading..")

downsample_by = 14
palette = 10

pyx = Pyx(factor=downsample_by, palette = palette)

pyx.fit(image)

print("Transforming..")
new_image = pyx.transform(image)

print("Saving..")
io.imsave(f"{FILE_PATH}/data/converted.png", new_image)
print("Done!")
print("-" * 50)