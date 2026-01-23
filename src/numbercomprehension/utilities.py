import random

import toga
from toga.sources import ListSource

from gtts import gTTS
import num2words


async def generate_number(minimum, maximum, language, accent, number_mp3):
    number = random.randint(int(minimum), int(maximum))

    tts = gTTS(text=f"{number}", lang=f"{language}", tld=f"{accent}")
    tts.save(number_mp3)

    return number


def generate_language_source():
    return toga.sources.ListSource(accessors=["name"], data=[
        {"name" : "Afrikaans", "lang" : "af", "accent" : "co.za", "num2words" : 0 },
        {"name" : "Albanian", "lang" : "sq", "accent" : "al", "num2words" : 0 },
        {"name" : "Amharic", "lang" : "am", "accent" : "com", "num2words" : 1 },
        {"name" : "Arabic", "lang" : "ar", "accent" : "com.sa", "num2words" : 1 },
        {"name" : "Basque", "lang" : "eu", "accent" : "es", "num2words" : 0 },
        {"name" : "Bengali", "lang" : "bn", "accent" : "co.in", "num2words" : 0 },
        {"name" : "Bosnian", "lang" : "bs", "accent" : "ba", "num2words" : 0 },
        {"name" : "Bulgarian", "lang" : "bg", "accent" : "com", "num2words" : 0 },
        {"name" : "Cantonese", "lang" : "yue", "accent" : "com", "num2words" : 1 },
        {"name" : "Catalan", "lang" : "ca", "accent" : "es", "num2words" : 1 },
        {"name" : "Chinese (China Mainland)", "lang" : "zh-CN", "accent" : "com", "num2words" : 1 },
        {"name" : "Chinese (Taiwan)", "lang" : "zh-TW", "accent" : "com", "num2words" : 1 },
        {"name" : "Croatian", "lang" : "hr", "accent" : "hr", "num2words" : 0 },
        {"name" : "Czech", "lang" : "cs", "accent" : "cz", "num2words" : 1 },
        {"name" : "Danish", "lang" : "da", "accent" : "dk", "num2words" : 1 },
        {"name" : "Dutch", "lang" : "nl", "accent" : "nl", "num2words" : 1 },
        {"name" : "English (Australia)", "lang" : "en", "accent" : "com.au", "num2words" : 0 },
        {"name" : "English (United Kingdom)", "lang" : "en", "accent" : "co.uk", "num2words" : 1 },
        {"name" : "English (United States)", "lang" : "en", "accent" : "us", "num2words" : 1 },
        {"name" : "Estonian", "lang" : "et", "accent" : "ee", "num2words" : 0 },
        {"name" : "Filipino", "lang" : "tl", "accent" : "com.ph", "num2words" : 0 },
        {"name" : "Finnish", "lang" : "fi", "accent" : "fi", "num2words" : 1 },
        {"name" : "French (Canada)", "lang" : "fr-CA", "accent" : "ca", "num2words" : 0 },
        {"name" : "French (France)", "lang" : "fr", "accent" : "fr", "num2words" : 1 },
        {"name" : "Galician", "lang" : "gl", "accent" : "es", "num2words" : 0 },
        {"name" : "German", "lang" : "de", "accent" : "de", "num2words" : 1 },
        {"name" : "Greek", "lang" : "el", "accent" : "gr", "num2words" : 0 },
        {"name" : "Gujarati", "lang" : "gu", "accent" : "co.in", "num2words" : 0 },
        {"name" : "Hausa", "lang" : "ha", "accent" : "ng", "num2words" : 0 },
        {"name" : "Hebrew", "lang" : "iw", "accent" : "co.il", "num2words" : 1 },
        {"name" : "Hindi", "lang" : "hi", "accent" : "co.in", "num2words" : 1 },
        {"name" : "Hungarian", "lang" : "hu", "accent" : "hu", "num2words" : 1 },
        {"name" : "Icelandic", "lang" : "is", "accent" : "is", "num2words" : 1 },
        {"name" : "Indonesian", "lang" : "id", "accent" : "com", "num2words" : 1 },
        {"name" : "Italian", "lang" : "it", "accent" : "it", "num2words" : 1 },
        {"name" : "Japanese", "lang" : "ja", "accent" : "co.jp", "num2words" : 1 },
        {"name" : "Javanese", "lang" : "jw", "accent" : "com", "num2words" : 0 },
        {"name" : "Kannada", "lang" : "kn", "accent" : "co.in", "num2words" : 1 },
        {"name" : "Khmer", "lang" : "km", "accent" : "com.kh", "num2words" : 0 },
        {"name" : "Korean", "lang" : "ko", "accent" : "co.kr", "num2words" : 1 },
        {"name" : "Latin", "lang" : "la", "accent" : "com", "num2words" : 0 },
        {"name" : "Latvian", "lang" : "lv", "accent" : "lv", "num2words" : 1 },
        {"name" : "Lithuanian", "lang" : "lt", "accent" : "lt", "num2words" : 1 },
        {"name" : "Malay", "lang" : "ms", "accent" : "com.my", "num2words" : 0 },
        {"name" : "Malayalam", "lang" : "ml", "accent" : "co.in", "num2words" : 0 },
        {"name" : "Marathi", "lang" : "mr", "accent" : "co.in", "num2words" : 0 },
        {"name" : "Myanmar", "lang" : "my", "accent" : "com.mm", "num2words" : 0 },
        {"name" : "Nepali", "lang" : "ne", "accent" : "com.np", "num2words" : 0 },
        {"name" : "Norwegian", "lang" : "no", "accent" : "no", "num2words" : 1 },
        {"name" : "Polish", "lang" : "pl", "accent" : "pl", "num2words" : 1 },
        {"name" : "Portuguese (Brazil)", "lang" : "pt", "accent" : "com.br" , "num2words" : 1 },
        {"name" : "Portuguese (Portugal)", "lang" : "pt", "accent" : "pt" , "num2words" : 1 },
        {"name" : "Punjabi", "lang" : "pa", "accent" : "co.in", "num2words" : 0 },
        {"name" : "Romanian", "lang" : "ro", "accent" : "ro", "num2words" : 1 },
        {"name" : "Russian", "lang" : "ru", "accent" : "ru", "num2words" : 1 },
        {"name" : "Serbian", "lang" : "sr", "accent" : "rs", "num2words" : 1 },
        {"name" : "Sinhala", "lang" : "si", "accent" : "lk", "num2words" : 0 },
        {"name" : "Slovak", "lang" : "sk", "accent" : "sk", "num2words" : 1 },
        {"name" : "Spanish (Mexico)", "lang" : "es", "accent" : "com.mx" , "num2words" : 0 },
        {"name" : "Spanish (Spain)", "lang" : "es", "accent" : "es" , "num2words" : 1 },
        {"name" : "Sundanese", "lang" : "su", "accent" : "com", "num2words" : 0 },
        {"name" : "Swahili", "lang" : "sw", "accent" : "com", "num2words" : 0 },
        {"name" : "Swedish", "lang" : "sv", "accent" : "se", "num2words" : 1 },
        {"name" : "Tamil", "lang" : "ta", "accent" : "co.in", "num2words" : 0 },
        {"name" : "Telugu", "lang" : "te", "accent" : "co.in", "num2words" : 1 },
        {"name" : "Thai", "lang" : "th", "accent" : "co.th", "num2words" : 1 },
        {"name" : "Turkish", "lang" : "tr", "accent" : "com.tr", "num2words" : 1 },
        {"name" : "Ukrainian", "lang" : "uk", "accent" : "com.ua", "num2words" : 1 },
        {"name" : "Urdu", "lang" : "ur", "accent" : "com.pk", "num2words" : 0 },
        {"name" : "Vietnamese", "lang" : "vi", "accent" : "com.vn", "num2words" : 1 },
        {"name" : "Welsh", "lang" : "cy", "accent" : "co.uk", "num2words" : 1 },
    ])
