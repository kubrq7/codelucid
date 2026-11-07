import os

class Config:
    SECRET_KEY = os.environ.get("CODELUCID_SECRET_KEY", "codelucid-elite-session-key-2026")
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    MAX_CONTENT_LENGTH = 64 * 1024  # 64KB max request for security
    
    # Mail Configuration
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('GMAIL_USER')
    MAIL_PASSWORD = os.environ.get('GMAIL_PASS')

    MAIL_DEFAULT_SENDER = ("CodeLucid", "codelucid.contact@gmail.com")

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False