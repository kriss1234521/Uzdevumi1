text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

# Tīrīšana un apstrāde
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return set(text.split())

words1 = clean_text(text1)
words2 = clean_text(text2)

# Sakritības analīze
common_words = words1.intersection(words2)
similarity_percentage = len(common_words) / len(words1.union(words2)) * 100

print(f"Kopējie vārdi: {common_words}")
print(f"Sakritības līmenis: {similarity_percentage:.2f}%")
