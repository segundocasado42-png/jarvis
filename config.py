# Configuration file for Jarvis AI Assistant

import os
from dotenv import load_dotenv

load_dotenv()

# Jarvis Configuration
JARVIS_NAME = "Jarvis"
JARVIS_LANGUAGE = "es"  # es for Spanish, en for English
JARVIS_VERSION = "1.0.0"

# API Keys (set in .env file)
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# Voice Configuration
VOICE_SPEED = 150  # Words per minute
VOICE_VOLUME = 1.0  # 0.0 to 1.0
VOICE_RATE = 1.0

# Speech Recognition
RECOGNITION_TIMEOUT = 10  # seconds
RECOGNITION_PHRASE_TIME_LIMIT = 15  # seconds

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Create directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# Features
FEATURES = {
    "voice_input": True,
    "voice_output": True,
    "web_search": True,
    "weather": True,
    "news": True,
    "system_control": True,
    "wikipedia": True,
    "youtube": True,
    "notes": True,
    "tasks": True,
}
