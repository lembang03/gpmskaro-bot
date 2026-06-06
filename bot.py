from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ================= CONFIG =================

TOKEN = "7646397047:AAH6lmMsQUTUppO99jTip1xA7VKfL-nFXAc"

WELCOME_IMAGE = "https://ibb.co/Cszz3ST5"

WEBSITE_GPMS = "https://gpms.xo.je/"


# ================= START =================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🌿 MEJUAH-JUAH 🌿

Selamat datang di Bot Resmi

GPMS - TANAH KARO

Gunakan perintah berikut:
/help
/info
/aturan
/admin
"""

    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )


# ================= HELP =================

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📖 DAFTAR MENU

/help
/info
/aturan
/admin

Mejuah-Juah
"""

    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )


# ================= INFO =================

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
ℹ️ GPMS - TANAH KARO

Wadah silaturahmi,
persaudaraan,
dan kebersamaan masyarakat Karo.

Bersatu Dalam Persaudaraan
"""

    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )


# ================= ATURAN =================

async def aturan(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📜 ATURAN GRUP

Saling menghormati
Tidak spam
Tidak hoax
Tidak SARA
Jaga etika berdiskusi

Mari jaga kebersamaan bersama
"""

    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )


# ================= ADMIN =================

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "KUNJUNGI WEBSITE GPMS",
                url="https://gpms.xo.je/"
            )
        ]
    ]

    await update.message.reply_text(
        "Silakan kunjungi website resmi GPMS.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ================= MEMBER BARU =================

async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):

    for member in update.message.new_chat_members:

        user_id = member.id
        nama = member.full_name

        username = f"@{member.username}" if member.username else "Tidak Ada Username"

        text = f"""
🌿 𝙈𝙀𝙅𝙐𝘼𝙃-𝙅𝙐𝘼𝙃𝙃 🌿

𝐒𝐄𝐋𝐀𝐌𝐀𝐓 𝐃𝐀𝐓𝐀𝐍𝐆 𝐃𝐈 𝐆𝐑𝐔𝐏 𝐆𝐏𝐌𝐒 - 𝐓𝐀𝐍𝐀𝐇 𝐊𝐀𝐑𝐎

━━━━━━━━━━━━━━

ID : {user_id}
NAMA : {nama}
USERNAME : {username}

━━━━━━━━━━━━━━

𝐆𝐑𝐔𝐏 𝐈𝐍𝐈 𝐔𝐍𝐓𝐔𝐊 𝐌𝐄𝐍𝐉𝐀𝐋𝐈𝐍
𝐒𝐈𝐋𝐀𝐓𝐔𝐑𝐀𝐇𝐌𝐈 𝐃𝐀𝐍 𝐏𝐄𝐑𝐒𝐀𝐔𝐃𝐀𝐑𝐀𝐀𝐍.

𝙅𝘼𝙉𝙂𝘼𝙉 𝙍𝘼𝙂𝙐 𝙐𝙉𝙏𝙐𝙆 𝘽𝙀𝙍𝙆𝙀𝙉𝘼𝙇𝘼𝙉 𝘿𝘼𝙉 𝘽𝙀𝙍𝙋𝘼𝙍𝙏𝙄𝙎𝙄𝙋𝘼𝙎𝙄 𝘿𝘼𝙇𝘼𝙈 𝘿𝙄𝙎𝙆𝙐𝙎𝙄.


𝐓𝐄𝐑𝐈𝐌𝐀 𝐊𝐀𝐒𝐈𝐇 𝐓𝐄𝐋𝐀𝐇 𝐁𝐄𝐑𝐆𝐀𝐁𝐔𝐍𝐆 ❤️
"""

        keyboard = [
            [
                InlineKeyboardButton(
                    "KUNJUNGI WEBSITE GPMS",
                    url="https://gpms.xo.je/"
                )
            ]
        ]

        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=WELCOME_IMAGE,
            caption=text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# ================= ERROR HANDLER =================

async def error_handler(update, context):
    print(f"ERROR: {context.error}")


# ================= MAIN =================

def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("aturan", aturan))
    app.add_handler(CommandHandler("admin", admin))

    app.add_handler(
        MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member)
    )

    app.add_error_handler(error_handler)

    print("GPMS - TANAH KARO BOT AKTIF")

    app.run_polling()


if __name__ == "__main__":
    main()
