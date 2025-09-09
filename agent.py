import ollama
import json

customer_complaint = """
Subject: Issue with my recent order, ORD1002

Dear Customer Support Team,

I am writing to report an issue with a recent purchase. My order, ID number ORD1002, which was delivered on June 20th, arrived with a damaged product. The smartwatch I ordered has a large crack in the screen and is not functioning.

I have attached photos showing the damage. My email is john.smith@example.com.

Could you please help me with a replacement or a refund?

Thank you,
John Smith
"""

# Define the system prompt to instruct the LLM
system_prompt = """
You are an expert email parsing agent. Your task is to extract the following
entities from the user's email: customer_name, customer_email, order_id,
and the core issue.

Respond with a valid JSON object containing these fields.
"""

# Call the chat method with a list of messages
try:
    response = ollama.chat(
        model='llama3:8b-instruct-q4_0',
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': customer_complaint},
        ],
        format='json'  # Optional: tell the model to respond in JSON format
    )

    # Parse the JSON response
    parsed_data = json.loads(response['message']['content'])
    
    # Print the extracted data
    print("Parsed Data:", parsed_data)

except Exception as e:
    print(f"An error occurred: {e}")