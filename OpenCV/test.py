from PIL import Image

im = Image.open("visa_org.jpg")
im.save("visa.jpg", quality=70, optimize=True)
