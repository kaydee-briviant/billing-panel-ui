from database import get_sessions
from model import Account
 
 
def main():
    session = get_sessions()
    try:
        accounts = [
            Account(plan_type="payg", credits=10),
            Account(plan_type="managed", credits=2),
            Account(plan_type="dedicated", credits=5),
            Account(plan_type="payg", credits=12)
        ]
        session.add_all(accounts)
        session.commit()

        print(f"Inserted {len(accounts)} account(s).")
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
 
 
if __name__ == "__main__":
    main()