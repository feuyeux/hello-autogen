import os
import pprint
from autogen import UserProxyAgent, AssistantAgent
os.environ['AUTOGEN_USE_DOCKER']='no'
local_llm_config = {
    "config_list": [
        {
            "model": "NotRequired",  # Loaded with LiteLLM command
            "api_key": "NotRequired",  # Not needed
            "base_url": "http://localhost:4000"  # Your LiteLLM URL
        }
    ],
    "cache_seed": None  # Turns off caching, useful for testing different models
}

assistant = AssistantAgent("assistant", llm_config=local_llm_config)
user_proxy = UserProxyAgent("user_proxy",
                            is_termination_msg=lambda x: x.get("content", "") 
                                and 
                                x.get("content","").rstrip().endswith("TERMINATE"),
                            human_input_mode="NEVER",
                            max_consecutive_auto_reply=5)

result = user_proxy.initiate_chat(assistant,
                                  message="编写一个同时支持windows和macos的shell脚本，用来查看当前文件夹下的文件及其属性")

pprint.pprint(result.summary)
pprint.pprint(result.chat_history)
pprint.pprint(result.cost)
