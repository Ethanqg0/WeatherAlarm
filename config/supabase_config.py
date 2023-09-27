import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
Client = create_client(url, key)

def get_quotes():
    quotes = Client.table("quotes").select("*").execute().data
    print(quotes)

get_quotes()