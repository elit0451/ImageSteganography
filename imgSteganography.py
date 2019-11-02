from PIL import Image 

im = Image.open("Stego.png")

width, height = im.size
character = []
msg = []
foundMsgEnd = False

for y in range(height):
    for x in range(width):
        r,g,b,a = im.getpixel((x,y))
        lastBit = bin(b)[-1]
        character.append(lastBit)
        if(len(character) == 8):
        	character.reverse()
        	int_char = int("".join(str(x) for x in character), 2)
        	if(int_char == 0):
        		foundMsgEnd = True
        		break
        	ascii_char = chr(int_char) 
        	msg.append(ascii_char)
        	character = []
    if(foundMsgEnd == True):
        break
print("".join(msg))