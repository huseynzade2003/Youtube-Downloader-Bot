from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Rəsmi Qrupumuz", url="https://t.me/Creativmafia")],
        [InlineKeyboardButton(
            "Sahibim👤", url="https://t.me/Mr_HD_20")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nDaha çox məlumat nümunəsi üçün /help\n Nümunə: `https://youtu.be/voBXTdusYQM` "
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
