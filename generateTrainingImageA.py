#generateTrainingImage.py

from PIL import Image

width=1000

for image in range(255):
    f=open('Training_Images/dataA'+str(image)+'.txt','a')
    imagePixels=[]
    for i in range(width):
        rowData=""
        for j in range(width):
            if i==0 and j==0:
                rowData=rowData+str(image)+" "
                imagePixels.append((image,image,image))
            else:
                rowData=rowData+str(0)+" "
                imagePixels.append((0,0,0))
        f.write(rowData+"\n")
    img = Image.new('RGB', (width, width))
    img.putdata(imagePixels)
    img.save('Training_Images/imageA'+str(image)+'.png')
    f.close()
    
