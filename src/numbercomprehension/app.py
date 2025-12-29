"""
Uses text-to-speech and random number generation to help you practice number
comprehension in a small range of languages
"""

import toga
from toga.style.pack import COLUMN, ROW
import random
from gtts import gTTS
from playsound3 import playsound, PlaysoundException

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
        self.default_language = 'French (France)'
        self.language = self.default_language
        self.language_name = 'French (France)'
        self.languages = [
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
          {"name" : "Spanish (Spain)", "lang" : "es", "accent" : "es" },
        ]

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

        self.language_dropdown = toga.Selection(items=self.languages, accessor="name")
        self.language_dropdown.value = self.language_dropdown.items.find({"name" : "French (France)"})

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
            "Feedback goes here",
            margin = 5,
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

        # Show the window
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    # Functions
    async def begin(self, widget):

        if self.run:
            self.run = 0
            self.begin_button.text = "Begin"
        elif not self.run:
            self.run = 1
            self.begin_button.text = "Stop"
            await self.new_number(self)


    async def repeat(self, widget):
        await self.speak_number(self)


    async def generate_number(self, widget):
        self.match = False
        new_number = random.randint(int(self.minimum), int(self.maximum))
        self.number = new_number

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
            return

        if guess > self.number:
            await self.speak_number(self)
            pass # TODO: Add feedback functionality
        elif guess < self.number:
            await self.speak_number(self)
            pass # TODO: Add feedback functionality
        else:
            self.match = True
            self.guess_input.value = ''
            await self.new_number(self)

    async def new_number(self, widget):
        if self.run:
            await self.generate_number(self)
            await self.speak_number(self)

    async def update_minimum(self, widget):
        self.minimum = self.minimum_input.value


    async def update_maximum(self, widget):
        self.maximum = self.maximum_input.value


def main():
    return NumberComprehension()
