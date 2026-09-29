import os

from dotenv import load_dotenv
from groq import Groq
from hindsight_client import Hindsight

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

print("SCRIPT STARTED")

# =========================
# LOAD ENV
# =========================

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")
HINDSIGHT_BANK_ID = os.getenv("HINDSIGHT_BANK_ID")

print("TOKEN FOUND:", TELEGRAM_BOT_TOKEN is not None)
print("GROQ KEY FOUND:", GROQ_API_KEY is not None)
print("HINDSIGHT KEY FOUND:", HINDSIGHT_API_KEY is not None)
print("BANK ID:", HINDSIGHT_BANK_ID)

# =========================
# GROQ
# =========================

client = Groq(
    api_key=GROQ_API_KEY
)

# =========================
# HINDSIGHT
# =========================

hindsight = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=HINDSIGHT_API_KEY
)

# =========================
# START COMMAND
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    print("/start RECEIVED")

    await update.message.reply_text(
        "Deal Intelligence Agent is active.\n\n"
        "Commands:\n"
        "/memory - View stored memory"
    )

# =========================
# MEMORY COMMAND
# =========================

async def memory(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        print("/memory RECEIVED")

        recalled = await hindsight.arecall(
            bank_id=HINDSIGHT_BANK_ID,
            query="people companies commitments preferences objections followups",
            max_tokens=2000
        )

        memory_text = str(recalled)

        print("HINDSIGHT MEMORY:")
        print(memory_text)

        if not memory_text:
            memory_text = "No memories found."

        await update.message.reply_text(
            memory_text[:4000]
        )

    except Exception as e:

        print("MEMORY ERROR:", e)

        await update.message.reply_text(
            f"Memory Error:\n{e}"
        )

# =========================
# CHAT
# =========================

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        user_message = update.message.text

        print("MESSAGE RECEIVED:", user_message)

        # ---------- RECALL ----------

        recalled = await hindsight.arecall(
            bank_id=HINDSIGHT_BANK_ID,
            query=user_message,
            max_tokens=1500
        )

        memory_context = str(recalled)

        print("MEMORY RETRIEVED")
        print(memory_context)

        # ---------- SYSTEM PROMPT ----------

        system_prompt = f"""
You are a Deal Intelligence Agent.

You track:

- People
- Companies
- Commitments
- Objections
- Competitors
- Follow-ups

Use memory whenever relevant.

Memory from Hindsight:

{memory_context}
"""

        # ---------- LLM ----------

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        answer = response.choices[0].message.content

        # ---------- STORE MEMORY ----------

        await hindsight.aretain(
            bank_id=HINDSIGHT_BANK_ID,
            content=user_message
        )

        print("MEMORY STORED")

        # ---------- BUILD PROOF ----------

        proof = ""

        try:

            if hasattr(recalled, "results"):

                proof += "\n\n---\n"
                proof += "🧠 Hindsight Memory Used:\n"

                for i, item in enumerate(recalled.results[:5], start=1):

                    text = getattr(item, "text", "")

                    proof += f"\n{i}. {text[:120]}"

        except Exception as proof_error:

            print("PROOF ERROR:", proof_error)

        final_reply = answer + proof

        # ---------- SEND ----------

        await update.message.reply_text(final_reply)

        print("REPLY SENT")

    except Exception as e:

        print("CHAT ERROR:", e)

        await update.message.reply_text(
            f"ERROR:\n{str(e)}"
        )