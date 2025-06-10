from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from src.db import database, models

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", summary="Get all events")
def get_events(db: Session = Depends(get_db)):
    events = db.query(models.Event).all()
    return events

@router.post("/", summary="Create a new event")
def create_event(name: str, location: str, date_: date, db: Session = Depends(get_db)):
    event = models.Event(name=name, location=location, date=date_)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

@router.get("/{event_id}", summary="Get event by ID")
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.delete("/{event_id}", summary="Delete event by ID")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(event)
    db.commit()
    return {"message": "Event deleted successfully"}
