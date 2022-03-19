from PIL import Image

background = Image.open("images/test-1.png")
foreground1 = Image.open("images/test-2.png")
foreground2 = Image.open("images/test-3.png")

background.paste(foreground1, (0, 0), foreground1)
background.paste(foreground2, (0, 0), foreground2)
background.show()
background.save('result.png')
