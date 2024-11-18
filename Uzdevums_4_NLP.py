from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Загрузка модели и токенизатора
model_name = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Функция для анализа настроения
def analizet_noskanojumu(teksts):
    # Токенизация текста
    inputs = tokenizer(teksts, return_tensors="pt", truncation=True, max_length=512)  # Ограничим длину
    # Прогноз модели
    outputs = model(**inputs)
    logits = outputs.logits
    # Определение метки настроения
    probabilities = torch.softmax(logits, dim=-1).detach().numpy()[0]
    labels = ["negative", "neutral", "positive"]
    max_index = probabilities.argmax()

    # Условие для нейтрального текста
    if probabilities[max_index] < 0.6:
        return "neutral", probabilities[max_index]
    return labels[max_index], probabilities[max_index]

# Тексты
teikumi = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

# Анализ настроения для каждого текста
for teikums in teikumi:
    noskanojums, varbutiba = analizet_noskanojumu(teikums)
    print(f"Teikums: '{teikums}' -> Noskaņojums: {noskanojums} ({varbutiba:.2f})")
