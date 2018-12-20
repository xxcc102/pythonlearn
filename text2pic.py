import os
from PIL import Image
# from PIL import ImageFont, ImageDraw
# import Image, ImageFont, ImageDraw
# path = os.path.join(os.getcwd(),'1.png')
img = Image.open('1.png')
img.show()
# print(img.size)



'''
text = u"这\n是\n一\n段\n测\n试\n文\n本\n，\ntest\n 123\n。"

im = Image.new("RGB", (50, 300), (255, 255, 255))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype(os.path.join("fonts", "msyh.ttf"), 14)

dr.text((10, 5), text, font=font, fill="#000000")

im.show()
#im.save("t.png")
'''