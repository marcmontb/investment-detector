from .types import Email
from ..integrations.mistral_client import MistralClient

class EmailSummarizer:
    def __init__(self):
        self.mistral_client = MistralClient()

    async def summarize(self, email: Email) -> str:
        # TODO: Implement email summarization logic
        pass 