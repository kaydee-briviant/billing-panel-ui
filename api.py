from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db
from model import Account

app = FastAPI()


@app.get("/accounts")
def get_accounts(db: Session = Depends(get_db)):
    accounts = db.query(Account).all()
    return [
        {"id": a.id, "plan_type": a.plan_type, "credits": a.credits}
        for a in accounts
    ]


@app.post("/accounts")
def create_account(account: dict, db: Session = Depends(get_db)):
    new_account = Account(plan_type=account["plan_type"], credits=account.get("credits"))
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return {"id": new_account.id, "plan_type": new_account.plan_type, "credits": new_account.credits}
