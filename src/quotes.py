from config.supabase_config import *
import dotenv

dotenv.load_dotenv()

def get_clients():
    clients = Client.table("clients").select("*").execute().data
    return clients

def get_quotes():
    quotes = Client.table("quotes").select("*").execute().data
    return quotes

def get_clients_quotes():
    quotes = Client.table("clients").select("quotes").execute().data
    return quotes

def isGeneral(user_quote):
    if user_quote["isGeneral"] == "TRUE":
        return True
    else:
        return False
    
def isUnique(user_quote, quote):
    clients_quotes = get_clients_quotes()
    for quote in clients_quotes:
        #check to see if user_quote and quotes are in the same clientquote meaning that its already been sent
        if user_quote["id"] == quote["clientID"] and quote["quoteID"] == quote["quoteID"]:
            return False
        
    return True
        




