"""
Uses text-to-speech and random number generation to help you practice number
comprehension in a small range of languages
"""

import toga
from toga.style.pack import COLUMN, ROW
from toga.sources import ListSource
import random
from gtts import gTTS
from playsound3 import playsound, PlaysoundException
import configparser

class NumberComprehension(toga.App):
    def startup(self):
        direction = COLUMN,
        main_box = toga.Box()


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
        self.languages = toga.sources.ListSource(accessors=["name"], data=[
            {"name" : "English (Australia)", "lang" : "en", "accent" : "com.au"},
            {"name" : "English (United Kingdom)", "lang" : "en", "accent" : "co.uk" },
            {"name" : "English (United States)", "lang" : "en", "accent" : "us" },
            {"name" : "French (Canada)", "lang" : "fr", "accent" : "ca" },
            {"name" : "French (France)", "lang" : "fr", "accent" : "fr" },
            {"name" : "Mandarin (China Mainland)", "lang" : "zh-CN", "accent" : "com" },
            {"name" : "Mandarin (Taiwan)", "lang" : "zh-TW", "accent" : "com" },
            {"name" : "Portuguese (Brazil)", "lang" : "pt", "accent" : "com.br" },
            {"name" : "Portuguese (Portugal)", "lang" : "pt", "accent" : "pt" },
            {"name" : "Spanish (Mexico)", "lang" : "es", "accent" : "com.mx" },
            {"name" : "Spanish (Spain)", "lang" : "es", "accent" : "es" }
        ])

        self.parse_config()


        # UI elements
        self.minimum_label = toga.Label(
            "Minimum number: ",
            margin = (0, 5),
        )
        self.minimum_input = toga.NumberInput(flex=1, max=(self.maximum-1),
            value=self.default_minimum, on_change=self.update_minimum)

        self.maximum_label = toga.Label(
            "Maximum number: ",
            margin = (0, 5),

        )
        self.maximum_input = toga.NumberInput(flex=1, min=(self.minimum+1),
            value=self.default_maximum, on_change=self.update_maximum)

        self.begin_button = toga.Button(
            "Begin",
            on_press = self.begin,
            margin = 5,
        )

        self.repeat_button = toga.Button(
            "Repeat",
            on_press = self.repeat,
        )

        self.guess_label = toga.Label(
            "Enter what you hear: ",
            margin = (0, 5),
        )
        self.guess_input = toga.TextInput(flex=1, placeholder="Enter number",
            on_confirm=self.compare_numbers)

        self.feedback_label = toga.Label(
            "",
            margin = 5,
        )

        self.language_dropdown = toga.Selection(items=self.languages, accessor="name")
        self.language_dropdown.value = self.language_dropdown.items.find(self.language)

        self.language_default_button = toga.Button(
            "Make current language default",
            on_press = self.update_default_language
        )

        # UI structuring
        main_box.add(self.minimum_label)
        main_box.add(self.minimum_input)
        main_box.add(self.maximum_label)
        main_box.add(self.maximum_input)
        main_box.add(self.begin_button)
        main_box.add(self.repeat_button)
        main_box.add(self.guess_label)
        main_box.add(self.guess_input)
        main_box.add(self.feedback_label)
        main_box.add(self.language_dropdown)
        main_box.add(self.language_default_button)

        # Show the window
        self.main_window = toga.MainWindow(title=self.formal_name)
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
            self.feedback_label.text = ""
        elif not self.run:
            self.run = 1
            self.begin_button.text = "Stop"
            await self.new_number(self)


    async def repeat(self, widget):
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


def main():
    return NumberComprehension()
