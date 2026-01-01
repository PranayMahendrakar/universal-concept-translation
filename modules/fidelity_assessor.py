"""Fidelity Assessor - Assess translation fidelity"""
from .base import LlamaClient
class FidelityAssessor:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "Expert in assessing translation accuracy."
    def assess_fidelity(self, original: str, translated: str) -> str:
        return self.client.generate(f"Assess translation fidelity:\nOriginal: {original}\nTranslated: {translated}\nEvaluate: 1. Semantic Preservation 2. Structural Preservation 3. Relational Preservation 4. Connotation Preservation 5. Loss Analysis 6. Gain Analysis 7. Overall Score 8. Improvements", self.system_prompt)
