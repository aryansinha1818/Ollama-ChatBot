from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"  # Fixed the typo in 'description'
)

# Initialize Ollama with llama2 model
llm = Ollama(model="llama2")

# Create prompt template
prompt = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} for a 5 year old child with 100 words"
)

# Add route
add_routes(
    app,
    prompt | llm,
    path="/poem",
    # Adding these helps OpenAPI documentation
    input_type=dict,
    config_keys=["tags"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
    