import cv2
import os

input_path = "data"

output_path = "atv2/answer_data"
os.makedirs(output_path, exist_ok=True)

files = [f for f in os.listdir(input_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

for fname in files:
    fpath = os.path.join(input_path, fname)

    img_bgr = cv2.imread(fpath)

    if img_bgr is None:
        print(f"Erro ao carregar {fname}")
        continue

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    base, ext = os.path.splitext(fname)
    out_bgr = os.path.join(output_path, f"{base}_bgr{ext}")
    out_rgb = os.path.join(output_path, f"{base}_rgb{ext}")
    out_gray = os.path.join(output_path, f"{base}_gray{ext}")

    cv2.imwrite(out_bgr, img_bgr)
    cv2.imwrite(out_rgb, img_rgb)
    cv2.imwrite(out_gray, img_gray)

    print(f"Processado: {fname} → {out_bgr}, {out_rgb}, {out_gray}")
