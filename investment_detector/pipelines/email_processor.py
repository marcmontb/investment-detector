from ..core.analyzer import EmailAnalyzer
from ..core.summarizer import EmailSummarizer
from ..integrations.msgraph_client import MSGraphClient
from ..integrations.airtable_client import AirtableClient

class EmailProcessor:
    def __init__(self):
        self.analyzer = EmailAnalyzer()
        self.summarizer = EmailSummarizer()
        self.msgraph_client = MSGraphClient()
        self.airtable_client = AirtableClient()

    async def process_emails(self):
        # TODO: Implement email processing pipeline
        pass 