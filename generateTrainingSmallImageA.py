from PIL import Image

width=10

for image in range(6):
    f=open('Training_Small_Images/dataA'+str(image)+'.txt','a')
    imagePixels=[]
    for i in range(width):
        rowData=""
        for j in range(width):
            if i==0 and j==0:
                rowData=rowData+str(image)+" "
                imagePixels.append((image*51,image*51,image*51))
            else:
                rowData=rowData+str(0)+" "
                imagePixels.append((0,0,0))
        f.write(rowData+"\n")
    img = Image.new('RGB', (width, width))
    img.putdata(imagePixels)
    img.save('Training_Small_Images/imageA'+str(image)+'.png')
    f.close()
    
