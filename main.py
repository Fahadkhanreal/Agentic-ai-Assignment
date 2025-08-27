from agents import Runner
from my_agent.agents import agent

import chainlit as cl





@cl.on_chat_start
async def main():
    await cl.Message("HI I am your Virtual Assistant").send()


@cl.on_message
async def msg(message:cl.Message):
   user_input = message.content
    
   result = Runner.run_sync(agent ,user_input)
   await cl.Message(result.final_output).send()







