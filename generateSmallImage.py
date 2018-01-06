from PIL import Image

width=10
import random
number_of_images=10
for image in range(number_of_images):
    f=open('Sample_Images/data'+str(image)+'.txt','a')
    imagePixels=[]
    for i in range(width):
        rowData=""
        for j in range(width):
            rgb=random.randrange(0,6)
            imagePixels.append((rgb*51,rgb*51,rgb*51))
            rowData=rowData+str(rgb)+" "
        f.write(rowData+"\n")
        
    img = Image.new('RGB', (width, width))
    img.putdata(imagePixels)
    img.save('Sample_Images/image'+str(image)+'.png')
    f.close()
    
    
             
           

