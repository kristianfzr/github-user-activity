import requests
import os
import sys
from github_user_activity.auth import TokenAuth

def main():
    if len(sys.argv) < 2:
        print("Usage: github-user-activity <username>")
        sys.exit(1)
    
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set")
        sys.exit(1)
    
    user = sys.argv[1]
    
    response = requests.get(f"https://api.github.com/users/{user}/events",
                            auth=(TokenAuth(token)))
    data = response.json()

    if response.status_code == 200:
        print("Output: ")
        for event in data:
            event_type = event['type']
            repo_name = event['repo']['name']
            
            if event_type == 'PushEvent':
                print(f"- Pushed to {repo_name}")
                
            elif event_type == "IssuesEvent":
                action = event['payload']['action']
                print(f"- {action.capitalize()} a new issue in {repo_name}")
                
            elif event_type == "WatchEvent":
                print(f"- Starred {repo_name}")
                
            elif event_type == "ForkEvent":
                print(f"- Forked {repo_name}")
                
            elif event_type == "CreateEvent":
                ref_type = event['payload']['ref_type']
                print(f"- Created {ref_type} in {repo_name}")
                
            elif event_type == 'PullRequestEvent':
                action = event['payload']['action']
                print(f"- {action.capitalize()} a pull request in {repo_name}")
                
            elif event_type == 'PullRequestReviewEvent':
                print(f"- Reviewed pull request {event['payload']['pull_request']['number']} in {repo_name}")
                
            elif event_type == 'PullRequestReviewCommentEvent':
                print(f"- Commented on pull request {event['payload']['pull_request']['number']} in {repo_name}")
    else:
        print(f"Error fetching events for {user}: {response.status_code}")
        
if __name__ == "__main__":
    main()