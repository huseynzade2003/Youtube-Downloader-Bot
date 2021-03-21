from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Hal-hazırda yalnız Youtube Single-i dəstəkləyir (Pleylist yoxdur) Yalnız Youtube linki Göndərinl"
    await message.reply_text(helptxt)
