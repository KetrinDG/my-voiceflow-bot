from pydantic import BaseModel

class Query(BaseModel):
    """
    Model for representing a query with a single question.

    Attributes:
        question (str): The question to be asked.
    """
    question: str
