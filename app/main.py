from fastapi import UploadFile, FastAPI
from fastapi.exceptions import HTTPException
from app.services.read_doc import validate_filetypes
from app.services.chunker import chunkDocument
from app.services.llmcall import user_answer
from app.models import DocumentUploadResponse, AnswerResponse, QuestionRequest
from typing import List, Dict
app = FastAPI()

document_store: Dict[str, List[str]] = {}
@app.post('/file/upload')
async def fileUpload(file: UploadFile) -> DocumentUploadResponse:
        file_path = f'uploads/{file.filename}'
        content = await file.read()
        with open(file_path, 'wb') as f:
            f.write(content)
        extracted_text = validate_filetypes(file_path=file_path)
        chunks = chunkDocument(extracted_text)

        document_store[f'{file.filename}'] = chunks

        return DocumentUploadResponse(
              fileName=f'{file.filename}',
              message="file has been uploaded"
        )

@app.post('/chat/')
def chat(request: QuestionRequest) -> AnswerResponse :
        chunks = document_store.get(request.fileName)
        if not chunks:
            raise HTTPException(
                  status_code=404,
                  detail='Document not found, please upload the document first!')
        answer = user_answer(
                question=request.question,
                chunkList=chunks
        )
        return AnswerResponse(answer=answer)