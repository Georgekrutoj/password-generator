from typing import Optional

from constants import *

from random import choice
from random import randint


class Password:
    def __init__(
            self,
            length: int,
            has_russian_letters: Optional[bool] = False,
            has_english_letters: Optional[bool] = False,
            has_special_symbols: Optional[bool] = False,
            has_numbers: Optional[bool] = True
    ) -> None:
        self.length = length
        self.has_russian_letters = has_russian_letters
        self.has_english_letters = has_english_letters
        self.has_special_symbols = has_special_symbols
        self.has_numbers = has_numbers
        self.symbols = ""

        if has_russian_letters:
            self.symbols += RUSSIAN_LETTERS
        if has_english_letters:
            self.symbols += ENGLISH_LETTERS
        if has_special_symbols:
            self.symbols += SPECIAL_SYMBOLS
        if has_numbers:
            self.symbols += NUMBERS

    def gen(self) -> str:
        password = ""

        for i in range(self.length):
            password += choice(self.symbols)

        return password
