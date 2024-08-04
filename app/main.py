import sys
import os
from fastapi import FastAPI, HTTPException

# Add the directory containing the chatbot module to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chatbot import AmazonReturnPolicyChatbot
from models import Query

app = FastAPI()
chatbot = AmazonReturnPolicyChatbot()


@app.get("/")
def read_root():
    """
    Root endpoint that returns a greeting message from the chatbot.

    Returns:
        dict: A dictionary with a greeting message from the chatbot.
    """
    return {"message": chatbot.greet()}


@app.post("/query/")
def query_bot(query: Query):
    """
    Endpoint to submit a query to the chatbot and get a response.

    Args:
        query (Query): The query object containing the question.

    Returns:
        dict: A dictionary with the chatbot's answer to the question.

    Raises:
        HTTPException: If an error occurs while processing the query.
    """
    try:
        answer = chatbot.answer_query(query.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application using uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
