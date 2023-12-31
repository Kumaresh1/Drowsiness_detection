import os
import json
# from dotenv import load_dotenv
from supabase import create_client, Client
from datetime import datetime

#Replace with ur supabase
supabaseUrl = #Replace with ur supabase

supabaseKey = #Replace with ur supabase

secretKey = #Replace with ur supabase

supabase: Client = create_client(supabaseUrl, supabaseKey)


def insert_trip_details(tripId, name, image, flag):
    # url: str = os.environ.get("SUPABASE_URL", supabaseUrl)
    # key: str = os.environ.get("SUPABASE_KEY", supabaseKey)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    data = {
        'currentTime': current_time,
        'image': image,
        'threshold': flag,

    }
    supabase.table('trip_data').insert({
        'data': json.dumps(data),
        'name': name,
        'trip_id': tripId,

    }).execute()


def create_trip(name):

    response = supabase.from_("Blocked_users").select("*").execute()
    print(response)
    if len(response.data):
        data = response.data
        names = [item["name"].lower() for item in data]
        print(names, "Blocked users : ")
        if name.lower() in names:
            raise Exception("User is blocked! Can't proceed")

        # Handle the error appropriately
    res = supabase.table('trips').insert({
        'name': name
    }).execute()
    return res.data[0]['id']

# def main():
#     # load_dotenv()

#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
#     insert_trip_details(supabase, name, current_time)
