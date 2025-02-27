from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram.errors import UserNotParticipant
import humanize
from helper.database import  insert 

force_channel = "mkn_bots_updates"

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
    if force_channel:   
        try:             
            user = await client.get_chat_member(force_channel, message.from_user.id)
            if user.status == "kicked":
               await message.reply_text("Sorry, You're Banned")
               return
        except UserNotParticipant:
            await message.reply_text(
                text="**sorry bro നിങ്ങൾ ഞങ്ങളുടെ ചാനലിൽ ജോയിൻ ചെയ്തിട്ടില്ല താഴെയുള്ള ബട്ടനിൽ ക്ലിക്ക് ചെയ്ത് join ചെയ്യൂ എന്നിട്ട് വീണ്ടും start കൊടുക്കൂ 🙏**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=f"https://t.me/{force_channel}")]
              ])
            )
            return
        else:
            await message.reply_photo(
                photo="https://telegra.ph/file/2e2a07e86066538ed7406.jpg",
                caption=f"""👋 Hai {message.from_user.mention} \n𝙸'𝚖 𝙰 𝚂𝚒𝚖𝚙𝚕𝚎 𝙵𝚒𝚕𝚎 𝚁𝚎𝚗𝚊𝚖𝚎+𝙵𝚒𝚕𝚎 𝚃𝚘 𝚅𝚒𝚍𝚎𝚘 𝙲𝚘𝚟𝚎𝚛𝚝𝚎𝚛 𝙱𝙾𝚃 𝚆𝚒𝚝𝚑 𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 𝙰𝚗𝚍 𝙲𝚞𝚜𝚝𝚘𝚖 𝙲𝚊𝚙𝚝𝚒𝚘𝚗 𝚂𝚞𝚙𝚙𝚘𝚛𝚝! \n𝙱𝙾𝚃 𝙲𝚛𝚎𝚊𝚝𝚎𝚍 𝙱𝚢: @mr_MKN & @Mr_MKN_TG \n 🤩""",
                reply_markup=InlineKeyboardMarkup( [[
                    InlineKeyboardButton("👨‍💻 OWNER 👨‍💻", url='https://t.me/mr_MKN')
                    ],[
                    InlineKeyboardButton('📢up channel📢', url='https://t.me/mkn_bots_updates'),
                    InlineKeyboardButton('ℹ️help groupℹ️', url='https://t.me/MKN_BOTZ_DISCUSSION_GROUP')
                    ]]
                    )
                )
        return

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename ",callback_data = "rename")
       ,InlineKeyboardButton("Cancel✖️",callback_data = "cancel")  ]]))
