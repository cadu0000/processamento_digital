import cv2
import os
import random

input_path = "data"
output_path = "atv3/answer_data"
os.makedirs(output_path, exist_ok=True)

def recortar_aleatorio(img, largura, altura):
    h, w = img.shape[:2]
    if largura > w or altura > h:
        return None
    x = random.randint(0, w - largura)
    y = random.randint(0, h - altura)
    return img[y:y+altura, x:x+largura]

files = [f for f in os.listdir(input_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

for fname in files:
    fpath = os.path.join(input_path, fname)
    img = cv2.imread(fpath)
    if img is None:
        continue
    cropped = recortar_aleatorio(img, 100, 100)
    if cropped is not None:
        base, ext = os.path.splitext(fname)
        out_path = os.path.join(output_path, f"{base}_crop{ext}")
        cv2.imwrite(out_path, cropped)
        print(f"{fname} → {out_path}")
