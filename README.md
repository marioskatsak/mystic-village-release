# Mystic Village Full Project

## Structure

- backend/main.py
- frontend/components/*.js
- assets/models/*.glb
- assets/audio/*.wav
- scripts/deploy_vercel.sh
- scripts/eas.json
- scripts/push_to_github.sh

## Setup

### Backend
cd backend
pip install fastapi uvicorn openai python-dotenv
uvicorn main:app --reload

### Frontend
cd frontend
npm install @react-three/fiber @react-three/drei three react react-dom
npm start

### assets/models
Place .glb files in /assets/models

### Scripts
chmod +x scripts/*.sh