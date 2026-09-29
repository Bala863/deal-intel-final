# Deal Intelligence Agent

## Overview

Deal Intelligence Agent is a memory-powered AI assistant that tracks people, companies, commitments, preferences, objections, and follow-up actions.

The agent uses Hindsight persistent memory and a Groq-hosted LLM to remember important business information across conversations.

## Problem

Traditional AI assistants forget information once a conversation ends.

Sales teams and business professionals often lose track of:

- Customer preferences
- Follow-up commitments
- Meeting notes
- Prospect interests
- Important conversations

## Solution

This project combines:

- Telegram Bot
- Groq LLM
- Hindsight Memory

to create an AI agent that remembers information even after the application is restarted.

## Features

- Persistent memory
- People tracking
- Company tracking
- Commitment tracking
- Follow-up recommendations
- Memory recall after restart

## Example

User:
I met Rajesh from Microsoft. He likes technical discussions.

Later:

What do you remember about Rajesh?

Agent:
Rajesh works at Microsoft, enjoys technical discussions, and requested a proposal by October 5.

## Tech Stack

- Python
- Telegram Bot API
- Groq
- Hindsight
- GPT-OSS-120B

## Proof of Persistent Memory

The agent stores information using Hindsight memory banks.

After restarting the bot:

- Previously stored information remains available
- The agent recalls earlier conversations
- Responses become personalized using recalled memories

This demonstrates persistent memory beyond a single chat session.

## Future Improvements

- CRM integration
- Meeting preparation workflows
- Multi-user memory
- Email follow-up generation

- ## Architecture

```text
User
  │
  ▼
Telegram Bot
  │
  ▼
Deal Intelligence Agent
  │
  ├── Recall Memory → Hindsight
  │
  ├── Generate Response → Groq GPT-OSS-120B
  │
  └── Store New Facts → Hindsight
```

## Example Workflow

### Interaction 1

User:

> I met Rajesh from Microsoft. He likes technical discussions.

Agent:

> Noted. Rajesh works at Microsoft and enjoys technical discussions.

The information is stored in Hindsight.

### Interaction 2 (After Restart)

User:

> What do you remember about Rajesh?

Agent:

> Rajesh works at Microsoft, enjoys technical discussions, and has been discussed previously.

The memory survives application restarts because it is stored in Hindsight.

## Why Hindsight

Most AI assistants forget information once the session ends.

Hindsight provides persistent memory that allows the agent to:

- Remember people
- Track companies
- Recall commitments
- Store preferences
- Improve responses over time

This allows the agent to behave more like a long-term business assistant rather than a stateless chatbot.

## Persistent Memory Proof

The following workflow demonstrates persistence:

1. User shares information about a prospect.
2. Agent stores the information using Hindsight.
3. Application is stopped.
4. Application is restarted.
5. User asks about the prospect.
6. Agent recalls previously stored information.

This demonstrates memory persistence beyond a single runtime session.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_key
TELEGRAM_BOT_TOKEN=your_token
HINDSIGHT_API_KEY=your_key
HINDSIGHT_BANK_ID=your_bank_id
```

Run:

```bash
python telegram_bot.py
```
