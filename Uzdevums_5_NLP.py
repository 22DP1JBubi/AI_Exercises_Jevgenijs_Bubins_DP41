import re

# Необработанный текст
neapstradats_teksts = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

# Функция для очистки текста
def tirit_tekstu(teksts):
    # Удаляем упоминания (@John)
    teksts = re.sub(r"@\w+", "", teksts)
    # Удаляем URL (http://example.com)
    teksts = re.sub(r"http\S+|www\.\S+", "", teksts)
    # Удаляем эмодзи
    teksts = re.sub(r"[^\w\s.,!?]", "", teksts)
    # Удаляем лишние восклицательные знаки (!!! -> .)
    teksts = re.sub(r"[!]+", ".", teksts)
    # Приводим текст к нижнему регистру
    teksts = teksts.lower()
    # Удаляем лишние пробелы
    teksts = re.sub(r"\s+", " ", teksts).strip()
    return teksts

# Обрабатываем текст
tirits_teksts = tirit_tekstu(neapstradats_teksts)

# Вывод результата
print(f"Tīrs teksts: {tirits_teksts}")
