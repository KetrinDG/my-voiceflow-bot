# Amazon Return Policy Chatbot

## Overview

The **Amazon Return Policy Chatbot** is a FastAPI application designed to interact with users and provide information about Amazon's return policies. It combines predefined answers with a question-answering (QA) model to address user queries.

## Project Structure

```
my-voiceflow-bot/
│
├── app/
│   ├── __init__.py          # Initialization file for the app directory.
│   ├── main.py              # The entry point for the FastAPI application.
│   ├── chatbot.py           # Contains the AmazonReturnPolicyChatbot class for handling queries.
│   ├── models.py            # Defines data models, including the Query model.
│   ├── qa-models.p          # Contains the pre-trained QA models for answering queries.
│   ├── scraper.py           # Functions for scraping Amazon's return policy.
│   └── utils.py             # Utility functions for interacting with the OpenAI API and processing text.
│
├── requirements.txt         # List of project dependencies.
├── .dockerignore            # Docker ignore file to exclude files from the Docker context.
├── Dockerfile               # Docker configuration file for containerizing the application.
└── README.md                # Project documentation file.
```

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/KetrinDG/my-voiceflow-bot.git
    cd my-voiceflow-bot
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Ensure you have your OpenAI API key and other necessary configurations in your environment. Set `OPENAI_API_KEY` in your environment variables.

## Docker Setup

The project includes Docker configuration files to containerize the application. Follow these steps to run the application using Docker:

1. **Build the Docker image:**

    ```sh
    docker build -t amazon-return-policy-chatbot -f Dockerfile .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -p 8000:8000 --env-file .env amazon-return-policy-chatbot
    ```

    Ensure to create a `.env` file with necessary environment variables like `OPENAI_API_KEY`.

## Usage

### Running the Application

To start the FastAPI application without Docker, run:

```sh
uvicorn app.main:app --reload
```

The application will be accessible at [http://localhost:8000](http://localhost:8000).

### Endpoints

- **Root Endpoint (GET /)**

    Returns a greeting message from the chatbot.

    **Response:**

    ```json
    {
      "message": "Hello! How can I help you with Amazon return policies?"
    }
    ```

- **Query Endpoint (POST /query/)**

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
- Using the QA model to generate answers for less common queries.

### `utils.py`

Contains utility functions for:

- Fetching responses from the OpenAI API.
- Scraping Amazon's return policy text from their website.

### `scraper.py`

Provides functionality for:

- Scraping the return policy from Amazon's website.
- Saving the scraped policy text to a file.

## Contributing

Feel free to open issues or submit pull requests for improvements. Please follow the project's coding standards and guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **FastAPI**: For building the high-performance web framework.
- **OpenAI**: For providing the API used in the chatbot.
- **Hugging Face Transformers**: For the QA model.
- **BeautifulSoup**: For scraping Amazon's return policy.

