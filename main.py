from browser_use import Agent, ChatOpenAI
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

# Get API key from https://modelstudio.console.alibabacloud.com/?tab=playground#/api-key
api_key = os.getenv('ALIBABA_CLOUD')
base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

llm = ChatOpenAI(model='qwen-vl-max', api_key=api_key, base_url=base_url)

async def main():
    agent = Agent(
        task="搜索稀土掘金上关于人工智能的热门问题，并总结回答。",
        llm=llm,
        use_vision=True
    )
    result = await agent.run()
    print('result:', result)

if __name__ == "__main__":
    asyncio.run(main())