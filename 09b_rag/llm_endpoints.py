def prompt_ollama(prompt:str, model="gemma3:12b"):
    """A prompt helper function that sends a prompt to 
    ollama and returns only the text response."""
    import openai
    # setup connection to the LLM server
    client = openai.OpenAI(
        base_url = "http://localhost:11434/v1",
        api_key = "none" # not required by ollama
    )
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    
    # extract answer
    return response.choices[0].message.content
