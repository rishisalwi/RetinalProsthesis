from PIL import Image

width=10

for image in range(width**2):
    f=open('Training_Small_Images/dataB'+str(image)+'.txt','a')
    imagePixels=[]
    for i in range(width):
        rowData=""
        for j in range(width):
            if i*width+j==image:
                rowData=rowData+str(0)+" "
                imagePixels.append((0,0,0))
            else:
                rowData=rowData+str(256)+" "
                imagePixels.append((256,256,256))
        f.write(rowData+"\n")
    img = Image.new('RGB', (width, width))
    img.putdata(imagePixels)
    img.save('Training_Small_Images/imageB'+str(image)+'.png')
    f.close()
    
