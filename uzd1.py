from collections import Counter
import re

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."
text = re.sub(r'[^\w\s]', '', text).lower()  # Tīra tekstu
word_counts = Counter(text.split())
print(word_counts)
