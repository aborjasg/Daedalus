from django.http import JsonResponse

class ActionResponse:
    def __init__(self, service:str, endpoint:str, input:str, output:str, status=200):
        self.service = service
        self.endpoint = endpoint
        self.input = input
        self.output = output
        self.status = status        

    def to_json(self):
        return JsonResponse({"service": self.service, "endpoint": self.endpoint, "input": self.input, "output": self.output, "status": self.status})