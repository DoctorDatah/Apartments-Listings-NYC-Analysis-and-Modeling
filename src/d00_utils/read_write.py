import os
import sys
import numpy as np 
import pandas as pd 


PROJECT_ROOT = os.getcwd()
DATA_DIR = os.path.join(PROJECT_ROOT, "data")


def create_data_sub_dir(dir_name):
    try:
        sub_dir = os.path.join(DATA_DIR, dir_name)
        if(os.path.isdir(sub_dir) is False):
            os.makedirs(sub_dir)
            print('Dir Created')
        else:
            print('Dir already exist.')
    except:
        print('Something went wrong')

        
def save_data_file(dir_name, file_name, data):
    try:
        sub_dir = os.path.join(dir_name, file_name)
        full_path = os.path.join(DATA_DIR, sub_dir)
        data.to_csv(full_path, index = False)
        print('File saved.')
    except:
        print('Something went wrong')