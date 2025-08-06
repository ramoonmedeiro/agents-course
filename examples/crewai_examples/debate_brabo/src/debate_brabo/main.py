#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from debate_brabo.crew import Debate

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'proposta': 'Proposta sobre quem é o maior jogador da NBA (O GOAT)'
    }
    
    try:
        final_result = Debate().crew().kickoff(inputs=inputs)
        print(final_result.raw)
    except Exception as e:
        raise Exception(f"Um erro aconteceu com o crew: {e}")
