import gradio as gr
import json
import os
from remembr.memory.milvus_memory import MilvusMemory
from remembr.memory.memory import MemoryItem
from remembr.agents.remembr_agent import ReMEmbRAgent

# 1. 填入你的大语言模型 API Key (这里以 OpenAI 为例，你也可以换成其他的)
os.environ["OPENAI_API_KEY"] = "123"

# 2. 连接本地免安装数据库 (Milvus Lite)
print("正在连接本地记忆库...")
memory = MilvusMemory("video_memory_collection")
memory.reset() # 每次启动清空旧记忆

# 3. 读取你的 JSON 文件
json_path = "./remembr/data/captions/0/captions/remembr/data/captions/0/captions/captions_Llama-3-VILA1.5-8b_3_secs.json" 
print(f"正在读取视频日记: {json_path}")

with open(json_path, 'r', encoding='utf-8') as f:
    captions_data = json.load(f)
    for item in captions_data:
        # 注意：如果你的 json 里时间字段叫 timestamp，就把 item['time'] 改成 item['timestamp']
        mem_item = MemoryItem(
            caption=item['caption'], 
            time=float(item.get('time', 0.0)),
            position=[0.0, 0.0, 0.0], 
            theta=0.0
        )
        memory.insert(mem_item)
print("记忆注入完成！")

# 4. 初始化 AI 大脑
agent = ReMEmbRAgent(llm_type='deepseek-chat')
agent.set_memory(memory)

# 5. 构建 Gradio 网页聊天界面
def chat_with_video(message, history):
    # 调用 agent 进行检索和回答
    response = agent.query(message)
    return response.text

print("正在启动 Web 界面...")
# share=True 是 AutoDL 必备，它会生成一个你可以直接在浏览器点开的公网链接
demo = gr.ChatInterface(
    fn=chat_with_video, 
    title="🤖 ReMEmbR 视频记忆助手",
    description="我已经看完了你的视频并记在脑子里了，想问点什么？"
)

if __name__ == "__main__":
    demo.launch(share=True, server_name="0.0.0.0")
