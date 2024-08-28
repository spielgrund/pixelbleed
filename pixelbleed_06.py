
# 'pip install pillow' but import PIL
from PIL import Image
import random
import time

STEPLENGTH = 300
THRESHOLD = 100
STEPS = 5

start_time = time.time()

png_filepath = 'Fronalpstock_big (1).jpg'
image_start = Image.open(png_filepath)
image_rot = image_start.rotate(90,expand=True)
X,Y = image_rot.size
print(X,Y)
# this will print info about the PIL object
print(image_rot.format, image_rot.size, image_rot.mode)

pixel_values = list(image_rot.getdata())

THRESHOLD_MULT = THRESHOLD*3

def check_threshold(t):
    return sum(t)>THRESHOLD_MULT

# for i in range(len(pixel_values)):
#     if(check_threshold(pixel_values[i])):
#         pixel_values[i] = (0,0,0)

# for i in range(Y):
#     for j in range(X):
#         index = i*X+j
#         if(check_threshold(pixel_values[index])):
#             pixel_values [i*X+j] = (0,0,0)
i = 0
j = 0

while(i<Y):
    zeile = i*X
    
    while(j<X):
        index = zeile+j
        temp = pixel_values[index]
        r = temp[0]
        g = temp[1]
        b = temp[2]
        add=0
        if(check_threshold(temp)):
            STEPLENGTH_RANDOM = random.randint(1,STEPLENGTH)
            for _ in range(STEPLENGTH_RANDOM):
                if(_%STEPS==0):
                    if((r+1)<255):r+=1
                    if((g+1)<255):g+=1
                    if((b+1)<255):b+=1

                if(j+_>X):
                    #print("break")
                    break
                else:
                    pixel_values[index+_] = (r,g,b)
                    j+=1
                    #print(j)
            
            
        j+=1
    j=0
    i+=1

    

#print(pixel_values)

new_image = Image.new(image_rot.mode, (X, Y))

# Set the pixel values of the new image
new_image.putdata(pixel_values)

new_image = new_image.rotate(270, expand=True)


end_time = time.time()

elapsed_time = end_time - start_time
print(elapsed_time)
# Save or display the new image
#new_image.save("new_image.jpg")  # Save the new image to a file
new_image.show()  # Display the new image


