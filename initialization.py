from google import genai
from google.genai.types import (
    GenerateContentConfig,
    SafetySetting,    
)

# Initialize LLM
def initialize_llm_vertex(project_id,region,model_name,max_output_tokens,temperature,top_p):
    
    client = genai.Client(vertexai=True, project=project_id, location=region)

    # https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters
    safety_settings = [
        SafetySetting(
            category="HARM_CATEGORY_HATE_SPEECH",
            threshold="BLOCK_ONLY_HIGH",
        ),
        SafetySetting(
            category="HARM_CATEGORY_DANGEROUS_CONTENT",
            threshold="OFF",
        ),
        SafetySetting(
            category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
            threshold="BLOCK_ONLY_HIGH",
        ),
        SafetySetting(
            category="HARM_CATEGORY_HARASSMENT",
            threshold="BLOCK_ONLY_HIGH",
        ),
    ]
    generation_config = GenerateContentConfig(temperature=temperature,
                                     top_p=top_p,
                                     max_output_tokens=max_output_tokens,)
    return client, safety_settings,generation_config