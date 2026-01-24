from PIL import Image
import torch
from transformers import AutoModelForCausalLM, AutoProcessor

model_path = "PaddlePaddle/PaddleOCR-VL"
image_path = "Image_1.jpg"
task = "ocr"  # 'ocr' | 'table' | 'chart' | 'formula'

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

PROMPTS = {
    "ocr": "OCR:",
    "table": "Table Recognition:",
    "formula": "Formula Recognition:",
    "chart": "Chart Recognition:",
}

image = Image.open(image_path).convert("RGB")

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    torch_dtype=torch.float16
).to(DEVICE).eval()

processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

print("Running inference...")
task  = "OCR: Extract all visible text from the image in reading order."
with torch.no_grad():
    result = model.generate(
        processor,
        image=image,
        # prompt=PROMPTS[task],
        max_new_tokens=2048
    )

print("\n=== OUTPUT ===")
print(result)
