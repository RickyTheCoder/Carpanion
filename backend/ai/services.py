import base64
import io
from langchain import ChatCompletion, OpenAI

def data_uri_to_blob(data_uri):
    # Split the data URI into parts
    header, data = data_uri.split(',')

    # Get the MIME type
    mime_type = header.split(';')[0].split(':')[1]

    # Decode the base64 data
    byte_string = base64.b64decode(data)

    # Create a BytesIO object and return it
    return io.BytesIO(byte_string), mime_type

def process_image(image_path):
    # Read the image file and encode it as base64
    with open(image_path, 'rb') as f:
        image_data = f.read()
    base64_image = base64.b64encode(image_data).decode('utf-8')

    # Create an OpenAI client
    openai = OpenAI(api_key="your-api-key")

    # Create a chat model
    chat_model = ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please list all items bought in the attached image of the receipt. Then, for each item, provide the usual expiration days. Also, try to make a give the full name of the item, like Good&Gather Hummus instead of GG Hummus. Lastly, please give the number of days each item could expire in, prefixed with [Least number of days] a positive number. Here are the examples of the output:\n"
                    + "1. Good&Gather Yogurt: Usually Expire in 2-3 weeks; [Least number of days] 14\n"
                    + "2. Lettuce: Usually Expire in 7-10 days; [Least number of days] 7\n"
                    + "3. Canned beans: This is a type of food that can be stored as long as 1-2 years. However, it is still suggested to have it ASAP. [Least number of days] 365\n"
                    + "Ambiguous Items: GOOD&GATHER, Smartly\n"
                    + "Not food: Blogilates, Basketball, T-shirt\n"
            },
            {
                "role": "assistant",
                "content": {
                    "type": "image",
                    "data": base64_image
                }
            }
        ]
    )

    # Parse the response
    # ...

    return result