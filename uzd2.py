from langdetect import detect

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day."
]

print("Tekstu valodas noteikšana:")
for text in texts:
    language = detect(text)
    print(f"Teksts: '{text}' - Valoda: {language}")
