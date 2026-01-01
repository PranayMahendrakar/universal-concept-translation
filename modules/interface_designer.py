"""Interface Designer - Design translation interfaces"""
from .base import LlamaClient
class InterfaceDesigner:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "Expert in cognitive interface design."
    def design_interface(self, systems: str, requirements: str = "") -> str:
        return self.client.generate(f"Design translation interface:\nSystems: {systems}\nRequirements: {requirements}\nSpecify: 1. Interface Architecture 2. Input Processing 3. Output Format 4. User Experience 5. Error Handling 6. Feedback Mechanisms 7. Learning Integration 8. Scalability", self.system_prompt)
