import config
from llama_cpp import Llama

async def fetch_llm_reply(message):
    response = await get_alpaca_response(message)
    return response

async def get_alpaca_response(message):
    llm = Llama(model_path=config.modelpath)
    output = llm(f"Q: {message} A: ", max_tokens=20, stop=["Q:", "\n"], echo=True)
    message = output['choices'][0]['text']
    print (message)
    response = message.split("A: ")[1]
    return response