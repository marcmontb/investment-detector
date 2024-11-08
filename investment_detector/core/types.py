from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class Email:
    id: str
    subject: str
    sender: str
    received_date: datetime
    body: str
    attachments: List[str]

@dataclass
class AnalysisResult:
    email_id: str
    investment_probability: float
    key_points: List[str]
    summary: str
    detected_companies: List[str] 