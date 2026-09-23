from skimage import io
from pyxelate import Pyx, Pal
from pathlib import Path

INFILE = "sample_scare.png"
DIR = Path(__file__).parent.resolve()

def image_to_pixel(img_path, file_out_name, downsample_by = 14, palette = 7):
    print("-" * 50)
    print("Finding IMG..")

    image = io.imread(img_path)
   
    print("IMG found, reading..")

    pyx = Pyx(factor=downsample_by, palette = palette)

    pyx.fit(image)

    print("Transforming..")
    new_image = pyx.transform(image)

    file_out = file_out_name if file_out_name else "output.png"

    io.imsave(file_out, new_image)
    print(f"Finished! Image saved to converters/output/{file_out}")
    print("-" * 50)

if __name__ == "__main__":
    i = 0
    for image_path in Path(f"{DIR}/images").glob('*.png'):
        path_string = str(image_path)
        image_to_pixel(path_string, f"{DIR}/output/pixel11-{i}.png", 14, 11)
        i+= 1
