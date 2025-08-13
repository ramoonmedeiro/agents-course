# internal tools
from graph_constructor import GraphConstructor


class Chat:
    def __init__(self, thread_id: str):
        self.thread_id = thread_id
        self.graph = GraphConstructor().compile_graph()
        self.config = {"configurable": {"thread_id": self.thread_id}}

    def run_chat(self, user_input: str):
        result = self.graph.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            },
            config=self.config
        )

        return result["messages"][-1].content
    
if __name__ == "__main__":
    user_input="nada"
    chat = Chat(thread_id="1")
    while user_input != "bye":
        user_input = input("H: ")
        response_chat = chat.run_chat(user_input="Olá meu nome é ramon")
        print(chat)