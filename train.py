import face_recognition
import pathlib
from utils import packing, unpacking
import pandas as pd

try:   
    ROOT = pathlib.Path(__file__)
except NameError:
    ROOT = pathlib.Path('.')
BASE = ROOT.parent

IMAGE_FOLDER = BASE / 'dataset' / 'Images'

train_csv_path = (BASE / 'dataset' / 'Train.csv').absolute().as_posix()

train_df = pd.read_csv(train_csv_path)

# This is an example of running face recognition on a single image
# and drawing a box around each person that was identified.

# Load a sample picture and learn how to recognize it.
known_face_encodings = []
known_face_names = []
total_label_number = len(train_df['label'].unique())
for num, label in enumerate(sorted(train_df['label'].unique())):
    print()
    print("{0}/{1} completed".format(num+1, total_label_number))
    print("{} label started".format(label))
    label_df = train_df[train_df['label']==label]
    for enum, img_name in enumerate(label_df['id']):
        print("{0}/{1} completed...".format(enum+1, len(label_df)))
        image_path = (IMAGE_FOLDER / label / img_name).absolute().as_posix()
        image = face_recognition.load_image_file(image_path)
        if face_recognition.face_encodings(image):
            face_encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(face_encoding)
            known_face_names.append(label)
        else:
            print("{}/{} have some problem".format(label, img_name))

with open((BASE / 'known_face_encodings.pkl').as_posix(), 'wb') as f:
    f.write(packing(known_face_encodings))

with open((BASE / 'known_face_names.pkl').as_posix(), 'wb') as f:
    f.write(packing(known_face_names))

with open((BASE / 'known_face_encodings.pkl').as_posix(), 'rb') as f:
    _ = unpacking(f.read())
    # print(_)

with open((BASE / 'known_face_names.pkl').as_posix(), 'rb') as f:
    _ = unpacking(f.read())
    # print(_)

print('Learned encoding for', len(known_face_encodings), 'images.')