from dotenv import load_dotenv
# from openai import OpenAI, BadRequestError, AuthenticationError, RateLimitError
import ollama
import os

# Load environment variables from .env file
load_dotenv()

# read API key After loading .env file
# api_key = os.getenv('OPENAI_API_KEY')

# client= OpenAI(api_key = api_key)

"""
SYSTEM_PROMPT = (
    "You are a financial document question-answering system. "
    "STRICT RULES:"
    "- Answer ONLY the exact question asked."
    "- Use ONLY the provided context."
    "- DO NOT rephrase the question."
    "- DO NOT explain your reasoning."
    "- DO NOT provide background or interpretations."
    "- If the answer is not explicitly stated, reply exactly:"
    "  'Not disclosed in documents.'"
)"""

import subprocess
import json

def generate_answer(prompt: str) -> str:
    try:
        process = subprocess.run(
            ["ollama", "run", "gemma3:1b"],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        if process.returncode != 0:
            return "⚠️ LLM execution failed."

        return process.stdout.strip()

    except Exception as e:
        return f"⚠️ Ollama error: {e}"

'''
    except BadRequestError as e:
        print("OPENAI BAD REQUEST:", e)
        return "OpenAI BadRequestError – check prompt or model."

    except AuthenticationError as e:
        print("OPENAI AUTH ERROR:", e)
        return "OpenAI AuthenticationError – API key issue."

    except RateLimitError as e:
        print("OPENAI RATE LIMIT:", e)
        return "OpenAI RateLimitError – quota exceeded."

    except Exception as e:
        print("UNKNOWN OPENAI ERROR:", e)
        return "Unknown OpenAI error."
        '''