import os
from supabase import create_client, Client
from dotenv import load_dotenv

def create_supabase_client():
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    return create_client(url, key)
