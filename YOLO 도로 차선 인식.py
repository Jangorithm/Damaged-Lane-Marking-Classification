#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import numpy as np
from collections import defaultdict
import os

track_history = defaultdict(lambda: None)  

model = YOLO("./segment_best.pt")


cap = cv2.VideoCapture("Z:/동영상/2022-08-02T06_59_40.135Z_1.mp4")
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))


save_path = "C:/Users/바탕 화면/차선/"
if not os.path.exists(save_path):
    os.makedirs(save_path)

frame_count = 0  

while True:
    ret, im0 = cap.read()
    if not ret:
        print("비디오 처리 완료")
        break

    im0 = cv2.resize(im0, (int(w / 2), int(h / 2)))
    annotator = Annotator(im0, line_width=0)
    results = model.track(im0, persist=True)

    try:
        if results[0].boxes.id is not None and results[0].masks is not None:
            masks = results[0].masks.xy
            track_ids = results[0].boxes.id.int().cpu().tolist()

            for mask, track_id in zip(masks, track_ids):
                
                if track_history[track_id] is None:
                    annotator.seg_bbox(mask=mask, mask_color=colors(track_id, True), track_label=str(track_id))

                   
                    mask_img = np.zeros(im0.shape[:2], dtype=np.uint8)
                    mask_img = cv2.fillPoly(mask_img, np.int32([mask]), 255)
                    detected_part = cv2.bitwise_and(im0, im0, mask=mask_img)

                    
                    save_filename = os.path.join(save_path, f"detected_{frame_count}_{track_id}.jpg")
                    cv2.imwrite(save_filename, detected_part)

                    
                    track_history[track_id] = mask
    except:
        pass

    cv2.imshow("instance-segmentation-object-tracking", im0)
    frame_count += 1  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

