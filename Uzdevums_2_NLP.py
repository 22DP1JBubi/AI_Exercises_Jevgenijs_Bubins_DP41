import langid

teksti = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
]

for teksts in teksti:
    valoda, _ = langid.classify(teksts)
    print(f"Teksts: '{teksts}' -> Valoda: {valoda}")
