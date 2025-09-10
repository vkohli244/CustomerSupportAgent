import ollama
import json

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from langchain_core.tools import Tool
from tools import get_order_details, get_shipping_status


getOrderDetails: Tool = Tool(
                            name="getOrderDetails", 
                            func=get_order_details,
                            description="Use this tool to get the details of an order, the input must be the order number")

getShippingStatus: Tool = Tool(
                            name="getShippingStatus", 
                            func=get_shipping_status,
                            description="Use this tool to get the shipping status of an order, the input must be a tracking number")

toolbox:list[Tool] = [getOrderDetails,getShippingStatus]

system_message = (
    "You are an expert customer support agent. You have access to tools to help "
    "customers with their orders. Your goal is to be helpful and provide "
    "accurate information. Use your tools to look up order details and "
    "shipping status to solve the customer's issue."
)

# Create the ChatPromptTemplate object
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_message),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

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


