import re

text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

# Tīrīšana
text = re.sub(r'@\w+', '', text)  # Noņem lietotājvārdus
text = re.sub(r'http\S+', '', text)  # Noņem URL
text = re.sub(r'[^\w\s]', '', text)  # Noņem pieturzīmes un simbolus
text = text.lower().strip()  # Mazie burti un apgriešana

print(f"Tīrs teksts: {text}")
