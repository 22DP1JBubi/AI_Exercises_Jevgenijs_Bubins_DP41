from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Загрузка модели
model_name = "Davlan/xlm-roberta-base-ner-hrl"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Создаём пайплайн
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

# Исходный текст
teksts = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

# Анализ текста
rezultati = ner_pipeline(teksts)

# Вывод результатов
print("Identificētās īpašās vienības:")
for r in rezultati:
    print(f"Teksts: {r['word']}, Tips: {r['entity_group']}, Līdzība: {r['score']:.2f}")
