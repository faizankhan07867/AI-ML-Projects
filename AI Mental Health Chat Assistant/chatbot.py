from sentiment import predict_sentiment

def get_response(message):

    sentiment = predict_sentiment(message)

    if sentiment == "positive":

        return (
            "😊 I'm glad you're feeling positive! "
            "Keep taking care of yourself and stay motivated."
        )

    return (
        "💙 I'm sorry you're going through a difficult time. "
        "Consider talking to someone you trust, taking a short walk, "
        "or practicing deep breathing. If these feelings become intense "
        "or continue for a long time, reaching out to a qualified mental "
        "health professional can really help."
    )