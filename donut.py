import torch
from PIL import Image
from transformers import DonutProcessor, VisionEncoderDecoderModel

MODEL_ID = "naver-clova-ix/donut-base-finetuned-docvqa"

try:
    print(f"Loading model: {MODEL_ID}")
    processor = DonutProcessor.from_pretrained(MODEL_ID)
    model = VisionEncoderDecoderModel.from_pretrained(MODEL_ID)
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    model.to(device)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    print("Make sure you have an internet connection or try downloading the model manually")




# 3) Prepare image + question prompt
image = Image.open("Image_1.jpg").convert("RGB")
question = "Extract all visible text and fields from this document. Return everything in JSON format."

task_prompt = f"<s_docvqa><s_question>{question}</s_question><s_answer>"

inputs = processor(
    image,
    task_prompt,
    return_tensors="pt"
).to(device)

# 4) Generate prediction
generated_ids = model.generate(
    pixel_values=inputs.pixel_values,
    decoder_input_ids=inputs.input_ids,
    max_length=512
)

# 5) Decode and format output
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
output = processor.token2json(generated_text)

print("Answer:", output)
