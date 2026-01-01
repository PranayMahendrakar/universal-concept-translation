"""Translation Validator - Validate translations"""
from .base import LlamaClient
class TranslationValidator:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "Expert in translation validation."
    def validate(self, translation: str, criteria: str = "") -> str:
        return self.client.generate(f"Validate translation:\nTranslation: {translation}\nCriteria: {criteria}\nCheck: 1. Correctness 2. Completeness 3. Consistency 4. Clarity 5. Usability 6. Round-Trip Test 7. Expert Review 8. Certification", self.system_prompt)
