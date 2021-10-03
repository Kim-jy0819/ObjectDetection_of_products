# -*- coding: utf-8 -*-
"""
You can extract images from the video.
You only need to set the path of video.

@author: 김진용
"""

import numpy as np
import cv2
import random
import csv

input = 'C:/Users/charl/green/green_normal.mp4' # 동영상 경로 

cap = cv2.VideoCapture(input)

frame_total = cap.get(cv2.CAP_PROP_FRAME_COUNT)


curr_frame = 0 #영상에서 현재 프레임
frame_skip = 5 # 다음 프레임까지 스킵 수(이건 안건드는게 좋을거에요)
skip_count = 0
frame_idx=1   #데이터프레임 수
quit = 0


while (cap.isOpened() & (curr_frame < frame_total)):
    if quit:
        exit()
        
    while skip_count < frame_skip:
        success, frame = cap.read()
        skip_count = skip_count + 1
        curr_frame = curr_frame + 1
        
    skip_count=0
    success, frame = cap.read()
    
    
    if success == True:
        # Clone frame
        

        frameClone = frame.copy()
        
        curr_frame = curr_frame + 1
        
        cv2.imwrite(f'C:/Users/charl/green/green_normal/{frame_idx}.jpg', frameClone) # 이미지 저장할 폴더 경로
        frame_idx=frame_idx+1