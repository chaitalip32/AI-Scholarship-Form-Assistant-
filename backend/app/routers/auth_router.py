from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.user import User
from app.schemas.auth_schema import UserSignup
from app.core.security import hash_password
from fastapi.security import OAuth2PasswordBearer
from fastapi import Security

from app.schemas.auth_schema import UserLogin
from app.core.security import(
    verify_password,
    create_access_token
)
router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(user:UserSignup, db: Session=Depends(get_db)):

    existing_user=db.query(User).filter(
        User.email==user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    hashed_pw=hash_password(user.password)

    new_user=User(
        name=user.name,
        email=user.email,
        password=hashed_pw,
        role='student'
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return{
        "message":"User created successfully"
    }

@router.post("/login")
def login(user: UserLogin, db: Session=Depends(get_db)):
    db_user=db.query(User).filter(
        User.email==user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    
    valid_password=verify_password(
        user.password,
        db_user.password
    )

    if not valid_password:
        raise HTTPException(
            status_code=401,
            detail="Invalid credential"
        )
    
    token=create_access_token(
        data={
            "sub":db_user.email
        }
    )

    return{
        "access_token": token,
        "token_type": "bearer"
    }

oauth2_scheme=OAuth2PasswordBearer(
    tokenUrl="login"
)

@router.get("/profile")
def profile(
    token:str=Security(oauth2_scheme)
):
    email=verify_token(token)

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    return{
        "email":email
    }