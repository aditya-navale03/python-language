import os
import subprocess
from datetime import datetime, timedelta
import random

# Configuration
REPO_NAME = "my-attractive-graph"
COMMIT_COUNT = 40

# Create and enter the repo directory
if not os.path.exists(REPO_NAME):
    os.mkdir(REPO_NAME)
os.chdir(REPO_NAME)

# Initialize git repo
subprocess.run(["git", "init"])

# Create a file to modify
with open("activity.txt", "w") as f:
    f.write("GitHub Contributions:\n")

# Starting date (40 days ago)
start_date = datetime.now() - timedelta(days=COMMIT_COUNT)

for i in range(COMMIT_COUNT):
    commit_date = start_date + timedelta(days=i)
    with open("activity.txt", "a") as f:
        f.write(f"Commit number {i+1}\n")
    
    # Git add and commit with custom date
    subprocess.run(["git", "add", "activity.txt"])
    env = os.environ.copy()
    formatted_date = commit_date.strftime("%Y-%m-%dT12:00:00")
    env["GIT_AUTHOR_DATE"] = formatted_date
    env["GIT_COMMITTER_DATE"] = formatted_date
    subprocess.run(["git", "commit", "-m", f"Commit {i+1}"], env=env)

print("✅ 40 commits done. Now run these commands manually to push it:")
print("cd", REPO_NAME)
print("git remote add origin <your_repo_url>")
print("git branch -M main")
print("git push -u origin main")
