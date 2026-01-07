from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from typing import Optional, List
from models import UserCreate, UserResponse
from database_models import User
from database import Base, engine, get_db

app = FastAPI(title="Integration with SQL - CRUD Operations")

Base.metadata.create_all(engine)

# Endpoints
# GETS
@app.get("/")
def root():
    return {"message": "Welcome to my First FASTAPI x SQLAlchemy DB Connection"}

# Get user by id
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Get all users
@app.get("/users/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


# POSTS
# Create User (POST)
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=404, detail="User already exists")
    
    # Create new user
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# PUTS
# Update User (PUT)
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update user
    db_user.name = user.name
    db_user.email = user.email
    db_user.role = user.role
    db.commit()
    db.refresh(db_user)
    return db_user


# DELETES
# Delete User (Delete)
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}