from agents import Agent

PROMPT = """
Tu objetivo es unicamente ayudar a los usuarios a escribir correos electrónicos, artículos o incluso novelas. Sugiere oraciones, corrige gramática y estilo, o incluso genera texto completo basado en un tema o idea proporcionada por el usuario. 
"""

class MainAgent:
    def __init__(self):
        self.agent = None

    def get_agent(self):
        if not self.agent:
            self.create_agent()
        return self.agent

    def create_agent(self):
        try:
            self.agent = Agent(
                name="Writing assistant",
                instructions=PROMPT,
                model="gpt-4o-mini"  # Si se requiere se puede cambiar por otro modelo
            )
            return self.agent
        except Exception as e:
            return str(e)