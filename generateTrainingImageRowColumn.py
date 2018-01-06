from PIL import Image

width=1000

for image in range(width):
    f=open('Training_Images/dataRow'+str(image)+'.txt','a')
    imagePixels=[]
    for i in range(width):
        rowData=""
        for j in range(width):
            if i==image:
                rowData=rowData+str(0)+" "
                imagePixels.append((0,0,0))
            else:
                rowData=rowData+str(256)+" "
                imagePixels.append((256,256,256))
        f.write(rowData+"\n")
    img = Image.new('RGB', (width, width))
    img.putdata(imagePixels)
    img.save('Training_Images/imageRow'+str(image)+'.png')
    f.close()
for image in range(width):
    f=open('Training_Images/dataColumn'+str(image)+'.txt','a')
    imagePixels=[]
    for i in range(width):
        rowData=""
        for j in range(width):
            if j==image:
                rowData=rowData+str(0)+" "
                imagePixels.append((0,0,0))
            else:
                rowData=rowData+str(256)+" "
                imagePixels.append((256,256,256))
        f.write(rowData+"\n")
    img = Image.new('RGB', (width, width))
    img.putdata(imagePixels)
    img.save('Training_Images/imageColumn'+str(image)+'.png')
    f.close()
