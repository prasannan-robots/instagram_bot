"""One-off InstaPy session (same as bot.py's job, without the scheduler)."""

from bot import job

if __name__ == "__main__":
    job()
