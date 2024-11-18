from transformers import AutoTokenizer, AutoModelForCausalLM
from deep_translator import GoogleTranslator
from langdetect import detect  # Используем langdetect для определения языка

# Загрузка модели и токенизатора
model_name = "Qwen/Qwen2.5-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_text(input_text, max_length=50):
     # Определяем язык текста с помощью langdetect
    detected_language = detect(input_text)

    # Если текст не на английском, переводим его на английский
    if detected_language != 'en':
        translated_input  = GoogleTranslator(source=detected_language, target='en').translate(input_text)
    else:
        translated_input  = input_text

    # Введение в токенизацию
    input_ids = tokenizer.encode(translated_input , return_tensors="pt")
    
   # Генерация текста
    output_ids = model.generate(input_ids, max_length=max_length, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)

    # Декодирование сгенерированного текста
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    # Переводим обратно на исходный язык, если он не английский
    if detected_language != 'en':
        translated_generated_text = GoogleTranslator(source='en', target=detected_language).translate(generated_text)
        return translated_generated_text
    else:
        return generated_text

if __name__ == "__main__":
    text = "Reiz kādā tālā zemē" # Пример текста на латышском языке
    completed_story  = generate_text(text)
    print(f"Ģenerētais stāsts:\n{completed_story}")