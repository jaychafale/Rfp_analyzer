import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def call_gemini(prompt: str) -> dict:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        result = model.generate_content(prompt)
        text_response = result.text.strip()

        # Strip markdown-style formatting
        if text_response.startswith("```json"):
            text_response = text_response.replace("```json", "").replace("```", "").strip()

        return json.loads(text_response)

    except json.JSONDecodeError:
        return {
            "error": "Gemini response could not be parsed as JSON.",
            "raw_response": result.text
        }
    except Exception as e:
        return {
            "error": str(e)
        }


def call_gemini_embedding(text: str) -> list[float]:
    try:
        import google.generativeai as genai
        from dotenv import load_dotenv
        import os

        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        print(f"🔐 Using Gemini API key: {'FOUND' if api_key else 'NOT FOUND'}")

        genai.configure(api_key=api_key)

        result = genai.embed_content(
            model="models/embedding-001",
            content=text,
            task_type="retrieval_document"
        )

        return result["embedding"]
    except Exception as e:
        print("❌ Embedding error:", e)
        return []


