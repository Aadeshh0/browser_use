from browser_use.llm import ChatGoogle
from browser_use import Agent, BrowserSession
import asyncio

from dotenv import load_dotenv
load_dotenv()

browser = BrowserSession(
    executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS

    # Use a specific data directory on disk (optional, set to None for incognito)
    # user_data_dir='~/.config/browseruse/profiles/default',   # this is the default 
)

llm = ChatGoogle(
    model = 'gemini-2.5-flash', 
)

async def main():
    agent = Agent(
        task = 'compare the prices of samsung s25 ultra and iphone 15 pro max',
        llm = llm,
        browser = browser,
    )

    result = await agent.run()
    print(result)

asyncio.run(main())