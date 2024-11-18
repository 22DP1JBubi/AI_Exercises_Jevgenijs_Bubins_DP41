import stanza
from collections import Counter

# Загрузка латышской модели
stanza.download('lv')
nlp = stanza.Pipeline('lv')

# Тексты
teksts1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
teksts2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

# Функция для обработки текста
def apstrade_ar_nlp(teksts):
    doc = nlp(teksts.lower())
    # Фильтруем только слова (убираем знаки препинания) и лемматизируем
    lemmatizetie_vardi = {word.lemma for sent in doc.sentences for word in sent.words if word.text.isalpha()}
    return lemmatizetie_vardi

# Обрабатываем тексты
vardi1 = apstrade_ar_nlp(teksts1)
vardi2 = apstrade_ar_nlp(teksts2)

# Найти пересечения слов
sakritibas = vardi1 & vardi2

# Считаем процент совпадений
total_vardi = len(vardi1 | vardi2)
sakritibu_procents = (len(sakritibas) / total_vardi) * 100

# Вывод результата
print(f"Sakritīgie vārdi: {sakritibas}")
print(f"Sakritību procents: {sakritibu_procents:.2f}%")
