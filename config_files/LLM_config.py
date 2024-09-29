model = \
    {
        "Llama3.1 8B": {
            "access": "local",
            "platform": "Ollama",
            "model": "llama3.1",
        },
        "Llama3.1 8B instruct-q8": {
            "access": "local",
            "platform": "Ollama",
            "model": "llama3.1:8b-instruct-q8_0",
        },
        "Llama3.1 8B instruct-fp16": {
            "access": "local",
            "platform": "Ollama",
            "model": "llama3.1:8b-instruct-fp16",
        },
        "Llama3.1 70B instruct-q3_K_M": {
            "access": "local",
            "platform": "Ollama",
            "model": "llama3.1:70b-instruct-q3_K_M",
        }
    }

platform = \
    {
    "Ollama":
        {
            "model_field": "model",
            "role_field": "role",
            "content_field": "content"
        }
    }