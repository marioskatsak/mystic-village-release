from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# CORS setup for web/mobile frontend compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== WORLD GENERATOR ==========

def generate_world():
    village_names = ["Dourgouthion", "Koryfi", "Skotadi", "Ximeri", "Stagona"]
    weathers = ["foggy", "stormy", "raining ash", "silent", "sunless"]
    events = [
        "The lake whispers forgotten names.",
        "No sun will rise today.",
        "Birds fly backwards since dawn.",
        "Dreams bleed into the soil.",
        "The clock tower ticks counter to time."
    ]
    npcs = [
        {"id": 1, "name": "Elder Mira", "role": "memory keeper"},
        {"id": 2, "name": "Loros", "role": "outcast poet"},
        {"id": 3, "name": "Myra", "role": "child who never ages"}
    ]
    return {
        "village_name": random.choice(village_names),
        "weather": random.choice(weathers),
        "mystic_energy": random.randint(50, 100),
        "daily_event": random.choice(events),
        "npcs": random.sample(npcs, k=random.randint(1, len(npcs)))
    }

# ========== ROUTES ==========

@app.get("/")
def read_root():
    return {"message": "Mystic Village API is alive 🌿"}

@app.get("/player")
def get_player():
    return {"name": "Unnamed", "soul_points": 100, "memory_fragments": []}

@app.get("/village")
def get_village():
    return {"day": 1, "weather": "foggy", "mystic_energy": 73}

@app.get("/npc/{npc_id}")
def get_npc(npc_id: int):
    return {"id": npc_id, "name": "Elder Mira", "mood": "cryptic", "dialogue": ["The wind carries secrets.", "Not all memories are yours."]}

@app.post("/decision")
def make_decision(decision: dict):
    return {"result": "You chose the path of remembrance.", "soul_change": -10, "fragment_gained": "Father's Laugh"}

@app.get("/generate_world")
def get_generated_world():
    return generate_world()
