import os

i = 1
while i < 11:
    # Create or modify a file here (optional, based on your use case)
    # For example: open("file.txt", "w").write(f"Change {i}")
    
    # Stage all changes
    os.system("git add .")
    
    # Commit with a message based on the loop index
    os.system(f'git commit -m "Commit number {i}"')
    
    # Push to the main branch
    os.system("git push origin main")
    
    i += 1
