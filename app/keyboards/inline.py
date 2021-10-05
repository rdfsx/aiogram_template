from aiogram.utils.callback_data import CallbackData

from app.middlewares.i18n import I18nMiddleware
from app.utils.markup_constructor import InlineMarkupConstructor


class ExampleInlineMarkup(InlineMarkupConstructor):
    callback_data = CallbackData('test', 'number')

    def get(self):
        schema = [3, 2, 1]
        actions = [
            {'text': '1', 'callback_data': self.callback_data.new('1')},
            {'text': '2', 'callback_data': self.callback_data.new('2')},
            {'text': '3', 'callback_data': '3'},
            {'text': '4', 'callback_data': self.callback_data.new('4')},
            {'text': '5', 'callback_data': (self.callback_data, '5')},
            {'text': '6', 'callback_data': '6'},
        ]
        return self.markup(actions, schema)


class CancelMarkup(InlineMarkupConstructor):

    def get(self):
        schema = [1]
        actions = [
            {'text': 'Отмена', 'callback_data': 'cancel'},
        ]
        return self.markup(actions, schema)


class LanguageMarkup(InlineMarkupConstructor):
    callback_data = CallbackData("lang", "value")

    def get(self):
        languages = I18nMiddleware.AVAILABLE_LANGUAGES
        actions = [{'text': languages[lang].label, 'callback_data': self.callback_data.new(lang)} for lang in languages]
        schema = [1] * len(actions)

        return self.markup(actions, schema)
