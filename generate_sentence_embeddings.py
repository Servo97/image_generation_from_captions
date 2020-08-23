import json
import os
from os.path import join, isfile
import re
import numpy as np
import pickle
import argparse
import skipthoughts
import h5py
import time

def save_caption_vectors(data_dir):
    img_dir = join(data_dir, "flowers/jpg")
    image_files = [f for f in os.listdir(img_dir) if "jpg" in f]
    print(image_files[300:400])
    print(len(image_files))
    image_captions = {img_file: [] for img_file in image_files}
    
    caption_dir = join(data_dir, "flowers/text_c10")
    class_dirs = []
    for i in range(1,103):
        class_dir_name = "class_%.5d"%(i)
        class_dirs.append(join(caption_dir,class_dir_name))
    
    for class_dir in class_dirs:
        caption_files = [f for f in os.listdir(class_dir) if "txt" in f]
        for cap_file in caption_files:
            with open(join(class_dir,cap_file)) as f:
                captions = f.read().split("\n")
            img_file = cap_file[0:11] + ".jpg"
            #5 captions per image
            image_captions[img_file] += [cap for cap in captions if len(cap)>0][0:5]
    
    print(len(captions))
    
    model = skipthoughts.load_model()
    encoded_captions = {}
    for i,img in enumerate(image_captions):
        st = time.time()
        encoded_captions[img] = skipthoughts.encode(model,image_captions[img])
        print(i,len(image_captions),img)
        print("Seconds", time.time() - st)
        
    h = h5py.File(join(data_dir,"flower_tv.hdf5"))
    for key in encoded_captions:
        h.create_dataset(key, data = encoded_captions[key])
    h.close()

save_caption_vectors('Data')