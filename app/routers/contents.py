from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import parse_obj_as
from typing import List
from uuid import UUID

from ..schemas.contents import Content
from ..repositories.contents import ContentsRepository

router = APIRouter(prefix="/contents", tags=["contents"])


@router.get("/", response_model=List[Content])
def list_contents(skip: int = 0, max: int = 10, contents: ContentsRepository = Depends()):
    db_speedsters = contents.all(skip=skip, max=max)
    return parse_obj_as(List[Content], db_speedsters)


@router.post("/", response_model=Content, status_code=status.HTTP_201_CREATED)
def store_contents(content: Content, contents: ContentsRepository = Depends()):

    db_content = contents.create(content)
    return Content.from_orm(db_content)
