import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def generate_answer(question, retrieved_chunks):
    context = "\n\n".join(chunk["text"] for chunk in retrieved_chunks)

    prompt = f"""
Answer the question using ONLY the context below.
If the answer is not found, say you do not have enough information.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()
