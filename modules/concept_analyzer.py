"""Concept Analyzer - Analyze concepts across cognitive systems"""
from .base import LlamaClient
class ConceptAnalyzer:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "Expert in concept theory and cross-system analysis."
    def analyze(self, concept: str, system: str = "") -> str:
        return self.client.generate(f"Analyze concept: {concept}\nCognitive System: {system}\nProvide: 1. Concept Structure 2. Core Properties 3. Relations 4. Boundaries 5. Variations 6. Universal Aspects 7. System-Specific Aspects 8. Translation Challenges", self.system_prompt)
