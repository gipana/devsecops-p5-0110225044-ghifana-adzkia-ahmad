def format_response(message, status_code):
    return {
        "status": status_code,
        "message": message,
        "success": status_code == 200
    }

def validate_input(text):
    if not isinstance(text, str):
        return False
    return len(text.strip()) > 0
