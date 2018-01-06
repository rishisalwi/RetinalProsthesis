from PIL import Image

width=1000
import random
number_of_images=10**4
for image in range(number_of_images):
    f=open('Generated_Images/data'+str(image)+'.txt','a')
    imagePixels=[]
    for i in range(width):
        rowData=""
        for j in range(width):
            rgb=random.randrange(0,255)
            imagePixels.append((rgb,rgb,rgb))
            rowData=rowData+str(rgb)+" "
        f.write(rowData+"\n")
        
    img = Image.new('RGB', (width, width))
    img.putdata(imagePixels)
    img.save('Generated_Images/image'+str(image)+'.png')
    f.close()
    
    
             
           

