import os
import numpy as np
import cv2

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if any([filename.endswith(x) for x in ['.JPG', '.jpg']]):
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                cv2.imshow("images", img)
                if cv2.waitKey(1) == 27:
                    break  # esc to quit
    return images

folders = [
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___healthy',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold'
]

for folder in folders:
    images = load_images_from_folder("C:/PLANT/PlantVillage-Dataset/raw/grayscale/" + folder)
    # your code that does something with the return images goes here