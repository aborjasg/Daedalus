import uuid

from django.http import JsonResponse

class ActionResponse:
    def __init__(self, service:str, success:bool, data:dict, errors:list, status:int):
        self.service = service
        self.success = success
        self.data = data
        self.errors = errors
        self.status = status        
        self.correlationId = uuid.uuid4()

    def to_json(self):
        return JsonResponse({"service": self.service, "success": self.success, "data": self.data, "errors": self.errors, "status": self.status, "correlationId": self.correlationId})