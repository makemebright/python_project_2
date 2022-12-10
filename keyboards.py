from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='Функционал')
b2 = KeyboardButton(text='Моя кулинарная книга')

kb.add(b1, b2)

kb_receipt = ReplyKeyboardMarkup(resize_keyboard=True)
br1 = KeyboardButton(text='Следующий рецепт')
br2 = KeyboardButton(text='Добавить в мою книгу')
br3 = KeyboardButton(text='Моя кулинарная книга')

kb_receipt.add(br1, br2)
kb_receipt.add(br3)

# kb_receipt2 = ReplyKeyboardMarkup(resize_keyboard=True)
# br21 = KeyboardButton(text='Следующий рецепт')
# br22 = KeyboardButton(text='Отмена последнего действия')
# br23 = KeyboardButton(text='Моя кулинарная книга')
#
# kb_receipt.add(br21, br22)
# kb_receipt.add(br23)
