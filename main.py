import blessed
from app.pixel import Pixel
from random import Random
from app.color import Color
from time import sleep
from converters.resizer import resize_image
from pathlib import Path

def print_pixels(pixel_list : list[Pixel], term):
    '''
    Takes a list of pixels, creates a string from those pixels and prints them to the command line.
    '''
    print_string = "".join(pixel.draw_characters() for pixel in pixel_list)
    print(print_string)
    

def main():
    '''
    Jumpscare!

    Setup steps. We create a terminal and define the terminal's width and height.
    The "el funny" of terminal drawing is that characters are twice as high as they are wide.
    For this reason, we print 2 characters at the same time, but that technically
    leaves the width of the terminal at half of itself. (Does this make sense?)
    '''

    term = blessed.Terminal()

    width = int(term.width / 2)
    height = term.height - 1

    ''' DEBUG - Creates a nice colored checkerboard pattern
    pixel_list: list[Pixel] = []
    rng = Random()
    for x in range(width): 
        for y in range(height):

            r1, r2, r3 = (rng.randint(0,255),rng.randint(0,255),rng.randint(0,255))
            color = Color(r1,r2,r3)

            #color = Color(0,0,0) if (x + y) % 2 == 0 else Color(255,255,255)

            new_pixel = Pixel(x,y,color,term)
            pixel_list.append(new_pixel)

    print_pixels(pixel_list, term)
    '''

    # ----------------------------------------------
    '''
    In the images folder, we have every frame from the gif.
    We iterate through these images and save their resized versions
    in the resized_images list.
    '''
    pathlist = Path("./converters/images/").glob('*.png')
    resized_images = []
    for i, path_path in enumerate(pathlist):
        str_path = str(path_path)
        resized_image = resize_image(str_path, width, height)
        resized_images.append(resized_image)
        #resized_image.save(f"converters/output/resized{i}.png")
    # ----------------------------------------------
    '''
    Next, we load the images, and read the rgb values on every pixel.
    We save these rgb values and colors to a pixel_list.
    Pixel_lists are lists of Pixel objects, which can later be drawn with print_pixels()

    We don't immediately print pixels as we read them, because this process is slow.
    Instead, we save all these pixels-to-be-printed to large strings first, then
    print entire frames as strings at once.

    Every pixel_list we make goes into the frame_list, which we can later iterate over.
    '''
    frame_list = []
    for img in resized_images:
        image_pixels = img.load()

        pixel_list : list[Pixel] = []
        for x in range(width):
            for y in range(height):
                pix_rgb = image_pixels[x,y]
                color = Color(pix_rgb[0], pix_rgb[1], pix_rgb[2])
                pixel_list.append(Pixel(x,y,color, term))

        frame_list.append(pixel_list)

    # ----------------------------------------------
    '''
    We clear the terminal, wait a second for suspense, then call print_pixels on every
    pixel_list we generated. Sleep time inbetween to create the animation.
    '''
    print(term.clear())
    sleep(1)

    for frame in frame_list:
        sleep(0.02)
        print_pixels(frame, term)
    # ----------------------------------------------
    '''
    Done! Now just wait for the input from the user to close the scare.
    '''
    with term.cbreak():
        key = term.inkey()
    print(f"Terminal Size: {term.width}x{term.height}")
    print(term.clear())

if __name__ == "__main__":
    main()
