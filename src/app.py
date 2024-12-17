"""A library who """
# %%
import yfinance as yf
import json
import pandas as pd



def get_ticket_info(tickets: list[str]) -> None:
    for ticket in tickets:
        dat = yf.Ticker(ticker=ticket)
        save_ticket_info(ticket_name=ticket,dat=dat)
        save_ticket_history(ticket_name=ticket, dat=dat)
    return None

def save_ticket_history(ticket_name: str, dat: yf.ticker.Ticker):
    history = dat.history(period='1mo')
    history.to_csv(f"dados/history/{ticket_name}.csv", index=False)

def save_ticket_info(ticket_name: str, dat: yf.ticker.Ticker) -> None:
    """Save the ticket information in another folder"""
    with open(f"dados/info/{ticket_name}.json", 'w', encoding="UTF-8") as file:
        json.dump(dat.info,file,ensure_ascii=False, indent=4)
    print("Data saved as success")
    return None

if __name__ == "__main__":
    tickets = ["MSFT","GOGL","NVDA"]
    get_ticket_info(tickets=tickets)
    exit(0)