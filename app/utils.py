import openai
import requests
from bs4 import BeautifulSoup


def get_openai_response(prompt: str, api_key: str) -> str:
    """
    Gets a response from OpenAI API based on the given prompt.

    Args:
        prompt (str): The prompt to be sent to the OpenAI API.
        api_key (str): The API key for authentication with OpenAI.

    Returns:
        str: The response text from OpenAI API.

    Raises:
        Exception: If there is an error during the request to OpenAI API.
    """
    openai.api_key = api_key
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error during OpenAI API request: {e}")
        return None


def scrape_amazon_return_policy(url: str) -> str:
    """
    Scrapes the Amazon return policy text from the specified URL.

    Args:
        url (str): The URL of the Amazon page to scrape.

    Returns:
        str: The extracted text from the Amazon return policy page.

    Raises:
        Exception: If there is an error during the HTTP request or parsing of the page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        policy_text = soup.get_text(separator="\n")
        return policy_text
    except Exception as e:
        print(f"Error during Amazon page parsing: {e}")
        return None


def generate_prompt(user_query: str, return_policy_text: str) -> str:
    """
    Creates a prompt for OpenAI using the return policy text and the user's query.

    Args:
        user_query (str): The user's question.
        return_policy_text (str): The return policy text to be used in the prompt.

    Returns:
        str: The generated prompt for OpenAI.
    """
    prompt = f"Here is Amazon's return policy:\n\n{return_policy_text}\n\nUser's question: {user_query}\n\nAnswer the question using the information from the return policy:"
    return prompt
