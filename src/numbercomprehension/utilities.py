import random

import toga
from toga.sources import ListSource

from gtts import gTTS
from num2words import num2words


async def generate_number(minimum, maximum, language, accent, num2words_lang, num_type, thousands_separator, number_mp3):
    number = random.randint(int(minimum), int(maximum))

    if num_type.type == 'cardinal_basic':
        number_tts = f"{number:,}".replace(',', f"{thousands_separator}")
    elif num2words_lang:
        try:
            number_tts = num2words(number, to=num_type.type, lang=num2words_lang)
        except NotImplementedError:
            return """Apologies, this number type \n is not implemented for your \n selected language"""

    tts = gTTS(text=f"{number_tts}", lang=f"{language}", tld=f"{accent}")
    tts.save(number_mp3)

    return number


def generate_num_type_source():
    return toga.sources.ListSource(accessors=["name"], data=[
        {"name" : "Cardinal (Default)", "type" : "cardinal_basic" },
        {"name" : "Cardinal (Num2Words)" , "type" : "cardinal" },
        {"name" : "Ordinal", "type" : "ordinal" },
        {"name" : "Currency", "type" : "currency" },
        {"name" : "Year", "type" : "year" },
    ])


def generate_thousands_separator_source():
    return toga.sources.ListSource(accessors=["name"], data=[
        {"name" : "None", "char" : "" },
        {"name" : "Comma (,)", "char" : "," },
        {"name" : "Dot (.)", "char" : "." },
        {"name" : "Apostrophe (')", "char" : "'" },
        {"name" : "Underscore (_)", "char" : "_" },
        {"name" : "Space ( )", "char" : " " },
    ])


