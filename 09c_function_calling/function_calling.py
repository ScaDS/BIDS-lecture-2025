def function_to_dict(func):
    """
    Takes a function definition and turns it into a dictionary, which later can be stored as json.
    
    The function should have a docstring explaining what the function can be used for and the parameters should have type definitions.
    """
    import inspect
    
    # Extracting function details
    func_name = func.__name__
    func_doc = func.__doc__.strip() if func.__doc__ else ""
    sig = inspect.signature(func)
    
    # Parsing parameters
    params = {
        "type": "object",
        "properties": {},
        "required": []
    }
    
    for name, param in sig.parameters.items():
        param_type = str(param.annotation) if param.annotation != inspect._empty else "unknown"
        params["properties"][name] = {
            "type": param_type.lower() if isinstance(param_type, str) else str(param_type).lower()
        }
        if param.default == inspect._empty:
            params["required"].append(name)
    
    # Constructing the dictionary structure
    func_dict = {
        "type": "function",
        "function": {
            "name": func_name,
            "description": func_doc,
            "parameters": params
        }
    }
    
    return func_dict


def call_function_from_response(response, named_tools, verbose=False):
    """
    Takes a response-string from ollama/mistral raw mode, extracts a function to be called and its parameters and calls the function.
    The function must be in the dictionary named_tools where keys are names of functions and values are the corresponding functions.
    """
    import json
    
    first_entry = json.loads(response)

    func = named_tools[first_entry["name"]]
    arguments = first_entry["arguments"]
    
    if verbose:
        print("calling", func.__name__, "with", arguments)
    
    result = func(**arguments)
    
    return result


def prompt_ollama(message, endpoint:str= "http://localhost:11434/api/generate", model:str="mistral:v0.3", tools=None, verbose=False):
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
        messages=[{"role": "user", "content": message}],
        tools=tools
    )
    
    if verbose:
        print("reponse:", response)
    
    # extract answer
    return response.choices[0].message.content, response.choices[0].message.tool_calls

    
def act(prompt:str, tools:list, verbose=False):
    """
    Takes a prompt and a list of function tools, and turns it into a prompt to a function-calling capable language model.
    If the model can select a function to call considering the prompt, this function will be called.
    """
    # get a dictionary with names of functions as keys, and corresponding functions as values
    named_tools = {f.__name__: f for f in tools}
    
    # convert the functions to json
    #json_text = function_list_to_json(tools)
    
    # assamble the prompt together with the list of available functions.
    #my_prompt = f"""
    #[AVAILABLE_TOOLS]{json_text}[/AVAILABLE_TOOLS][INST] {prompt} [/INST]
    #"""
    
    # submit the prompt
    answer, tool_calls = prompt_ollama(prompt, tools=[function_to_dict(f) for f in tools])
    first_tool_call = tool_calls[0].function.arguments
 
    if verbose:
        print("answer", answer)
        print("call", first_tool_call)
    
    # call the function as specified in the response
    return call_function_from_response(first_tool_call, named_tools)
