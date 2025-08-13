from llms import LLMWithTools
from graph_state import State


def chatbot_node(old_state: State) -> State:
    llm_with_tools = LLMWithTools.llm_with_tools
    response = llm_with_tools.invoke(old_state["messages"])
    return {"messages": [response]}
