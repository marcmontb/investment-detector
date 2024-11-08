from typing import List
import aiohttp
from ..core.types import Email

class MSGraphClient:
    def __init__(self, client_id: str, client_secret: str, tenant_id: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id

    async def get_emails(self, folder: str = "inbox") -> List[Email]:
        # TODO: Implement email fetching logic
        pass 