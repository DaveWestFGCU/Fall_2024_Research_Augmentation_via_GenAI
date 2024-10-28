model = \
    {
        "Llama3.1 8B": {
            "id": "llama3.1",
            "access": "local",
            "platform": "Ollama",
        },
        "Llama3.1 8B instruct-q8": {
            "id": "llama3.1:8b-instruct-q8_0",
            "access": "local",
            "platform": "Ollama",
        },
        "Llama3.1 8B instruct-fp16": {
            "id": "llama3.1:8b-instruct-fp16",
            "access": "local",
            "platform": "Ollama",
        },
        "Llama3.1 70B instruct-q3_K_M": {
            "id": "llama3.1:70b-instruct-q3_K_M",
            "access": "local",
            "platform": "Ollama",
        },
        "Gemma2 27B": {
            "id": "gemma2:27b",
            "access": "local",
            "platform": "Ollama",
        },
        "Gemma2 9B": {
            "id": "gemma2",
            "access": "local",
            "platform": "Ollama",
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