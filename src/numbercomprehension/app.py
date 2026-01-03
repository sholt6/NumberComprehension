"""
Uses text-to-speech and random number generation to help you practice number
comprehension in a range of languages
"""

import toga
from toga.style.pack import COLUMN, ROW
from toga.sources import ListSource
from travertino.colors import color, rgb

import configparser
import random

from gtts import gTTS
from playsound3 import playsound, PlaysoundException


class NumberComprehension(toga.App):
    def startup(self):
        direction = COLUMN,
        main_box = toga.Box(direction=ROW, align_items="center", justify_content="center")

        # Variables
        self.run = 0
        self.number = None
        self.default_minimum = 0
        self.minimum = self.default_minimum
        self.default_maximum = 2100
        self.maximum = self.default_maximum
        self.match = False
        self.number_mp3 = self.paths.cache / 'number.mp3'
        self.config_file = self.paths.config / 'config.toml'
        self.default_language = 'French (France)'
        self.language = self.default_language
        self.languages = self.generate_language_source(self)

        ## Styling Variables
        #self.box_background_color = color('#333338')
        #self.begin_button_color = color('#6db442')
        #self.stop_button_color = color('#f04a50')

        # Parse config
        self.parse_config()

        # UI elements
        ## Settings
        self.minimum_label = toga.Label(
            "Minimum number: ",
            margin = 10,
            font_weight = 'bold',
        )

        self.minimum_input = toga.NumberInput(
            flex=1,
            max=(self.maximum-1),
            value=self.default_minimum,
            on_change=self.update_minimum,
            margin = 10,
            margin_top = 0,
        )

        self.maximum_label = toga.Label(
            "Maximum number: ",
            margin = 10,
            font_weight = 'bold',
        )

        self.maximum_input = toga.NumberInput(
            flex=1,
            min=(self.minimum+1),
            value=self.default_maximum,
            on_change=self.update_maximum,
            margin = 10,
            margin_top = 0,
        )

        self.language_settings_label = toga.Label(
            "Voice language: ",
            margin = 10,
            font_weight = 'bold',
        )

        self.language_dropdown = toga.Selection(
            items=self.languages,
            accessor="name",
            margin = 10,
            margin_top = 0,
        )
        self.language_dropdown.value = self.language_dropdown.items.find(self.language)

        self.language_default_button = toga.Button(
            "Set current language as default",
            on_press = self.update_default_language,
            margin = 10,
            margin_top = 0,
        )

        ## Controls
        self.begin_button = toga.Button(
            "Begin",
            on_press = self.begin,
            margin = 10,
            #background_color=self.begin_button_color,
            #font_weight = 'bold',

        )

        self.repeat_button = toga.Button(
            "Repeat",
            on_press = self.repeat,
            margin = 10,
        )

        ## Answering
        self.guess_label = toga.Label(
            "Enter what you hear: ",
            margin = 10,
            #font_weight = 'bold',
        )
        self.guess_input = toga.TextInput(
            placeholder="Enter number",
            on_confirm=self.compare_numbers,
            margin = 10,
            margin_top = 0,
            width = 200
        )

        self.feedback_label = toga.Label(
            "",
            margin = 10,
            margin_top = 0,
        )


        # Interface layout
        settings_box = toga.Box(direction=COLUMN, margin_top=25, margin_left=15, margin_right=10)#, background_color=self.box_background_color)
        settings_box.add(self.minimum_label)
        settings_box.add(self.minimum_input)
        settings_box.add(self.maximum_label)
        settings_box.add(self.maximum_input)
        settings_box.add(self.language_settings_label)
        settings_box.add(self.language_dropdown)
        settings_box.add(self.language_default_button)

        controls_box = toga.Box(direction=COLUMN, margin_top=25, margin_left=25, margin_right=25)#, background_color=self.box_background_color)
        controls_box.add(self.begin_button)
        controls_box.add(self.repeat_button)
        controls_box.add(self.guess_label)
        controls_box.add(self.guess_input)
        controls_box.add(self.feedback_label)

        main_box.add(controls_box)
        main_box.add(settings_box)


        # Hotkeys
        start = toga.Command(
            self.begin,
            text="Start/stop",
            shortcut=toga.Key.MOD_1 + "e",
            order=1
        )

        repeat = toga.Command(
            self.repeat,
            text="Repeat number",
            shortcut=toga.Key.MOD_1 + 'r',
            order=2
        )

        self.main_window = toga.MainWindow()
        self.main_window.toolbar.add(start, repeat)


        # Show the window
        self.main_window = toga.MainWindow(title="Number Comprehension", size = (440, 380))
        self.main_window.content = main_box
        self.main_window.show()


    # Functions
    def parse_config(self):
        config = configparser.ConfigParser()

        try:
            config.read(self.config_file)
            self.language = config['SETTINGS']['PREFERRED_LANGUAGE']
        except KeyError:
            self.create_config(self)


    def create_config(self, widget, *args):
        config = configparser.ConfigParser()

        config['SETTINGS'] = {'PREFERRED_LANGUAGE' : self.language}
        with open(self.config_file, 'w') as config_file:
            config.write(config_file)


    def update_default_language(self, widget):
        config = configparser.ConfigParser()

        try:
            config.read(self.config_file)
            config['SETTINGS']['PREFERRED_LANGUAGE'] = str(self.language_dropdown.value.name)
            with open(self.config_file, 'w') as config_file:
                config.write(config_file)
        except (FileNotFoundError, KeyError):
            self.create_config(self, widget)


    async def begin(self, widget):
        if self.run:
            self.run = 0
            self.begin_button.text = "Begin"
            self.begin_button.background_color = self.begin_button_color
            self.feedback_label.text = ""
        elif not self.run:
            self.run = 1
            self.begin_button.text = "Stop"
            self.begin_button.background_color = self.stop_button_color
            self.guess_input.focus()
            await self.new_number(self)


    async def repeat(self, widget):
        if self.run:
            await self.speak_number(self)


    async def generate_number(self, widget):
        # Reset some other values first; perhaps move this
        self.match = False
        self.feedback_label.text = ""

        self.number = random.randint(int(self.minimum), int(self.maximum))

        tts = gTTS(text=f"{self.number}", lang=f"{self.language_dropdown.value.lang}", tld=f"{self.language_dropdown.value.accent}")
        tts.save(self.number_mp3)


    async def speak_number(self, widget):
        try:
            playsound(self.number_mp3, False)
        except PlaysoundException:
            return


    async def compare_numbers(self, widget):
        if self.number is None:
            self.feedback_label.text = "Press 'Begin' to start!"
            return

        try:
            guess = int(self.guess_input.value)
        except ValueError:
            self.feedback_label.text = "Enter integers only!"
            return

        if guess > self.number:
            self.feedback_label.text = "Your guess is too high"
            await self.speak_number(self)
        elif guess < self.number:
            self.feedback_label.text = "Your guess is too low"
            await self.speak_number(self)
        else:
            self.match = True
            self.guess_input.value = ''
            await self.new_number(self)

    async def new_number(self, widget):
        if self.run:
            await self.generate_number(self)
            await self.speak_number(self)

    def update_minimum(self, widget):
        self.minimum = self.minimum_input.value

    def update_maximum(self, widget):
        self.maximum = self.maximum_input.value

    def generate_language_source(self, widget):
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


def main():
    return NumberComprehension()
