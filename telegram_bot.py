# =========================
# APP
# =========================

print("CREATING APP")

app = ApplicationBuilder().token(
    TELEGRAM_BOT_TOKEN
).build()

print("ADDING HANDLERS")

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CommandHandler("memory", memory)
)

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        chat
    )
)

print("STARTING POLLING")

app.run_polling()
