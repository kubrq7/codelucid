import os

class Config:
    SECRET_KEY = os.environ.get("CODELUCID_SECRET_KEY", "codelucid-elite-session-key-2026")
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    MAX_CONTENT_LENGTH = 64 * 1024  # 64KB max request for security
    
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
