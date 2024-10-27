import flet as ft

from constants import *
from password import Password


def main(page: ft.Page) -> None:
    def gen(_) -> None:
        pass_length = int(length.value)
        password = Password(
            pass_length,
            has_russian_letters.value,
            has_english_letters.value,
            has_special_symbols.value,
            has_numbers.value
        )
        generated.value = password.gen()
        generated.size = TEXT_SIZE / pass_length

        page.update()

    page.title = TITLE
    page.theme_mode = THEME
    page.window.width = WINDOW_WIDTH
    page.window.height = WINDOW_HEIGHT
    page.window.max_width = WINDOW_MAX_WIDTH
    page.window.max_height = WINDOW_MAX_HEIGHT
    page.window.min_width = WINDOW_MIN_WIDTH
    page.window.min_height = WINDOW_MIN_HEIGHT
    page.window.resizable = IS_WINDOW_RESIZABLE

    has_english_letters = ft.Checkbox("English letters")
    has_russian_letters = ft.Checkbox("Russian letters")
    has_special_symbols = ft.Checkbox("Special symbols")
    has_numbers = ft.Checkbox(label="Has numbers", value=True)
    length = ft.TextField(
        keyboard_type=ft.KeyboardType.NUMBER,
        multiline=False,
        max_length=MAX_LENGTH_OF_LENGTH,
        label="Password length"
    )
    submit_button = ft.ElevatedButton(
        text="Generate",
        icon=ft.icons.PASSWORD,
        on_click=gen
    )
    generated = ft.Text()

    page.add(ft.Column(
        controls=[
            has_english_letters,
            has_russian_letters,
            has_special_symbols,
            has_numbers,
            length,
            submit_button,
            generated
        ]
    ))

    page.update()


ft.app(main)
