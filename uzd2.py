from langdetect import detect

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day."
]

for text in texts:
    print(detect(text))
