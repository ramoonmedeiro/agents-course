import requests
from dotenv import load_dotenv, find_dotenv
import os
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_sync_playwright_browser

# langchain
from langchain.agents import Tool


load_dotenv(find_dotenv())

chat_id = os.getenv("TELEGRAM_CHAT_ID")
token = os.getenv("TELEGRAM_TOKEN")

class AllTools:
    def __init__(self):
        pass

    def send_message(self, msg):
        """
        Função que manda mensagem para o telegram

        ----------
        parameters
        ----------

        msg: str
            - parâmetro contendo a mensagem que será enviada
        """
        data = {"chat_id": chat_id, "text": msg}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)


    def setup_playwright(self):
        sync_browser = create_sync_playwright_browser(headless=False)
        toolkit = PlayWrightBrowserToolkit.from_browser(sync_browser=sync_browser)
        tool_dict = {tool.name: tool for tool in toolkit.get_tools()}
        navigate_tool = tool_dict.get("navigate_browser")
        extract_text_tool = tool_dict.get("extract_text")
        return navigate_tool, extract_text_tool

    def get_all_tools(self):
        tool_notification = Tool(
        name="tool que notifica via telegram",
        func=self.send_message,
        description="Função que manda mensagem para o telegram"
    )
        
        navigate_tool, extract_text_tool = self.setup_playwright()
        all_tools = [tool_notification, navigate_tool, extract_text_tool]
        return all_tools


if __name__ == "__main__":
    # Rodando o browser e pegando o seu conteúdo
    navigate_tool, extract_text_tool = setup_playwright()
    navigate_tool.run({"url": "https://cnn.com"})
    text = extract_text_tool.run({})
    print(text)