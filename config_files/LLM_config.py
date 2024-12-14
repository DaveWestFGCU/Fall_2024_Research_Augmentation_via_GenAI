model = \
    {
        "Llama3.1 8B instruct-q8": {
            "id": "llama3.1:8b-instruct-q8_0",
            "access": "local",
            "platform": "Ollama",
        },

        "Llama3.1 70B instruct-q3_K_M": {
            "id": "llama3.1:70b-instruct-q3_K_M",
            "access": "local",
            "platform": "Ollama",
        },

        "ChatGPT 4o-Mini": {
            "id": "gpt-4o-mini-2024-07-18",
            "access": "api",
            "platform": "OpenAI"
        },

        "ChatGPT 4o-Mini EmoEvent (Tokenized) Fine-Tuned": {
            "id": "ft:gpt-4o-mini-2024-07-18:florida-gulf-coast-university::AUIJ0Mfh",
            "access": "api",
            "platform": "OpenAI"
        }
    }

platform = \
    {
    "Ollama":
        {
            "model_field": "model",
            "role_field": "role",
            "content_field": "content"
        },
    "OpenAI":
        {
            "model_field": "model",
            "role_field": "role",
            "content_field": "content"
        }
    }