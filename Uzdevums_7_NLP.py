from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

model_name = "bert-base-multilingual-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def get_embedding(word):
    inputs = tokenizer(word, return_tensors="pt")
    outputs = model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1)
    return embedding.squeeze().detach().numpy()

def cosine_similarity(vec1, vec2):
    vec1 = vec1 / np.linalg.norm(vec1)
    vec2 = vec2 / np.linalg.norm(vec2)
    return np.dot(vec1, vec2)

words = ["māja", "dzīvoklis", "jūra"]
embeddings = {word: get_embedding(word) for word in words}

for word1 in words:
    for word2 in words:
        if word1 != word2:
            similarity = cosine_similarity(embeddings[word1], embeddings[word2])
            print(f"Līdzība starp '{word1}' un '{word2}': {similarity:.2f}")
