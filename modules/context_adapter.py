"""Context Adapter - Adapt translations to context"""
from .base import LlamaClient
class ContextAdapter:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "Expert in context-sensitive translation."
    def adapt_context(self, translation: str, target_context: str) -> str:
        return self.client.generate(f"Adapt to context:\nTranslation: {translation}\nTarget Context: {target_context}\nAdapt: 1. Context Analysis 2. Relevant Adjustments 3. Cultural Factors 4. Technical Level 5. Purpose Alignment 6. Tone Adjustment 7. Final Adaptation 8. Verification", self.system_prompt)
