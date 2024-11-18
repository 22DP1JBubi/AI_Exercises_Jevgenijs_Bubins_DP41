from transformers import pipeline

# Создаем пайплайн для резюмирования с доступной моделью
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Исходный текст
raksts = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām.
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

# Резюмируем текст
rezume = summarizer(raksts, max_length=100, min_length=30, do_sample=False)

# Вывод результата
print(f"Rezumējums: {rezume[0]['summary_text']}")
