#translateImage.py

width=1000
number_of_images=1000
import random
random.seed("RetinalProsthesis")
imageShuffledList=[]
for i in range(width):
    for j in range(width):
        imageShuffledList.append([i,j])
random.shuffle(imageShuffledList)
pixelShuffledList=range(255)
random.shuffle(pixelShuffledList)

for image in range(0,number_of_images):
    translatedPixels=[]
    if image%10==0:
        print image
    f=open('Training_Images/dataColumn'+str(image)+'.txt','r')
    for i in range(width):
        pixels=[]
        pixels=map(int,f.readline().split(" ")[0:width])
        pixelRow=[]
        for pixel in pixels:
            if pixel==256:
                pixelRow.append(256)
            else:
                pixelRow.append(pixelShuffledList[pixel])
        translatedPixels.append(pixelRow)
    finalTranslatedPixels=[]
    for i in range(width):
        lst=[]
        for j in range(width):
            lst.append(0)
        finalTranslatedPixels.append(lst)
    for i in range(width):
        for j in range(width):
            newPosition=imageShuffledList[i*width+j]
            finalTranslatedPixels[newPosition[0]][newPosition[1]]=translatedPixels[i][j]
    f=open('Training_Images/translatedDataColumn'+str(image)+'.txt','a')
    for i in finalTranslatedPixels:
        s=""
        for j in i:
            s=s+str(j)+" "
        f.write(s+"\n")
    f.close()

