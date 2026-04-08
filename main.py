from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# BOT TOKEN (Railway से आएगा)
BOT_TOKEN = "8610192884:AAEAhG02sIg7pa92Xi1CAdT0HupEpz1NU1E"

# Razorpay Links (अपना link डालना)
PLAN_1 = "https://rzp.io/rzp/Oa0lD2k"
PLAN_2 = "https://rzp.io/rzp/Oa0lD2k"
PLAN_3 = "https://rzp.io/rzp/Oa0lD2k"

# Private Channel Link
CHANNEL_LINK = "https://t.me/+DDu98ooLzFBkOWI1"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 7 Days - ₹149", callback_data='plan1')],
        [InlineKeyboardButton("⚡ 15 Days - ₹299", callback_data='plan2')],
        [InlineKeyboardButton("💎 1 Month - ₹499", callback_data='plan3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo="https://kommodo.ai/i/yWVCuf7STFOXSuIXUnus",
        caption="💰 Choose Your Subscription Plan",
        reply_markup=reply_markup
    )

# Button click
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "plan1":
        await query.message.reply_text(f"💳 Pay here:\n{PLAN_1}")
    elif query.data == "plan2":
        await query.message.reply_text(f"💳 Pay here:\n{PLAN_2}")
    elif query.data == "plan3":
        await query.message.reply_text(f"💳 Pay here:\n{PLAN_3}")

    await query.message.reply_text("✅ Payment hone ke baad /done likho")

# Done command
async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🎉 Payment Confirmed!\n\n👉 Join your private channel:\n{CHANNEL_LINK}"
    )

# App start
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(CommandHandler("done", done))

print("Bot is running...")
app.run_polling()
