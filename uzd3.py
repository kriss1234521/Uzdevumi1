text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

words1 = set(text1.lower().split())
words2 = set(text2.lower().split())

intersection = words1.intersection(words2)
similarity = (len(intersection) / ((len(words1) + len(words2)) / 2)) * 100

print(f"Sakritība: {similarity}%")
