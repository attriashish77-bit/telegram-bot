{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww29200\viewh18460\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup\
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes\
\
BOT_TOKEN = "8610192884:AAEAhG02sIg7pa92Xi1CAdT0HupEpz1NU1E"\
\
# Razorpay Links\
PLAN_1 = "https://rzp.io/rzp/Oa0lD2k"\
PLAN_2 = "https://rzp.io/rzp/Oa0lD2k"\
PLAN_3 = "https://rzp.io/rzp/Oa0lD2k"\
\
CHANNEL_LINK = "https://t.me/+DDu98ooLzFBkOWI1"\
\
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    keyboard = [\
        [InlineKeyboardButton("\uc0\u55357 \u56613  7 Days - $1.99", callback_data='plan1')],\
        [InlineKeyboardButton("\uc0\u9889  15 Days - $3.99", callback_data='plan2')],\
        [InlineKeyboardButton("\uc0\u55357 \u56462  1 Month - $5.99", callback_data='plan3')],\
    ]\
\
    reply_markup = InlineKeyboardMarkup(keyboard)\
\
    await update.message.reply_photo(\
        photo="https://kommodo.ai/i/yWVCuf7STFOXSuIXUnus",\
        caption="\uc0\u55357 \u56496  *Choose Your Subscription Plan*",\
        parse_mode="Markdown",\
        reply_markup=reply_markup\
    )\
\
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    query = update.callback_query\
    await query.answer()\
\
    if query.data == "plan1":\
        await query.message.reply_text(f"Pay here:\\n\{PLAN_1\}")\
\
    elif query.data == "plan2":\
        await query.message.reply_text(f"Pay here:\\n\{PLAN_2\}")\
\
    elif query.data == "plan3":\
        await query.message.reply_text(f"Pay here:\\n\{PLAN_3\}")\
\
    await query.message.reply_text(\
        "\uc0\u9989  Payment complete hone ke baad 'DONE' likh kar send karein"\
    )\
\
async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    await update.message.reply_text(\
        f"\uc0\u55356 \u57225  Payment Verified!\\n\\nJoin your private channel:\\n\{CHANNEL_LINK\}"\
    )\
\
app = ApplicationBuilder().token(BOT_TOKEN).build()\
\
app.add_handler(CommandHandler("start", start))\
app.add_handler(CallbackQueryHandler(button))\
app.add_handler(CommandHandler("done", done))\
\
app.run_polling()}