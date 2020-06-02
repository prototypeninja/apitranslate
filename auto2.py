import pysrt
import os
from mtranslate import translate
def main(text):
    to_translate = text
    return translate(to_translate, 'fr')
