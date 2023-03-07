import face_recognition
import numpy as np
from PIL import Image, ImageDraw
import os
import pandas as pd

import pathlib
from utils import unpacking

try:   
    ROOT = pathlib.Path(__file__)
except NameError:
    ROOT = pathlib.Path('.')
BASE = ROOT.parent

IMAGE_FOLDER = BASE / 'dataset' / 'Images'
OUTPUT_FOLDER = BASE / 'dataset' / 'Test_Output'

with open((BASE / 'known_face_encodings.pkl').as_posix(), 'rb') as f:
    known_face_encodings = unpacking(f.read())

with open((BASE / 'known_face_names.pkl').as_posix(), 'rb') as f:
    known_face_names = unpacking(f.read())
    
test_csv_path = (BASE / 'dataset' / 'Test.csv').absolute().as_posix()
test_df = pd.read_csv(test_csv_path)

def get_face_recognition(image_path):
    # Load an image with an unknown face
    unknown_image = face_recognition.load_image_file(image_path)
    # Find all the faces and face encodings in the unknown image
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    # Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
    # See http://pillow.readthedocs.io/ for more about PIL/Pillow
    pil_image = Image.fromarray(unknown_image)
    # Create a Pillow ImageDraw Draw instance to draw with
    draw = ImageDraw.Draw(pil_image)
    
    # Loop through each face found in the unknown image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    
        name = "Unknown"
    
        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
    
        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
    
        # Draw a label with a name below the face
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

    # Remove the drawing library from memory as per the Pillow docs
    del draw
    return pil_image


for label in sorted(test_df['label'].unique()):
    label_df = test_df[test_df['label']==label]
    for img_name in label_df['id']:
        image_path = (IMAGE_FOLDER / label / img_name).absolute().as_posix()
        pil_image = get_face_recognition(image_path)
        os.makedirs((OUTPUT_FOLDER / label).absolute().as_posix(), exist_ok=True)
        output_image_path = (OUTPUT_FOLDER / label / img_name).absolute().as_posix()
        pil_image.save(output_image_path)