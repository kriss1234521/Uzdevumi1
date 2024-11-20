from collections import Counter
import re

text = """
Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas.
Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem.
"""

# Teksta tīrīšana un apstrāde
text = text.lower()
text = re.sub(r'[^\w\s]', '', text)  # Noņem pieturzīmes
words = text.split()

# Vārdu skaitīšana
word_counts = Counter(words)

print("Vārdu biežuma analīze:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
