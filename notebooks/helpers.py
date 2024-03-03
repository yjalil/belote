import os
import shutil
import random
from pathlib import Path

def create_test_dir(data_dir, test_dir, test_split_ratio):
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    folder = Path(data_dir)
    subfolders = [subfolder for subfolder in folder.iterdir() if subfolder.is_dir()]

    for train_subfolder in subfolders :

        test_subfolder = train_subfolder.parent.parent / 'test' / train_subfolder.name
        if not os.path.exists(test_subfolder):
                os.mkdir(test_subfolder)

        files = os.listdir(train_subfolder)
        num_files_to_move = int(len(files) * test_split_ratio)
        files_to_move = random.sample(files, num_files_to_move)
        for file_name in files_to_move:
            src = os.path.join(train_subfolder, file_name)
            dst = os.path.join(test_subfolder, file_name)
            shutil.move(src, dst)



    print("Test dataset created successfully.")


def destroy_test_dir(test_dir):
    if not os.path.exists(test_dir):
        return 'Test dir does not exist'
    folder = Path(test_dir)
    subfolders = [subfolder for subfolder in folder.iterdir() if subfolder.is_dir()]

    for test_subfolder in subfolders :

        train_subfolder = test_subfolder.parent.parent / 'train' / test_subfolder.name
        if not os.path.exists(train_subfolder):
                return 'train subfolder path not found'

        files = os.listdir(test_subfolder)
        for file in files:
            src = os.path.join(test_subfolder, file)
            dst = os.path.join(train_subfolder, file)
            print(f'{src} => {dst}')
            shutil.move(src, dst)



    print("Test dataset merged to train successfully.")
