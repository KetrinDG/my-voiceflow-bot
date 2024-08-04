from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
from app.scraper import scrape_amazon_return_policy


class QAModel:
    def __init__(self, max_length: int = 2048) -> None:
        """
        Initializes the QAModel with a specified maximum context length.

        Args:
            max_length (int): Maximum length of the context to be considered for question answering. Defaults to 2048.

        Raises:
            ValueError: If the scraped context is empty.
        """
        self.max_length = max_length
        self.model_name = 'bert-large-uncased-whole-word-masking-finetuned-squad'
        self.context = scrape_amazon_return_policy()
        if not self.context.strip():
            raise ValueError("Scraped context is empty. Please check the scraper function.")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForQuestionAnswering.from_pretrained(self.model_name)
        self.nlp = self.create_pipeline()
        print("QAModel initialized successfully.")

    def create_pipeline(self):
        """
        Creates a Hugging Face pipeline for question answering.

        Returns:
            pipeline: A question-answering pipeline with the specified model and tokenizer.
        """
        return pipeline('question-answering', model=self.model, tokenizer=self.tokenizer)

    def get_answer(self, question: str) -> str:
        """
        Gets an answer to a given question based on the scraped context.

        Args:
            question (str): The question for which an answer is to be retrieved.

        Returns:
            str: The answer to the question or a message indicating that the question is out of scope.
        """
        try:
            context_to_use = self.context[:self.max_length]

            # Check if the question is relevant to the return policy
            if not self.is_relevant_question(question):
                return "I'm sorry, I can't help with that. Please contact customer support."

            # Get the answer from the model
            answer = self.nlp(question=question, context=context_to_use)

            cleaned_answer = answer.get('answer', '').strip()

            return cleaned_answer if cleaned_answer else "I'm sorry, I can't help with that. Please contact customer support."
        except Exception as e:
            print(f"Error: {e}")
            return "I'm sorry, I can't help with that. Please contact customer support."

    def is_relevant_question(self, question: str) -> bool:
        """
        Checks if the question is related to return policies based on keywords.

        Args:
            question (str): The question to be checked.

        Returns:
            bool: True if the question is related to return policies, False otherwise.
        """
        keywords = ["return", "refund", "exchange", "policy", "returning", "returns", "shipping", "order", "cookies"]
        return any(keyword in question.lower() for keyword in keywords)


# Create a global instance of QAModel
qa_model = QAModel()


def get_short_answer(question: str) -> str:
    """
    Retrieves a short answer to the provided question using the global QAModel instance.

    Args:
        question (str): The question for which an answer is needed.

    Returns:
        str: The answer to the question.
    """
    return qa_model.get_answer(question)
