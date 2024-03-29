from PIL import Image
import pyperclip
import colorsys 
import requests
import io
import test #See scratchcloudvariables on my github I call the file test
import time

cloud = True
hues = "" #See hsv contains first digit of a hues
sats = ""
vals = ""
hues2 = "" #contains second digit
sats2 = ""
vals2 = ""
def new_image():
    
    global hues
    global hues2
    global sats
    global sats2
    global vals
    global vals2

    with io.BytesIO(requests.get("https://source.unsplash.com/48x48").content) as a: #gets image's bytes puts it in a io and opens it using PIL
        global img
        img  = Image.open(a)
        img = img.copy()
        
    rgbimage = img.convert("RGB")
    rgbimage.show()
    output = ""
    i = 1 
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            colorset = rgbimage.getpixel((x,y)) #https://stackoverflow.com/questions/11064786/get-pixels-rgb-using-pil
            colorset = [a/255.0 for a in colorset] 
            colorset = [str(round(a * 100)) for a in colorsys.rgb_to_hsv(*colorset)] #https://stackoverflow.com/questions/2612361/convert-rgb-values-to-equivalent-hsv-values-using-python
            #multiplied by hundred to get number instead of decimal
            for index, value in enumerate(colorset):
                if len(value) == 3:
                    colorset[index] = "99" #set a value that is equal to hundred to 99 because it has two digits
                elif len(value) == 1:
                    colorset[index] = "0" + colorset[index] #set a value that has only one digit to that plus zero to make two digits

            if cloud: 
                hues = hues + colorset[0][0] #see above comments
                sats = sats + colorset[1][0]
                vals = vals + colorset[2][0]
                hues2 = hues2 + colorset[0][1]
                sats2 = sats2 + colorset[1][1]
                vals2 = vals2 + colorset[2][1] 

    if cloud:
        session.SetCloudVar("Which type and other information", 1) #tells the scratch program what information we are sending
        for i in range(9):
            time.sleep(0.1)
            session.SetCloudVar(str(i + 1),hues[i * 256:256 if i == 0 else (i + 1) * 256]) #for each cloud variable it adds 256th of hues
            time.sleep(0.1)
        session.SetCloudVar("Which type and other information", 0.1) #tells the scratch program that the variables are ready to read
        time.sleep(0.3) 
        session.SetCloudVar("Which type and other information", 2)
        for i in range(9):
            time.sleep(0.1)
            session.SetCloudVar(str(i + 1),sats[i * 256:256 if i == 0 else (i + 1) * 256]) 
            time.sleep(0.1)
        session.SetCloudVar("Which type and other information", 0.1)
        time.sleep(0.3)
        session.SetCloudVar("Which type and other information", 3)
        for i in range(9):
            time.sleep(0.1)
            session.SetCloudVar(str(i + 1), vals[i * 256:256 if i == 0 else (i + 1) * 256])
            time.sleep(0.1)
        session.SetCloudVar("Which type and other information", 0.1)
        time.sleep(0.3)    
        session.SetCloudVar("Which type and other information", 4)
        for i in range(9):
            time.sleep(0.1)
            session.SetCloudVar(str(i + 1),hues2[i * 256:256 if i == 0 else (i + 1) * 256]) 
            time.sleep(0.1)
        session.SetCloudVar("Which type and other information", 0.1)
        time.sleep(0.3)
        session.SetCloudVar("Which type and other information", 5)
        for i in range(9):
            time.sleep(0.1)
            session.SetCloudVar(str(i + 1),sats2[i * 256:256 if i == 0 else (i + 1) * 256])
            time.sleep(0.1)
        session.SetCloudVar("Which type and other information", 0.1)
        time.sleep(0.3)
        session.SetCloudVar("Which type and other information", 6)
        for i in range(9):
            time.sleep(0.1)
            session.SetCloudVar(str(i + 1), vals2[i * 256:256 if i == 0 else (i + 1) * 256])    
            time.sleep(0.1)
        session.SetCloudVar("Which type and other information", 0.1)
        time.sleep(0.3)
        session.SetCloudVar("Which type and other information", 0)

if cloud:
    session = test.ScratchSession() 
new_image()
