from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FitMind AI Backend"
    mongodb_url: str = "mongodb+srv://rudraphoto21_db_user:idgOyjweq3sWp74b@cluster0.wudlybj.mongodb.net/fitmind_ai?appName=Cluster0"
    gemini_api_key: str = "AIzaSyBs7ZDysumUQfx8dx3LKc8w9KM0vuui3kk"
    jwt_secret_key: str = "your-secret-key"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440

settings = Settings()
