from PIL import Image, ImageSequence

im = Image.open('eagle_animated.gif')

index = 1
for frame in ImageSequence.Iterator(im):
    frame.save("eagle%d.gif" % index)
    index += 1
