import json
import urllib.request
from urllib.error import HTTPError, URLError

url = "https://api.github.com/users/praisemuochukwu789/events"

# GitHub requires a User-Agent header, otherwise it blocks default requests
req = urllib.request.Request(url, headers={"User-Agent": "Python-CLI-App"})

try:
  with urllib.request.urlopen(req) as response:
    # Read the raw bytes, decode to string, and parse into Python data
    data = json.loads(response.read().decode("utf-8"))
    print(f"Successfully fetched {len(data)} events!")

    # Peek at the first event to make sure it's working
    if data:
      print(f"Latest event type: {data[0]['type']}")
      
except HTTPError as e:
    # Catches explicit server responses like 404 Not Found or 500 Server Error
    print(f"HTTP Error code: {e.code}")
except URLError as e:
    # Catches low-level failures, like failing to connect to the internet entirely
    print(f"Failed to reach the server. Reason: {e.reason}")
except Exception as e:
  print(f"An error occurred: {e}")