from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
result = generator("Reiz kādā tālā zemē...", max_length=50, num_return_sequences=1)

print("Ģenerētais teksts:", result[0]['generated_text'])
