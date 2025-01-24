import re
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter, RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    documents = PyPDFLoader(q1_pdf).load()
    text_splitter = CharacterTextSplitter(chunk_overlap=0)
    page_chunks = text_splitter.split_documents(documents)
    return page_chunks[-1]

def hw02_2(q2_pdf):
    documents = PyPDFLoader(q2_pdf).load()
    text_splitter = RecursiveCharacterTextSplitter(
            chunk_overlap=0,
            chunk_size=50,
            separators=[
                r"第\s+[一二三四五六七八九十]+\s+章",
                r"第\s+[\d-]+\s+條"
            ],
            is_separator_regex=True
    )
    combined_text = "\n".join([doc.page_content for doc in documents])
    chunks = text_splitter.split_text(combined_text)
    return len(chunks)

# hw02_1(q1_pdf)
# hw02_2(q2_pdf)