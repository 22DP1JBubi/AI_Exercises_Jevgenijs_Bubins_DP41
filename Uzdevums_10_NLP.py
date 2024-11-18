from deep_translator import GoogleTranslator

# Функция перевода текста с латышского на английский
def translate_to_english(latvian_texts):
    translated_texts = []
    for text in latvian_texts:
        translated_text = GoogleTranslator(source="lv", target="en").translate(text)
        translated_texts.append(translated_text)
    return translated_texts

if __name__ == "__main__":
    # Тексты на латышском языке
    latvian_texts = [
        "Labdien! Kā jums klājas?",
        "Es šodien lasīju interesantu grāmatu."
    ]
    
    # Перевод на английский
    translated_texts = translate_to_english(latvian_texts)
    
    # Вывод переведённых текстов
    for original, translated in zip(latvian_texts, translated_texts):
        print(f"Latviski: {original}")
        print(f"Angliski: {translated}\n")
