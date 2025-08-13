# internal tools
from tools import AllTools

# langchain
from langchain_groq import ChatGroq
from langchain_core.tools import BaseTool

# pydantic
from pydantic import BaseModel

# typing
from typing import List


class LLMWithTools(BaseModel):
    all_tools: List[BaseTool] = AllTools().get_all_tools()

    llm: ChatGroq = ChatGroq(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=0,
        max_tokens=300
    )

    llm_with_tools: ChatGroq = llm.bind_tools(all_tools)