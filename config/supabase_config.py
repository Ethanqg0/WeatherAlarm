from supabase import create_client
from dotenv import load_dotenv

def create_supabase_client():
    load_dotenv()
    url = "https://wonclqrwdjpiodpgwbgs.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndvbmNscXJ3ZGpwaW9kcGd3YmdzIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ1NzI0OTAsImV4cCI6MjAxMDE0ODQ5MH0.fMJHVn5ECaWJA7pn18oPreKTCwtBS7g32N_M4NH55A8"
    return create_client(url, key)
