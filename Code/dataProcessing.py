import xml.etree.ElementTree as ET
import os
from os import listdir, getcwd
from os.path import join

#Get current directory. We assume we have VOCDevkit in current working directory
wd = getcwd()

#Open file to write the CSV data
csv_file = open('VOCDev.csv', 'w')
#Insert the header
csv_file.write('imageset,imagename,imagewidth,imageheight,class,difficulty,pose,truncated,xmin,xmax,ymin,ymax\n')

sets = [('train'), ('val')]
x = 0
for image_set in sets:
    image_ids = open('Datasets/VOC2007_Trainval/ImageSets/Main/%s.txt' % (image_set)).read().strip().split()
    for image_id in image_ids:
        
        #Open up the annotation file
        ann_file = open('Datasets/VOC2007_Trainval/Annotations/%s.xml' % (image_id))
        tree = ET.parse(ann_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)
        
        for obj in root.iter('object'):
            cls = obj.find('name').text
            difficult = obj.find('difficult').text
            pose = obj.find('pose').text
            truncated = obj.find('truncated').text
            xmlbox = obj.find('bndbox')
            xmin = xmlbox.find('xmin').text
            xmax = xmlbox.find('xmax').text
            ymin = xmlbox.find('ymin').text
            ymax = xmlbox.find('ymax').text
            
            csv_file.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % 
                       (image_set, image_id, w, h, cls, difficult, 
                        pose, truncated, xmin, xmax, ymin, ymax))
        ann_file.close()
csv_file.close()
