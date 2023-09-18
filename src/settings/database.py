import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from supabase import create_client, Client

supabase_url: str = os.environ.get("supabase_url")
supabase_key: str = os.environ.get("supabase_key")

client: Client = create_client(supabase_url, supabase_key)
