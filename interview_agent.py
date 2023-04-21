from generative_agent import GenerativeAgent

__all__ = ['interview_agent']

USER_NAME="gaogao"

def interview_agent(agent: GenerativeAgent, message: str) -> str:
    """Help the notebook user interact with the agent."""
    new_message = f"{USER_NAME} says {message}"
    return agent.generate_dialogue_response(new_message)[1]
