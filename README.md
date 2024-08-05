# Amazon Return Policy Chatbot

## Overview

The Amazon Return Policy Chatbot is a FastAPI application designed to interact with users and provide information about Amazon's return policies. It uses a combination of predefined answers and a question-answering model to respond to user queries.

## Project Structure

- `app/`
  - `__init__.py`: Initialization file for the app directory.
  - `main.py`: The entry point for the FastAPI application.
  - `chatbot.py`: Contains the `AmazonReturnPolicyChatbot` class responsible for handling user queries and providing answers.
  - `models.py`: Defines the data models used in the application, including the `Query` model for user input.
  - `scraper.py`: Contains functions for scraping Amazon's return policy from their website.
  - `utils.py`: Utility functions for interacting with the OpenAI API and processing return policy text.

- `requirements.txt`: List of dependencies required for the project.
- `README.md`: Project documentation file.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/KetrinDG/my-voiceflow-bot.git
   cd amazon_return_chatbot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables for API keys and other configurations. For OpenAI API, ensure you have your API key set up in your environment.

## Usage

### Running the Application

To start the FastAPI application, run:
```bash
uvicorn app.main:app --reload
```

The application will be accessible at `http://localhost:8000`.

### Endpoints

- **Root Endpoint (`GET /`)**

  Returns a greeting message from the chatbot.

  **Response:**
  ```json
  {
    "message": "Hello! How can I help you with Amazon return policies?"
  }
  ```

- **Query Endpoint (`POST /query/`)**

  Submit a query to the chatbot and receive a response.

  **Request Body:**
  ```json
  {
    "question": "How can I return an item?"
  }
  ```

  **Response:**
  ```json
  {
    "answer": "To return an item, visit the Returns Support Centre, choose the item, and follow the instructions to print a return label."
  }
  ```

## Functionality

### `chatbot.py`

The `AmazonReturnPolicyChatbot` class is responsible for:

- Loading the return policy text from Amazon's website.
- Providing predefined answers for common queries.
- Using a QA model to generate answers for less common queries.

### `utils.py`

Contains utility functions for:

- Fetching responses from the OpenAI API.
- Scraping Amazon's return policy text from their website.

### `scraper.py`

Provides functionality for scraping the return policy from Amazon's website and saving it to a file.

## Contributing

Feel free to open issues or submit pull requests for improvements. Please follow the project's coding standards and guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI](https://openai.com/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
```
