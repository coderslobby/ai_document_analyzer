from pydantic import BaseModel

class DocumentUploadResponse(BaseModel):
    fileName : str
    message : str

class QuestionRequest(BaseModel):
    fileName: str
    question: str

class AnswerResponse(BaseModel):
    answer: str