from github import Github
import datetime

GITHUB_TOKEN = ""


REPO_NAME = "facebook/react"


g = Github(GITHUB_TOKEN)


repo = g.get_repo(REPO_NAME)


events = repo.get_events()


user_times = {}


for event in events:
    username = event.actor.login
    event_time = event.created_at

    if username not in user_times:
        
        user_times[username] = {
            "last_event_time": event_time,
            "total_time": 0
        }
    else:
        
        last_event_time = user_times[username]["last_event_time"]
        time_diff = last_event_time - event_time
        minutes_diff = time_diff.total_seconds() / 60 

        
        user_times[username]["total_time"] += minutes_diff
        user_times[username]["last_event_time"] = event_time


sorted_user_times = sorted(user_times.items(), key=lambda x: x[1]['total_time'], reverse=True)


for user, data in sorted_user_times:
    print(f"Usuário: {user}, Tempo estimado total: {data['total_time']:.2f} minutos")







from github import Github
import datetime

GITHUB_TOKEN = ""


REPO_NAME = "microsoft/TypeScript"


g = Github(GITHUB_TOKEN)


repo = g.get_repo(REPO_NAME)


events = repo.get_events()


user_times = {}


for event in events:
    username = event.actor.login
    event_time = event.created_at

    if username not in user_times:
        
        user_times[username] = {
            "last_event_time": event_time,
            "total_time": 0
        }
    else:
        
        last_event_time = user_times[username]["last_event_time"]
        time_diff = last_event_time - event_time
        minutes_diff = time_diff.total_seconds() / 60 

        
        user_times[username]["total_time"] += minutes_diff
        user_times[username]["last_event_time"] = event_time


sorted_user_times = sorted(user_times.items(), key=lambda x: x[1]['total_time'], reverse=True)


for user, data in sorted_user_times:
    print(f"Usuário: {user}, Tempo estimado total: {data['total_time']:.2f} minutos")

