from skimage import io
from pyxelate import Pyx
from pathlib import Path

INFILE = "sample_scare.png"
DIR = Path(__file__).parent.resolve()

def image_to_pixel(img, *file_out_name, downsample_by = 14, palette = 7):
    print("-" * 50)
    print("Finding IMG..")

    #image = io.imread(f"{DIR}/input/{INFILE}")
    image = img
    print("IMG found, reading..")

    downsample_by = 14
    palette = 7

    pyx = Pyx(factor=downsample_by, palette = palette)

    pyx.fit(image)

    print("Transforming..")
    new_image = pyx.transform(image)

    print("Saving..")

    file_out = file_out_name if file_out_name else "output.png"

    io.imsave(f"{DIR}/output/{file_out}", new_image)
    print(f"Finished! Image saved to converters/output/{file_out}")
    print("-" * 50)

if __name__ == "__main__":
    pass # Todo: next steps here
