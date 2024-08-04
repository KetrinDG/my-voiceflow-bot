import string
from app.qa_model import get_short_answer
from app.scraper import scrape_amazon_return_policy



class AmazonReturnPolicyChatbot:
    def __init__(self):
        """
        Initializes the AmazonReturnPolicyChatbot by loading the return policy text and setting predefined answers.

        Raises:
            ValueError: If the return policy text cannot be loaded.
        """
        self.return_policy_text = self.load_return_policy()
        if not self.return_policy_text:
            raise ValueError("Failed to load return policy text")

        self.predefined_answers = {
            "return an item after 30 days": "After 30 days, you may be entitled to a repair, replacement, or refund. Please contact Amazon for further assistance.",
            "pay for return shipping": "Amazon will refund the cost of sending an item back if it was sold or dispatched by Amazon. If not eligible for free return, the return cost will be deducted from your refund.",
            "return an item": "To return an item, visit the Returns Support Centre, choose the item, and follow the instructions to print a return label.",
            "items that cannot be returned": "Certain items like health protection or hygiene products, and custom products, cannot be returned unless defective.",
            "item is defective": "If a product is defective, contact Amazon within 30 days for a return. After 30 days, you may need to contact the manufacturer.",
            "return policy for international orders": "Most Amazon Global Store items can be returned within 30 days of receipt. Use the Returns Support Centre for details.",
            "process a return": "Amazon will issue a refund within 14 days of receiving your returned item.",
            "return a gift card": "Amazon.co.uk Gift Cards are non-returnable items.",
            "discounted items": "Discounted items follow the same return policy as regular items, unless otherwise specified.",
            "cancel my order": "To cancel your order, visit the Your Orders page, select the order, and click 'Cancel Items'.",
            "return policy": "Amazon's return policy allows you to return most items within 30 days of receipt. Items should be in their original condition and packaging for a full refund.",
            "purposes of cookies": "Cookies are used to understand how customers use our services, display and measure personalized ads, and generate audience insights."
        }

    def load_return_policy(self):
        """
        Loads the return policy content by scraping the Amazon return policy page.

        Returns:
            str: The scraped return policy content.
        """
        context = scrape_amazon_return_policy()
        if not context.strip():
            print("Warning: The scraped policy content is empty.")
        return context

    def greet(self):
        """
        Returns a greeting message from the chatbot.

        Returns:
            str: A greeting message.
        """
        return "Hello! How can I help you with Amazon return policies?"

    def answer_query(self, question):
        """
        Provides an answer to a given question using predefined answers or the QA model.

        Args:
            question (str): The question to be answered.

        Returns:
            str: The answer to the question or a message directing to customer support.
        """
        try:
            # Check for a predefined answer
            predefined_answer = self.generate_predefined_answer(question)
            if predefined_answer:
                return predefined_answer

            # If no predefined answer is found, use the model to find an answer
            model_answer = self.generate_answer_with_model(question)
            if model_answer:
                return model_answer

            # If no answer is found, direct to customer support
            return "I'm sorry, I can't help with that. Please contact customer support."
        except Exception as e:
            return f"Error: {str(e)}"

    def generate_predefined_answer(self, question):
        """
        Generates an answer from the predefined answers based on the question.

        Args:
            question (str): The question to get an answer for.

        Returns:
            str: The predefined answer if available, otherwise None.
        """
        question_cleaned = question.lower().translate(str.maketrans('', '', string.punctuation)).strip()

        # Поиск подходящего ответа по ключевым словам
        for key in self.predefined_answers:
            if key in question_cleaned:
                answer = self.predefined_answers.get(key)
                print(f"Predefined answer for '{question_cleaned}': {answer}")
                return answer

        return None

    def generate_answer_with_model(self, question):
        """
        Generates an answer using the QA model.

        Args:
            question (str): The question to get an answer for.

        Returns:
            str: The answer generated by the model, or a message indicating no answer found.
        """
        answer = get_short_answer(question)
        print(f"Model answer for '{question}': {answer}")

        if not answer.strip():
            return "I'm sorry, I can't help with that. Please contact customer support."

        # Format the answer with a capital letter
        return answer[0].upper() + answer[1:]

    def is_relevant(self, answer):
        """
        Checks if the answer is relevant based on certain keywords.

        Args:
            answer (str): The answer to be checked.

        Returns:
            bool: True if the answer is relevant, False otherwise.
        """
        # Basic relevance check
        if 'first-party' in answer.lower() or 'third-party' in answer.lower():
            return False

        relevant_keywords = ["return", "policy", "refund", "shipping", "order", "cookies"]
        return any(keyword in answer.lower() for keyword in relevant_keywords)
