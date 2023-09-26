from config.supabase_config import *

def get_clients_quotes():
    quotes = Client.table("clients").select("quotes").execute().data
    return quotes

