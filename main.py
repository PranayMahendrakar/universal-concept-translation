#!/usr/bin/env python3
"""Universal Concept Translation Framework - Author: Pranay M"""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.markdown import Markdown
from modules import *

console = Console()

def main():
    console.print(Panel("🌐 UNIVERSAL CONCEPT TRANSLATION FRAMEWORK 🌐\nBridging Cognitive Architectures", style="bold green"))
    mods = [("Concept Analysis", ConceptAnalyzer()), ("Architecture Mapping", ArchitectureMapper()),
            ("Translation", TranslationEngine()), ("Semantic Bridges", SemanticBridgeBuilder()),
            ("Fidelity Assessment", FidelityAssessor()), ("Alien Concepts", AlienConceptHandler()),
            ("Universal Grammar", UniversalGrammarFinder()), ("Context Adaptation", ContextAdapter()),
            ("Interface Design", InterfaceDesigner()), ("Validation", TranslationValidator())]
    while True:
        table = Table(title="Translation Modules")
        for i,(n,_) in enumerate(mods,1): table.add_row(str(i),n)
        table.add_row("0","Exit")
        console.print(table)
        c = Prompt.ask("Select", choices=[str(i) for i in range(len(mods)+1)])
        if c == "0": break
        query = Prompt.ask("Input")
        m = mods[int(c)-1][1]
        result = m.analyze(query) if hasattr(m,'analyze') else m.map_architecture(query) if hasattr(m,'map_architecture') else m.translate(query,"system1","system2") if hasattr(m,'translate') else m.build_bridge(query,"system2") if hasattr(m,'build_bridge') else m.assess_fidelity(query,"translation") if hasattr(m,'assess_fidelity') else m.handle_alien(query) if hasattr(m,'handle_alien') else m.find_grammar(query) if hasattr(m,'find_grammar') else m.adapt_context(query,"context") if hasattr(m,'adapt_context') else m.design_interface(query) if hasattr(m,'design_interface') else m.validate(query)
        console.print(Panel(Markdown(result), title=mods[int(c)-1][0], border_style="green"))

if __name__ == "__main__": main()
