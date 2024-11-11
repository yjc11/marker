from pathlib import Path

from marker.convert import convert_single_pdf
from marker.models import load_all_models

val_dir = '/workspace/youjiachen/workspace/markdown_tester/dataset/sample'
output_dir = '/workspace/youjiachen/workspace/markdown_tester/dataset/pred/surya'
Path(output_dir).mkdir(parents=True, exist_ok=True)
model_lst = load_all_models()
for pdf_path in Path(val_dir).glob('*.pdf'):
    full_text, images, out_meta = convert_single_pdf(pdf_path, model_lst)
    oup_path = Path(output_dir, pdf_path.stem)
    oup_path.mkdir(parents=True, exist_ok=True)
    for img_name, img in images.items():
        img.save(oup_path / img_name)

    with open(oup_path / f"{pdf_path.stem}.md", "w") as f:
        f.write(full_text)
