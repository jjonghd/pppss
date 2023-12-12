from fileinput import close
import cv2    
import numpy as np
import os
import shutil
from tkinter import*
from tkinter import filedialog

root = Tk()
root.title("사진 분류 프로그램")
root.geometry("540x480")




def take_picture():
    picture = cv2.VideoCapture(0) 

    capNum = int (0)  
    while True:  
        ret, frame = picture.read() 
        
        if os.path.exists('picture000.png') and os.path.isfile('picture000.png'):
            os.remove('picture000.png') 

        cv2.imshow("camera", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('p'):
            
            
            cv2.imwrite('picture%03d.png' % capNum,frame) 
            capNum += 1   

            break;

        if cv2.waitKey(1) == ord('1'): 
            img_captured = cv2.imwrite('picture%03d.png' % capNum, frame);
            capNum += 1   
        
        if cv2.waitKey(1) == ord('s'):
            break;

    picture.release()
    cv2.destroyAllWindows()
    
    image1_path = "C:/Users/전종현/Desktop/project"
    file_list = os.listdir(image1_path)
    file_list_png=[file for file in file_list if file.endswith(".png")]

    image2_path = 'picture000.png'

    Delete("C:/Users/전종현/Desktop/pp")

    for i in file_list_png:
        similarity_score = compare_images(i, image2_path)
        print(f"이미지의 유사도: {similarity_score}")
        capNum1 = int(0)
        if (similarity_score < 1 ):
            shutil.move(i, "C:/Users/전종현/Desktop/pp")
            
    shutil.move('picture000.png', "C:/Users/전종현/Desktop/pp")

def compare_images(i, image2_path):
    
    image1 = cv2.imread(i)
    image2 = cv2.imread(image2_path)
    
    image1 = cv2.resize(image1, (300,300))
    image2 = cv2.resize(image2, (300,300))
    
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])
    
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    
    return similarity

def Delete(filepath):
    if os.path.exists(filepath):
        for file in os.scandir(filepath):
            os.remove(file.path)
            
def take_picture2():
    picture = cv2.VideoCapture(0) 

    capNum = int (0)  
    while True:  
        ret, frame = picture.read()  

        cv2.imshow("camera", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('p'):

            cv2.imwrite('picture%03d.png' % capNum,frame) 
            capNum += 1   

            break;

        if cv2.waitKey(1) == ord('1'): 
            img_captured = cv2.imwrite('picture%03d.png' % capNum, frame);
            capNum += 1   
        
        if cv2.waitKey(1) == ord('s'):
            break;

    picture.release()
    cv2.destroyAllWindows()
    

def openFile():
    os.startfile("C:/Users/전종현/Desktop/pp")
    
  



        
pbutton = Button(root, text = "사진 찍기", command = take_picture)
pbutton.pack()

open_button = Button(root, text="파일 열기", command = openFile)
open_button.place(x=300, y=300)

pbutton2 = Button(root, text = ".", command = take_picture2)
pbutton2.place(x=50, y=50)

label1 = Label(root, text = "p, 사진찍기")
label1.place(x=150, y=75) 

label2 = Label(root, text = "s, 사진을 찍어주는 창 종료")
label2.place(x=150, y=100) 


root.mainloop()





