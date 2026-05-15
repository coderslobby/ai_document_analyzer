import pymupdf
from typing import List
from spire.doc import *  # type:ignore
import mimetypes
from fastapi.exceptions import HTTPException
from typing import Dict, Callable

# Reading Pdf files
def read_Pdf(file_path: str) -> str:
    with pymupdf.open(filename=file_path) as doc:
        fullTextDoc: List[str] = []
        for page in doc:
            fullTextDoc.append(str(page.get_text())) # type: ignore 
        return ''.join(fullTextDoc)

# reading docx files
def read_doc(file_path: str) -> str:
    my_doc = Document() # type:ignore
    my_doc.LoadFromFile(file_path) # type:ignore
    fullTextDoc = my_doc.GetText()
    print(fullTextDoc)
    return str(fullTextDoc)

FILE_HANDLERS: Dict[str, Callable[[str], str]] = {
    'application/pdf': read_Pdf,
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': read_doc
}
#validating the file types
def validate_filetypes(file_path: str):    
    mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type not in FILE_HANDLERS:
        raise HTTPException(400,'Invalid File Type')
    
    handler = FILE_HANDLERS.get(mime_type)
    if handler:
        return handler(file_path)
    else:
        raise HTTPException(400,'Invalid File Type')