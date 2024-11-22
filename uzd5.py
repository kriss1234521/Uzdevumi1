import re

raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"
cleaned_text = re.sub(r'[@#\!\?]+|http\S+', '', raw_text).lower()
print(cleaned_text.strip())
