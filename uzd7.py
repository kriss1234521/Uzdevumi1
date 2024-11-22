from gensim.models import Word2Vec

sentences = [["māja", "dzīvoklis", "jūra"]]
model = Word2Vec(sentences, min_count=1)
for word in ["māja", "dzīvoklis", "jūra"]:
    print(f"{word}: {model.wv[word]}")
