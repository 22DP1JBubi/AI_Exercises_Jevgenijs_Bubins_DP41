import stanza
from collections import Counter

# Загрузка латышской модели
stanza.download('lv')
nlp = stanza.Pipeline('lv')

# Текст
teksts = """
Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas.
Kaķis gribēja redzēt sauli, bet saule слēpās aiz māкоņiem.
"""

# Обработка текста
doc = nlp(teksts)

# Извлекаем только слова (без знаков препинания)
vardi = [word.text.lower() for sent in doc.sentences for word in sent.words if word.text.isalpha()]

# Подсчитываем частоту
vardu_biezums = Counter(vardi)

# Выводим результаты
print("Vārdu biežums:")
for vards, skaits in vardu_biezums.items():
    print(f"{vards}: {skaits}")
