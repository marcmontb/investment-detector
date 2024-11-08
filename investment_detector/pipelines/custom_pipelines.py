from typing import List, Callable
from ..core.types import Email, AnalysisResult

class Pipeline:
    def __init__(self):
        self.steps: List[Callable] = []

    def add_step(self, step: Callable):
        self.steps.append(step)

    async def execute(self, input_data: any) -> any:
        result = input_data
        for step in self.steps:
            result = await step(result)
        return result 