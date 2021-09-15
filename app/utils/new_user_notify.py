from contextlib import suppress

from aiogram import Dispatcher
from aiogram.utils.markdown import quote_html

from app.config import Config


async def notify_new_user(dp: Dispatcher, user_id: int) -> None:
    user = await dp.bot.get_chat(chat_id=user_id)
    pics = await dp.bot.get_user_profile_photos(user_id)
    txt = [
        "#new_user",
        f"Имя: {quote_html(user.full_name)}",
        f'id: <a href="tg://user?id={user.id}">{user_id}</a>',
        f"username: @{user.username}",
    ]
    with suppress():
        photo = pics.photos[0][-1].file_id
    for admin in Config.admins:
        if photo:
            await dp.bot.send_photo(admin, photo=photo, caption=('\n'.join(txt)))
        else:
            await dp.bot.send_message(admin, '\n'.join(txt))
