import gradio as gr
import os
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3,
    api_key=GROQ_API_KEY,
    timeout=20,
)

prompt_template_str = """Explain {concept} in under 100 words for a {users_background}. Start with a simple definition, 
then explain the core idea using an intuitive analogy or practical example related to the user's background as {users_background} when relevant. 
Avoid unnecessary jargon; if a technical term is essential, define it briefly. Focus on what it is, how it works, and why it matters. 
Adapt the explanation subtly to the learner’s technical background and interests without explicitly mentioning personalization.
"""

prompt_template = PromptTemplate.from_template(prompt_template_str)


def generate_explanation(concept, users_background):
    prompt = prompt_template.format(
        concept=concept,
        users_background=users_background
    )
    
    response = model.invoke(prompt)

    return response.text


demo = gr.Interface(
    fn=generate_explanation,
    inputs=[
        gr.Textbox(label="Concept"),
        gr.Textbox(label="Your Background")
    ],
    outputs=gr.Textbox(label="Explanation")
)

demo.launch()