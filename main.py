from PIL import Image
import os
import serial
import time
import numpy as np
board = "COM3"
bps=115200
timex=1
ser=serial.Serial(board,bps,timeout=timex)
file_dir = './bmp'
fileList = os.listdir(file_dir)
img_list = np.zeros([4385,8],dtype=np.int8)
index=0
for file_num in fileList:
    file_name = file_dir + '/' + file_num
    img = Image.open(file_name).convert("1")
    img_array = img.load()
    for y in range(8):
        a=0
        for x in range(8):
            if(img_array[x,y]==0):
                a+=0*2**(7-x)
            else:
                a+=1*2**(7-x)
        img_list[index][y]=a
    index+=1

for i in img_list:
    lis=bytes(i)
    ser.write(lis)
    time.sleep(0.05)
