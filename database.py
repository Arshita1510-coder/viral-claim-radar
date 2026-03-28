history = []

def save_claim(claim, result): 

    history.append({
        "claim": claim,
        "result": result["result"],
        "confidence": result["confidence"]
    })


def get_history():
    return history