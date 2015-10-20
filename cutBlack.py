# -*- coding: utf-8 -*
__author__ = 'administer'
import os
import subprocess
import csv

roi_path = 'F:\\Tools\\ROI\\'
source_image_path = 'E:\\workFile\\ROI2\\ROI\\roitestcase\\'
finish_image_path = 'E:\\workFile\\finish\\'
date_path = r'C:\\Users\\administer\\Desktop\\datas2.csv'


def cut_black():
    with open(date_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:

                cmd = [os.path.join(roi_path, 'ROI2'),'-s2', os.path.join(source_image_path, row[0]), os.path.join(finish_image_path, row[0]), row[1], row[2], row[3], row[4]]
                
                child = subprocess.Popen(cmd, cwd=roi_path)
                child.wait()
            except:
                print "error"
           

if __name__ == "__main__":
    cut_black()