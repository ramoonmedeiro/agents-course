# laanggraph
from langgraph.graph.message import add_messages

# typed
from typing import Annotated, TypedDict

class State(TypedDict):
    messages: Annotated[list, add_messages]