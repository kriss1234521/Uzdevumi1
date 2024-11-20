from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

# Izveidojiet modeli
sentences = [["māja", "dzīvoklis", "jūra"]]
model = Word2Vec(sentences, vector_size=50, min_count=1)

# Iegūstiet vektorus
vec_m = model.wv['māja']
vec_d = model.wv['dzīvoklis']
vec_j = model.wv['jūra']

# Salīdzina līdzības
sim_m_d = cosine_similarity([vec_m], [vec_d])[0][0]
sim_m_j = cosine_similarity([vec_m], [vec_j])[0][0]

print(f"Līdzība 'māja' un 'dzīvoklis': {sim_m_d}")
print(f"Līdzība 'māja' un 'jūra': {sim_m_j}")
