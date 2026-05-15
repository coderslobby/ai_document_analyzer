from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import config_setting
from typing import List

def chunkDocument(doc_text: str) -> List[str]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=config_setting.chunk_size, chunk_overlap=config_setting.chunk_overlap)
    texts = text_splitter.split_text(doc_text)
    return texts