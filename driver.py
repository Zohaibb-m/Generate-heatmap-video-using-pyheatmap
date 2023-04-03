# -*- coding: utf-8 -*-
import cv2
import math
from pyheatmap.heatmap import *

def main():
    output = "output.mp4"
    fps = 34
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output, fourcc, fps, (640, 360))  
    for i in range(238):
        url = f"Data/output{i}.txt"
        file = open(url, "r")
        sdata = file.read().split("\n")
        data = []
        for ln in sdata:
            a = ln.split(" ")
            if len(a) != 2:
                continue
            a  = [math.ceil(float(i)) for i in a]
            data.append(a)
        hm = HeatMap(data,base="BG.jpg")
        hm.clickmap(save_as="hit.png")
        hm.heatmap(save_as=f"heat.png")
        frame = cv2.imread(f"heat.png")
        # print("Generated frame")
        video_writer.write(frame)
    video_writer.release()

if __name__ == "__main__":
    main()