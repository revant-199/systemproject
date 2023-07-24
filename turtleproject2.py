from sketchpy import canvas
import sketchpy
obj=canvas.sketch_from_image(r"c:\Users\hp\Downloads\Patna photo.jpg")
obj.draw(threshold=100)