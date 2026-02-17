# NumberComprehension

Uses text-to-speech and random number generation to help you practice number comprehension in a range of languages

As a language learner, I noticed that while I know all the words for numbers in my target language, decoding them and identifying the number in the context of natural spoken language is a real challenge.
I created this app to allow me to practice this skill in isolation whenever I want.

Text-to-speech is provided by the [gTTS](https://gtts.readthedocs.io/en/latest/) (Google-text-to-speech) library.
Consequently, it supports any language that Google provides a text-to-speech model for, and only works while you are connected to the internet.

Please visit the [Release Page](https://github.com/sholt6/NumberComprehension/releases) to download the app for MacOS, Windows, or Debian.
However, none of these bundles are signed so may require a little advanced knowledge to install.


# Usage
For basic usage, open the app and select the desired language.
Click 'Begin' or press Ctrl/Cmd+E and a number will be read out to you.
Enter it as an integer (numbers only, no words) into the indicated box and press the Enter key.

If you are correct, a new number will be automatically generated.
If you are incorrect, some feedback will be provided.

If you wish to hear the number again, press 'Repeat' or press Ctrl/Cmd+R.

Some languages have additional modes which allow you to hear numbers spoken in different ways.
In all cases, the correct answer is still the the cardinal number, e.g.:
- "One hundred and twenty"  =>  120
- "One hundred and **twentieth**"  => 120
- "One Pound and twenty pence"  =>  120

## Settings features
**Default language:** pressing the 'Set current language as default' button will do as described: the next time you open the app, the currently selected language will already be set.

**Minimum/maximum number:** if you wish to practice a particular range of numbers, change these values.

**Number type:** all languages support cardinal numbers. Those in the table below specified to have 'Extra features' may also support:
- Cardinal (Num2Words) - slightly different approach to number generation which may work better for some languages
- Ordinal - first, second, third, etc.
- Currency - number will be read out as currency, however the correct answer will still be entered as a single integer
  - e.g. if "Ten dollars and twenty cents" were read out, the correct answer would be "1020"
- Year - some languages pronounce years differently to regular numbers. If that does not apply to your language, this should be the same as Cardinal
  - e.g. in English, 1960 would commonly be pronounced "Nineteen-sixty" as a year, but "One-thousand, nine hundred and sixty" if it were a quantity

**Thousands separator:** depending on the language you are using, you may get more useful results if you use one of these when working with numbers >999. Since languages vary in what they use as a thousands separator, the following are all available: `[_,.' ]`.
The default is to use none, and the setting is only relevant when using the 'Cardinal (Default)' number type setting.

## Known issues
- At present, regardless of chosen language, the currency setting will be spoken in Euros

# Supported languages
The following languages are all supported by this app, in some cases with multiple accents/dialects.
Please note that while I have checked they all produce output, I do not understand most of these languages and cannot state with certainty that the output given by Google will be of use to a learner of said language.
It is assumed that you already know the language well enough to judge this for yourself and merely want to practice.

Some languages are listed as supporting extra features. Please see the usage instructions above for an explanation of what this means.


| Language               | Extra features |
| ---------------------- | -------------- |
| Afrikaans              | no             |
| Albanian               | no             |
| Amharic                | **Yes**        |
| Arabic                 | **Yes**        |
| Basque                 | no             |
| Bengali                | no             |
| Bosnian                | no             |
| Bulgarian              | no             |
| Cantonese              | **Yes**        |
| Catalan                | **Yes**        |
| Chinese (Mainland)     | **Yes**        |
| Chinese (Taiwan)       | **Yes**        |
| Croatian               | no             |
| Czech                  | **Yes**        |
| Danish                 | **Yes**        |
| Dutch                  | **Yes**        |
| English (UK)           | **Yes**        |
| English (US)           | **Yes**        |
| Estonian               | no             |
| Filipino               | no             |
| Finnish                | **Yes**        |
| French (Canada)        | no             |
| French (France)        | **Yes**        |
| Galician               | no             |
| German                 | **Yes**        |
| Greek                  | no             |
| Gujarati               | no             |
| Hausa                  | no             |
| Hebrew                 | **Yes**        |
| Hindi                  | **Yes**        |
| Hungarian              | **Yes**        |
| Icelandic              | **Yes**        |
| Indonesian             | **Yes**        |
| Italian                | **Yes**        |
| Japanese               | **Yes**        |
| Javanese               | no             |
| Kannada                | **Yes**        |
| Khmer                  | no             |
| Korean                 | **Yes**        |
| Latin                  | no             |
| Latvian                | **Yes**        |
| Lithuanian             | **Yes**        |
| Malay                  | no             |
| Malayalam              | no             |
| Marathi                | no             |
| Myanmar                | no             |
| Nepali                 | no             |
| Norwegian              | **Yes**        |
| Polish                 | **Yes**        |
| Portuguese (European)  | **Yes**        |
| Portuguese (Brazilian) | **Yes**        |
| Punjabi                | no             |
| Romanian               | **Yes**        |
| Russian                | **Yes**        |
| Serbian                | **Yes**        |
| Sinhala                | no             |
| Slovak                 | **Yes**        |
| Spanish (Mexico)       | no             |
| Spanish (Spain)        | **Yes**        |
| Sundanese              | no             |
| Swahili                | no             |
| Swedish                | **Yes**        |
| Tamil                  | no             |
| Telugu                 | **Yes**        |
| Thai                   | **Yes**        |
| Turkish                | **Yes**        |
| Ukrainian              | **Yes**        |
| Urdu                   | no             |
| Vietnamese             | **Yes**        |
| Welsh                  | **Yes**        |


# Briefcase details
This cross-platform app was generated by Briefcase, part of The BeeWare Project. If you want to see more tools like Briefcase, please consider becoming a financial member of BeeWare.

- [Briefcase](https://briefcase.readthedocs.io/)
- [The BeeWare Project](https://beeware.org/)
- [becoming a financial member of BeeWare](https://beeware.org/contributing/membership)
