def numpy_to_bytestream(data):
    """Turn a NumPy array into a bytestream"""
    import numpy as np
    from PIL import Image
    import io

    # Convert the NumPy array to a PIL Image
    image = Image.fromarray(data.astype(np.uint8)).convert("RGBA")

    # Create a BytesIO object
    bytes_io = io.BytesIO()

    # Save the PIL image to the BytesIO object as a PNG
    image.save(bytes_io, format='PNG')

    # return the beginning of the file as a bytestream
    bytes_io.seek(0)
    return bytes_io.read()


def images_from_url_responses(response, input_shape = None):
    """Turns a list of OpenAI's URL responses into numpy images"""
    from skimage.io import imread
    from skimage import transform
    import numpy as np
    images = [imread(item.url) for item in response.data]

    if input_shape is not None:
        # make sure the output images have the same size and type as the input image
        images = [transform.resize(image, input_shape, anti_aliasing=True, preserve_range=True).astype(image.dtype) for image in images]

        if len(input_shape) == 2 and len(images[0].shape) == 3:
            # we sent a grey-scale image and got RGB images back
            images = [image[:,:,0] for image in images]

    if len(images) == 1:
        # If only one image was requested, return a single image
        return images[0]
    else:
        # Otherwise return a list of images as numpy array / image stack
        return np.asarray(images)

def extract_json(text:str):
    import re

    # Extract the JSON content using re.DOTALL to make '.' match newlines as well
    pattern = r"(?<=```json)(.*?)(?=```)"
    return re.findall(pattern, text, re.DOTALL)[0]


def prompt_kisski(prompt:str, image, model="qwen2.5-vl-72b-instruct"):
    """A prompt helper function that sends a message to the server
    and returns only the text response.
    """
    import openai
    import os
    
    message = prompt_and_image_to_message(prompt, image)
            
    # setup connection to the LLM
    client = openai.OpenAI(base_url="https://chat-ai.academiccloud.de/v1",
                           api_key=os.environ.get('KISSKI_API_KEY'))
    
    # submit prompt
    response = client.chat.completions.create(
        model=model,
        messages=message
    )
    
    # extract answer
    return response.choices[0].message.content



def prompt_scads_llm(prompt:str, image, model="Qwen/Qwen2-VL-7B-Instruct"):
    """A prompt helper function that sends a message to the server
    and returns only the text response.
    """
    import openai
    import os
    
    message = prompt_and_image_to_message(prompt, image)
    
    # setup connection to the LLM
    client = openai.OpenAI(base_url="https://llm.scads.ai/v1",
                           api_key=os.environ.get('SCADSAI_API_KEY'))
    
    # submit prompt
    response = client.chat.completions.create(
        model=model,
        messages=message
    )
    
    # extract answer
    return response.choices[0].message.content



def prompt_ollama(prompt:str, image, model="gemma3:4b"):
    """A prompt helper function that sends a message to ollama
    and returns only the text response.
    """
    import openai
    import os
    
    message = prompt_and_image_to_message(prompt, image)
        
    # setup connection to the LLM
    client = openai.OpenAI(
        base_url = "http://localhost:11434/v1"
    )
    
    # submit prompt
    response = client.chat.completions.create(
        model=model,
        messages=message
    )
    
    # extract answer
    return response.choices[0].message.content


def prompt_github_models(prompt:str, image, model="gpt-4o"):
    """A prompt helper function that sends a message to github models
    and returns only the text response.
    """
    import openai
    import os
    
    message = prompt_and_image_to_message(prompt, image)
        
    # setup connection to the LLM
    client = openai.OpenAI(
        base_url = "https://models.inference.ai.azure.com/",
        api_key = os.environ.get("GH_MODELS_API_KEY")
    )
    
    # submit prompt
    response = client.chat.completions.create(
        model=model,
        messages=message
    )
    
    # extract answer
    return response.choices[0].message.content


 


def prompt_and_image_to_message(prompt, image): 
    import base64
    from stackview._image_widget import _img_to_rgb
    if image is not None:
        rgb_image = _img_to_rgb(image)
        byte_stream = numpy_to_bytestream(rgb_image)
        base64_image = base64.b64encode(byte_stream).decode('utf-8')

        message = [{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{base64_image}"
            }
        }]}]
    else:
        message = [{"role": "user", "content": [
            {"type": "text", "text": prompt}
        ]}]
    return message
