from aiogram.utils.callback_data import CallbackData

from app.utils.markup_constructor import InlineMarkupConstructor


class ExampleInlineKb(InlineMarkupConstructor):
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


class CancelKb(InlineMarkupConstructor):

    def get(self):
        schema = [1]
        actions = [
            {'text': 'Отмена', 'cb': 'cancel'},
        ]
        return self.markup(actions, schema)


class AdminShowsSettingsKb(InlineMarkupConstructor):
    add_shows = "add_shows"
    delete_shows = "delete_shows"
    display_shows = "display_shows"

    def get(self):
        actions = [
            {'text': "Добавить текст для показов", 'cb': self.add_shows},
            {'text': "Удалить текст для показов", 'cd': self.delete_shows},
            {'text': "Вывести текст для показов", 'cb': self.display_shows}
        ]
        schema = [2, 1]
        return self.markup(actions, schema)
