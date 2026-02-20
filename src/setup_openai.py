import os
from dotenv import load_dotenv
from openai import OpenAI

# Load env variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def build_prompt(snapshot: str) -> str:
    return f"""
You are an expert in HPC I/O performance.

Analyze the following workflow execution snapshot and identify the I/O bottleneck.

Return your answer in this format:
- Bottleneck: <category>
- Explanation: <really short reasoning>

Snapshot:
{snapshot}
"""


def diagnose(snapshot: str, model: str = "gpt-4.1-mini") -> str:
    prompt = build_prompt(snapshot)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an HPC systems expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content


# Example usage
if __name__ == "__main__":
    snapshot = """
Workflow: Genomics Pipeline

Tasks:
- align_1, align_2, align_3 running concurrently
- High read/write on shared storage

Storage:
- Utilization: 95%
- Throughput much lower than capacity

"""

    result = diagnose(snapshot)
    print(result)