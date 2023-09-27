from config.supabase_config import *
import dotenv

dotenv.load_dotenv()


def get_clients_quotes():
    quotes = Client.table("clients").select("quotes").execute().data
    return quotes

