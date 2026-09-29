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