1. Login & Account System

✔ Store users in users.txt
✔ Format per line:

username | hashed_password


⚠ Do NOT store plain password. You’ll use hashlib.sha256()
(Makes it real-world level)

2. User File Structure

Instead of only username.txt, let’s split for organization:

{username}_pending.txt → tasks not done

{username}_completed.txt → tasks done

This separation makes operations clean.

3. Task Priority Levels

When user adds a task, ask:

Enter task priority (High/Medium/Low):


Store like:

Buy milk | Low
Submit assignment | High

4. Deadlines (optional but recommended!)

Add date input:

Pay electricity bill | High | 2025-01-10

5. Sort Options

In main menu, add:

7. Sort tasks by priority
8. Sort tasks by deadline

🔐 6. Password Security (tiny addition)

When registering:

Hash password using SHA-256

Save hash, not original

Example hash use:

import hashlib

hashlib.sha256(password.encode()).hexdigest()

🤝 7. Delete v/s Complete

Your current "delete" means move to completed — good.

Add REAL delete from completed too:

Remove permanently from completed list (y/n)?