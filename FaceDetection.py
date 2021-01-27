import cv2
import os
import json
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("P")
    args = parser.parse_args()
    return args
def main():
    args = parse_args()
    json_list = []
    dataDir = str(args.P)
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')   
    scaleFactor = 1.1                                                                                        
    minNeighbors = 1                                                                                                   
    FFlag = 1                                                                                                
    images = []
    for file in os.listdir(dataDir):
        file = file.lower()
        if file.endswith('.jpg'):
            images.append(dataDir + file)
    if images:
       
        
        for image in images:
            
            img = cv2.imread(image)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbors)
            
            if (FFlag):
                
                for (x,y,w,h) in faces:
                    element_1 = {"iname": image.replace(dataDir,''), "bbox": [int(x), int(y), int(w), int(h)]}
                    json_list.append(element_1)
                    
    output_json = "results.json"
    #dump json_list to result.json
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
 
    with open(os.path.join(__location__, output_json), 'w') as f:
        json.dump(json_list, f)
        
main()
