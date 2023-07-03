#This file should be executed before traning the CNN
import os
import shutil
import random
import glob

shutil.rmtree('FineData')    
os.makedirs('FineData')
os.makedirs('FineData/train/Cyclone')
os.makedirs('FineData/train/Earthquake')
os.makedirs('FineData/train/Flood')
os.makedirs('FineData/train/Wildfire')

os.makedirs('FineData/valid/Cyclone')
os.makedirs('FineData/valid/Earthquake')
os.makedirs('FineData/valid/Flood')
os.makedirs('FineData/valid/Wildfire')

shutil.copytree('Disaster','buffer')

nt=600
for c in random.sample(glob.glob('buffer/Cyclone/*'),int(nt)):
    shutil.move(c,'FineData/train/Cyclone')
for c in random.sample(glob.glob('buffer/Earthquake/*'),int(nt)):
    shutil.move(c,'FineData/train/Earthquake')
for c in random.sample(glob.glob('buffer/Flood/*'),int(nt)):
    shutil.move(c,'FineData/train/Flood')
for c in random.sample(glob.glob('buffer/Wildfire/*'),int(nt)):
    shutil.move(c,'FineData/train/Wildfire')

nv=100
for c in random.sample(glob.glob('buffer/Cyclone/*'),int(nv)):
    shutil.move(c,'FineData/valid/Cyclone')
for c in random.sample(glob.glob('buffer/Earthquake/*'),int(nv)):
    shutil.move(c,'FineData/valid/Earthquake')
for c in random.sample(glob.glob('buffer/Flood/*'),int(nv)):
    shutil.move(c,'FineData/valid/Flood')
for c in random.sample(glob.glob('buffer/Wildfire/*'),int(nv)):
    shutil.move(c,'FineData/valid/Wildfire')

shutil.rmtree('buffer')  

