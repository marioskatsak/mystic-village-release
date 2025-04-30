# Mystic Village 🕊️

A narrative-driven mystic RPG API built with FastAPI.
You are the last soul-walker in a forgotten village.
The world changes each time you play.

## Features
- Random world generation
- Dynamic NPC interactions (soon AI-enhanced)
- Soul-based decision system
- Built for web and mobile frontends

## Setup
```bash
git clone https://github.com/yourusername/mystic-village.git
cd mystic-village
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoints
- `/` → Health check
- `/player` → Player info
- `/village` → Static village state
- `/npc/{id}` → Interact with an NPC
- `/generate_world` → Generate random world instance
- `/decision` → Handle player choice

## License
MIT
