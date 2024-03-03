import os
import shutil
import random
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image

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
            # print(f'{src} => {dst}')
            shutil.move(src, dst)



    print("Test dataset merged to train successfully.")


def check_image_sizes(folder_path):
    # Get all subfolders and their contents
    folder = Path(folder_path)
    subfolders = [subfolder for subfolder in folder.iterdir() if subfolder.is_dir()]
    counter = 0
    # Get the size of the first image found
    first_image_size = None
    for subfolder in subfolders:
        images = list(subfolder.glob('*.jpg'))
        if images:
            with Image.open(images[0]) as img:
                first_image_size = img.size

            for image_path in images:
                with Image.open(image_path) as img:
                    if img.size != first_image_size:
                        # print(f"Image {image_path.name} in folder {subfolder.name} does not have the same size.")
                        counter += 1

    if counter != 0:
        print(f'{counter} images have a different size')
        return False
    print("All images have the same size.")
    return True


def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(len(acc))

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()


def plot_predict_samples(trained_model, test_ds):
    plt.figure(figsize=(10, 10))
    for images in test_ds.take(1):
        for i in range(9):
            ax = plt.subplot(3, 3, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(test_ds.class_names[int(np.argmax(trained_model.predict(np.expand_dims(images[i], axis=0)), axis=1))] )
            plt.axis("off")

    loss, acc = trained_model.evaluate(test_ds, verbose=2)
    print("Accuracy on new data: {:5.2f}%".format(100 * acc))
