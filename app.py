# pip install openai
# pip install gradio

import os

os.system('pip install openai')
os.system('pip install gradio')

import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=4, label="Chatbot with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="I can help you with anything you ask",
             theme="compact").launch(share=True)