from PIL import Image


image = Image.open('images/test_images/bcbb.jpg')
print(image.size)
image.thumbnail((400, 400))
image.save('images/test_images/bcbb_thumb.jpg')
image.show()

print(image.size) # Output: (400, 258)