import random

import toga
from toga.sources import ListSource

from gtts import gTTS


async def generate_number(minimum, maximum, language, accent, number_mp3):
    number = random.randint(int(minimum), int(maximum))

    tts = gTTS(text=f"{number}", lang=f"{language}", tld=f"{accent}")
    tts.save(number_mp3)

    return number


def generate_language_source():
    return toga.sources.ListSource(accessors=["name"], data=[
        {"name" : "Afrikaans", "lang" : "af", "accent" : "co.za"},
        {"name" : "Albanian", "lang" : "sq", "accent" : "al"},
        {"name" : "Amharic", "lang" : "am", "accent" : "com"},
        {"name" : "Arabic", "lang" : "ar", "accent" : "com.sa"},
        {"name" : "Basque", "lang" : "eu", "accent" : "es"},
        {"name" : "Bengali", "lang" : "bn", "accent" : "co.in"},
        {"name" : "Bosnian", "lang" : "bs", "accent" : "ba"},
        {"name" : "Bulgarian", "lang" : "bg", "accent" : "com"},
        {"name" : "Cantonese", "lang" : "yue", "accent" : "com"},
        {"name" : "Catalan", "lang" : "ca", "accent" : "es"},
        {"name" : "Chinese (China Mainland)", "lang" : "zh-CN", "accent" : "com"},
        {"name" : "Chinese (Taiwan)", "lang" : "zh-TW", "accent" : "com"},
        {"name" : "Croatian", "lang" : "hr", "accent" : "hr"},
        {"name" : "Czech", "lang" : "cs", "accent" : "cz"},
        {"name" : "Danish", "lang" : "da", "accent" : "dk"},
        {"name" : "Dutch", "lang" : "nl", "accent" : "nl"},
        {"name" : "English (Australia)", "lang" : "en", "accent" : "com.au"},
        {"name" : "English (United Kingdom)", "lang" : "en", "accent" : "co.uk"},
        {"name" : "English (United States)", "lang" : "en", "accent" : "us"},
        {"name" : "Estonian", "lang" : "et", "accent" : "ee"},
        {"name" : "Filipino", "lang" : "tl", "accent" : "com.ph"},
        {"name" : "Finnish", "lang" : "fi", "accent" : "fi"},
        {"name" : "French (Canada)", "lang" : "fr-CA", "accent" : "ca"},
        {"name" : "French (France)", "lang" : "fr", "accent" : "fr"},
        {"name" : "Galician", "lang" : "gl", "accent" : "es"},
        {"name" : "German", "lang" : "de", "accent" : "de"},
        {"name" : "Greek", "lang" : "el", "accent" : "gr"},
        {"name" : "Gujarati", "lang" : "gu", "accent" : "co.in"},
        {"name" : "Hausa", "lang" : "ha", "accent" : "ng"},
        {"name" : "Hebrew", "lang" : "iw", "accent" : "co.il"},
        {"name" : "Hindi", "lang" : "hi", "accent" : "co.in"},
        {"name" : "Hungarian", "lang" : "hu", "accent" : "hu"},
        {"name" : "Icelandic", "lang" : "is", "accent" : "is"},
        {"name" : "Indonesian", "lang" : "id", "accent" : "com"},
        {"name" : "Italian", "lang" : "it", "accent" : "it"},
        {"name" : "Japanese", "lang" : "ja", "accent" : "co.jp"},
        {"name" : "Javanese", "lang" : "jw", "accent" : "com"},
        {"name" : "Kannada", "lang" : "kn", "accent" : "co.in"},
        {"name" : "Khmer", "lang" : "km", "accent" : "com.kh"},
        {"name" : "Korean", "lang" : "ko", "accent" : "co.kr"},
        {"name" : "Latin", "lang" : "la", "accent" : "com"},
        {"name" : "Latvian", "lang" : "lv", "accent" : "lv"},
        {"name" : "Lithuanian", "lang" : "lt", "accent" : "lt"},
        {"name" : "Malay", "lang" : "ms", "accent" : "com.my"},
        {"name" : "Malayalam", "lang" : "ml", "accent" : "co.in"},
        {"name" : "Marathi", "lang" : "mr", "accent" : "co.in"},
        {"name" : "Myanmar", "lang" : "my", "accent" : "com.mm"},
        {"name" : "Nepali", "lang" : "ne", "accent" : "com.np"},
        {"name" : "Norwegian", "lang" : "no", "accent" : "no"},
        {"name" : "Polish", "lang" : "pl", "accent" : "pl"},
        {"name" : "Portuguese (Brazil)", "lang" : "pt", "accent" : "com.br" },
        {"name" : "Portuguese (Portugal)", "lang" : "pt", "accent" : "pt" },
        {"name" : "Punjabi", "lang" : "pa", "accent" : "co.in"},
        {"name" : "Romanian", "lang" : "ro", "accent" : "ro"},
        {"name" : "Russian", "lang" : "ru", "accent" : "ru"},
        {"name" : "Serbian", "lang" : "sr", "accent" : "rs"},
        {"name" : "Sinhala", "lang" : "si", "accent" : "lk"},
        {"name" : "Slovak", "lang" : "sk", "accent" : "sk"},
        {"name" : "Spanish (Mexico)", "lang" : "es", "accent" : "com.mx" },
        {"name" : "Spanish (Spain)", "lang" : "es", "accent" : "es" },
        {"name" : "Sundanese", "lang" : "su", "accent" : "com"},
        {"name" : "Swahili", "lang" : "sw", "accent" : "com"},
        {"name" : "Swedish", "lang" : "sv", "accent" : "se"},
        {"name" : "Tamil", "lang" : "ta", "accent" : "co.in"},
        {"name" : "Telugu", "lang" : "te", "accent" : "co.in"},
        {"name" : "Thai", "lang" : "th", "accent" : "co.th"},
        {"name" : "Turkish", "lang" : "tr", "accent" : "com.tr"},
        {"name" : "Ukrainian", "lang" : "uk", "accent" : "com.ua"},
        {"name" : "Urdu", "lang" : "ur", "accent" : "com.pk"},
        {"name" : "Vietnamese", "lang" : "vi", "accent" : "com.vn"},
        {"name" : "Welsh", "lang" : "cy", "accent" : "co.uk"},
    ])
