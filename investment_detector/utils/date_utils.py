from datetime import datetime, timezone
from typing import Optional

def parse_iso_date(date_string: str) -> datetime:
    return datetime.fromisoformat(date_string.replace('Z', '+00:00'))

def format_iso_date(dt: datetime) -> str:
    return dt.isoformat() 