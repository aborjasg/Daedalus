
class ErrorResponse:
    def __init__(self, code:str, message:str, details:str):
        self.code = code
        self.message = message
        self.details = details