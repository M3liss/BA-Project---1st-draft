import os
global dataset_labels
global detection_labels

dataset_labels =  ['ball', 'hand', 'both', 'nothing']
detection_labels = ['ball', 'hand']
if not os.path.exists('images'):
    os.mkdir('images')
if not os.path.exists('annotations'):
    os.mkdir('annotations')
for label in dataset_labels:
    if not os.path.exists(f'dataset/{label}'):
        os.mkdir(f'dataset/{label}')
        print(f"{label} directory created")

def add_dataset(new_label):
    dataset_labels.append(new_label)
    detection_labels.append(new_label)