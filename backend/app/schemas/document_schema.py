from pydantic import BaseModel

class DocumentResponse(BaseModel):
    id:int
    document_type:str
    file_url:str

    class Config:
        from_attributes= True