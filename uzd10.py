from transformers import MarianMTModel, MarianTokenizer

src_texts = ["Labdien! Kā jums klājas?", "Es šodien lasīju interesantu grāmatu."]
model_name = "Helsinki-NLP/opus-mt-lv-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

for text in src_texts:
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    print(f"Izvade: {tokenizer.decode(translated[0], skip_special_tokens=True)}")
