from PIL import Image

basewidth = 383
img = Image.open('C:/Users/User/Downloads/london-g5ead6031f_1920.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
img.save('C:/Users/User/Downloads/dddtest-image-london-g5ead6031f_1920.jpeg')