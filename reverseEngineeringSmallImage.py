number_of_images=6
width=10
pixelValueShift=[]
coordinateShift=[]
proposed0=number_of_images
proposedCoordinate=width**2
for image in range(width**2):
    f=open("Training_Small_Images/translatedDataB"+str(image)+".txt","r")
    pixels=map(int,''.join(f.readlines()).replace("\n","").split(" ")[0:width**2])
    if proposed0==number_of_images:
        for i in range(number_of_images):
            if i in pixels:
                proposed0=i
                break
    position=pixels.index(proposed0)
    coordinateShift.append((position/width, position%width))
print coordinateShift
pixelValueShift[0]=proposed0
for image in range(1,number_of_images):
    f=open("Training_Small_Images/translatedDataB"+str(image)+".txt","r")
    pixels=map(int,''.join(f.readlines()).replace("\n","").split(" ")[0:width**2])
    if proposedCoordinate==(width,width):
        for i in range(number_of_images):
            if i in pixels and i!=proposed0:
                proposedCoordinate=pixels.index(i)
                break
    pixelValueShift.append(pixels[proposedCoordinate])
print pixelValueShift