def generate_language_source():
    return toga.sources.ListSource(accessors=["name"], data=[
        {"name" : "Afrikaans", "lang" : "af", "accent" : "co.za", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Albanian", "lang" : "sq", "accent" : "al", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Amharic", "lang" : "am", "accent" : "com", "num2words" : 1, "num2words_lang" : "am" },
        {"name" : "Arabic", "lang" : "ar", "accent" : "com.sa", "num2words" : 1, "num2words_lang" : "ar" },
        {"name" : "Basque", "lang" : "eu", "accent" : "es", "num3words" : 0, "num2words_lang" : "" },
        {"name" : "Bengali", "lang" : "bn", "accent" : "co.in", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Bosnian", "lang" : "bs", "accent" : "ba", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Bulgarian", "lang" : "bg", "accent" : "com", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Cantonese", "lang" : "yue", "accent" : "com", "num2words" : 1, "num2words_lang" : "zh_HK" },
        {"name" : "Catalan", "lang" : "ca", "accent" : "es", "num2words" : 1, "num2words_lang" : "ca" },
        {"name" : "Chinese (China Mainland)", "lang" : "zh-CN", "accent" : "com", "num2words" : 1, "num2words_lang" : "zh" },
        {"name" : "Chinese (Taiwan)", "lang" : "zh-TW", "accent" : "com", "num2words" : 1, "num2words_lang" : "zh_TW" },
        {"name" : "Croatian", "lang" : "hr", "accent" : "hr", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Czech", "lang" : "cs", "accent" : "cz", "num2words" : 1, "num2words_lang" : "cs" },
        {"name" : "Danish", "lang" : "da", "accent" : "dk", "num2words" : 1, "num2words_lang" : "da" },
        {"name" : "Dutch", "lang" : "nl", "accent" : "nl", "num2words" : 1, "num2words_lang" : "nl" },
        {"name" : "English (Australia)", "lang" : "en", "accent" : "com.au", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "English (United Kingdom)", "lang" : "en", "accent" : "co.uk", "num2words" : 1, "num2words_lang" : "en_GB" },
        {"name" : "English (United States)", "lang" : "en", "accent" : "us", "num2words" : 1, "num2words_lang" : "en" },
        {"name" : "Estonian", "lang" : "et", "accent" : "ee", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Filipino", "lang" : "tl", "accent" : "com.ph", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Finnish", "lang" : "fi", "accent" : "fi", "num2words" : 1, "num2words_lang" : "fi" },
        {"name" : "French (Canada)", "lang" : "fr-CA", "accent" : "ca", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "French (France)", "lang" : "fr", "accent" : "fr", "num2words" : 1, "num2words_lang" : "fr" },
        {"name" : "Galician", "lang" : "gl", "accent" : "es", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "German", "lang" : "de", "accent" : "de", "num2words" : 1, "num2words_lang" : "de" },
        {"name" : "Greek", "lang" : "el", "accent" : "gr", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Gujarati", "lang" : "gu", "accent" : "co.in", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Hausa", "lang" : "ha", "accent" : "ng", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Hebrew", "lang" : "iw", "accent" : "co.il", "num2words" : 1, "num2words_lang" : "he" },
        {"name" : "Hindi", "lang" : "hi", "accent" : "co.in", "num2words" : 1, "num2words_lang" : "hi" },
        {"name" : "Hungarian", "lang" : "hu", "accent" : "hu", "num2words" : 1, "num2words_lang" : "hu" },
        {"name" : "Icelandic", "lang" : "is", "accent" : "is", "num2words" : 1, "num2words_lang" : "is" },
        {"name" : "Indonesian", "lang" : "id", "accent" : "com", "num2words" : 1, "num2words_lang" : "id" },
        {"name" : "Italian", "lang" : "it", "accent" : "it", "num2words" : 1, "num2words_lang" : "it" },
        {"name" : "Japanese", "lang" : "ja", "accent" : "co.jp", "num2words" : 1, "num2words_lang" : "ja" },
        {"name" : "Javanese", "lang" : "jw", "accent" : "com", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Kannada", "lang" : "kn", "accent" : "co.in", "num2words" : 1, "num2words_lang" : "kn" },
        {"name" : "Khmer", "lang" : "km", "accent" : "com.kh", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Korean", "lang" : "ko", "accent" : "co.kr", "num2words" : 1, "num2words_lang" : "ko" },
        {"name" : "Latin", "lang" : "la", "accent" : "com", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Latvian", "lang" : "lv", "accent" : "lv", "num2words" : 1, "num2words_lang" : "lv" },
        {"name" : "Lithuanian", "lang" : "lt", "accent" : "lt", "num2words" : 1, "num2words_lang" : "lt" },
        {"name" : "Malay", "lang" : "ms", "accent" : "com.my", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Malayalam", "lang" : "ml", "accent" : "co.in", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Marathi", "lang" : "mr", "accent" : "co.in", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Myanmar", "lang" : "my", "accent" : "com.mm", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Nepali", "lang" : "ne", "accent" : "com.np", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Norwegian", "lang" : "no", "accent" : "no", "num2words" : 1, "num2words_lang" : "no" },
        {"name" : "Polish", "lang" : "pl", "accent" : "pl", "num2words" : 1, "num2words_lang" : "pl" },
        {"name" : "Portuguese (Brazil)", "lang" : "pt", "accent" : "com.br" , "num2words" : 1, "num2words_lang" : "pt_BR" },
        {"name" : "Portuguese (Portugal)", "lang" : "pt", "accent" : "pt" , "num2words" : 1, "num2words_lang" : "pt" },
        {"name" : "Punjabi", "lang" : "pa", "accent" : "co.in", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Romanian", "lang" : "ro", "accent" : "ro", "num2words" : 1, "num2words_lang" : "ro" },
        {"name" : "Russian", "lang" : "ru", "accent" : "ru", "num2words" : 1, "num2words_lang" : "ru" },
        {"name" : "Serbian", "lang" : "sr", "accent" : "rs", "num2words" : 1, "num2words_lang" : "sr" },
        {"name" : "Sinhala", "lang" : "si", "accent" : "lk", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Slovak", "lang" : "sk", "accent" : "sk", "num2words" : 1, "num2words_lang" : "sk" },
        {"name" : "Spanish (Mexico)", "lang" : "es", "accent" : "com.mx" , "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Spanish (Spain)", "lang" : "es", "accent" : "es" , "num2words" : 1, "num2words_lang" : "es" },
        {"name" : "Sundanese", "lang" : "su", "accent" : "com", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Swahili", "lang" : "sw", "accent" : "com", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Swedish", "lang" : "sv", "accent" : "se", "num2words" : 1, "num2words_lang" : "sv" },
        {"name" : "Tamil", "lang" : "ta", "accent" : "co.in", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Telugu", "lang" : "te", "accent" : "co.in", "num2words" : 1, "num2words_lang" : "te" },
        {"name" : "Thai", "lang" : "th", "accent" : "co.th", "num2words" : 1, "num2words_lang" : "th" },
        {"name" : "Turkish", "lang" : "tr", "accent" : "com.tr", "num2words" : 1, "num2words_lang" : "tr" },
        {"name" : "Ukrainian", "lang" : "uk", "accent" : "com.ua", "num2words" : 1, "num2words_lang" : "uk" },
        {"name" : "Urdu", "lang" : "ur", "accent" : "com.pk", "num2words" : 0, "num2words_lang" : "" },
        {"name" : "Vietnamese", "lang" : "vi", "accent" : "com.vn", "num2words" : 1, "num2words_lang" : "vi" },
        {"name" : "Welsh", "lang" : "cy", "accent" : "co.uk", "num2words" : 1, "num2words_lang" : "cy" },
    ])
