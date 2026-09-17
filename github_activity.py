import json
import sys
import urllib.request
from urllib.error import HTTPError, URLError

# Check if the user provided a username in the terminal
if len(sys.argv) < 2:
  print("Please provide a username. Example: python github_activity.py praisemuochukwu789")
  sys.exit(1)

# Grab the username from the command-line arguments
username = sys.argv[1]
url = f"https://api.github.com/users/{username}/events"

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
      
      # Dictionaries to track your actions per repo
      repo_push_counts = {}
      repo_create_counts = {}

      for event in data:
        event_type = event["type"]
        repo_name = event["repo"]["name"]

        if event_type == "PushEvent":
          repo_push_counts[repo_name] = repo_push_counts.get(repo_name, 0) + 1

        elif event_type == "CreateEvent":
          # GitHub tells us if you made a repository, branch, or tag
          ref_type = event["payload"].get("ref_type", "unknown")
          repo_create_counts[repo_name] = repo_create_counts.get(repo_name, 0) + 1

      # Print out the push summaries
      for repo_name, push_count in repo_push_counts.items():
        print(f"- Pushed {push_count} time(s) to {repo_name}")

      # Print out the create summaries
      for repo_name, create_count in repo_create_counts.items():
        print(f"- Created {create_count} new item(s) in {repo_name}")

except HTTPError as e:
    # Catches explicit server responses like 404 Not Found or 500 Server Error
    print(f"HTTP Error code: {e.code}")
except URLError as e:
    # Catches low-level failures, like failing to connect to the internet entirely
    print(f"Failed to reach the server. Reason: {e.reason}")
except Exception as e:
  print(f"An error occurred: {e}")