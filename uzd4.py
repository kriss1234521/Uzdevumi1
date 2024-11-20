from textblob import TextBlob

texts = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

print("Noskaņojuma analīze:")
for text in texts:
    analysis = TextBlob(text)
    sentiment = "Pozitīvs" if analysis.polarity > 0 else "Negatīvs" if analysis.polarity < 0 else "Neitrāls"
    print(f"Teikums: '{text}' - Noskaņojums: {sentiment}")
