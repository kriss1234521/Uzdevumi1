from textblob import TextBlob

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

for sentence in sentences:
    polarity = TextBlob(sentence).sentiment.polarity
    if polarity > 0:
        print(f"{sentence} - Pozitīvs")
    elif polarity < 0:
        print(f"{sentence} - Negatīvs")
    else:
        print(f"{sentence} - Neitrāls")
