# internal tools
from tools import AllTools
from graph_state import State

# Nodes
from nodes import chatbot_node

# langgraph
from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver


class GraphConstructor:
    def __init__(self):
        self.all_tools = AllTools().get_all_tools() 
        self.graph_builder = StateGraph(State)

    def create_graph(self):
        # add nodes
        self.graph_builder.add_node("chatbot_node", chatbot_node)
        self.graph_builder.add_node("tools_node", ToolNode(tools=self.all_tools))

        # add conditional edge
        self.graph_builder.add_conditional_edges(
            "chatbot_node",
            tools_condition,
            {"tools": "tools_node", "__end__": "__end__"}
        )

        # add normal edges
        self.graph_builder.add_edge("tools_node", "chatbot_node")
        self.graph_builder.add_edge(START, "chatbot_node")
        return self.graph_builder
    
    def compile_graph(self):
        memory = MemorySaver()
        graph = self.create_graph().compile(checkpointer=memory)
        return graph