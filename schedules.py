import os
import json

'''
Global dictionary with all schedules
'''
all_schedules = {}


def load_all_schedules(data_directory):
    '''
    Load all schedules from .txt files in specified directory
    '''
    print(f"Loading schedules from: {data_directory}")
    for root, dirs, files in os.walk(data_directory):
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext != ".txt":
                print(f"Skipping file: {filename}")
                continue

            full_filename = os.path.join(root, filename)
            print(f"Loading from file: {full_filename}")
            with open(full_filename) as f:
                s = json.load(f)
                all_schedules[name] = s
    print(f"Total number of schedules loaded: {len(all_schedules)}")
