import gspread
from google.oauth2.service_account import Credentials
import logging
import os
import pandas as pd
from datetime import datetime
import sys


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='a'
)

logging.info("Starting the script")

try: 
    csv_fil = "produkter.csv"
    if not os.path.exists(csv_fil):
        logging.error(f"Kunne ikke finde {csv_fil}")
        print(f"Kunne ikke finde csv filen: {csv_fil}")
        sys.exit(1)
    
    logging.info(f"læser filen: {csv_fil}")
    
    df = pd.read_csv(csv_fil)
    df = df.dropna(how='all')
    df.columns = df.columns.str.strip()

    logging.info("Forbinder til google sheets")
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("tutorial-sheets-498206-a6f64265a234.json", scopes=scopes)
    client = gspread.authorize(creds)


    sheet_id = "1mY_AlBKbYB3eFdrV8SLlp_BXdxtWyjIWAIgtjSeMgyY"
    workbook = client.open_by_key(sheet_id)

    sheet = workbook.get_worksheet(0)

    logging.info("Rydder arket")
    print("Rydder arket")
    sheet.clear()

    headers = df.columns.tolist()
    rows = df.values.tolist()
    payload = [headers] + rows

    logging.info("Uploader data til Google Sheets (række 3 og ned)...")
    sheet.append_rows(payload, table_range="A3")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary_tekst = f"Last Updated: {timestamp}"
    sheet.update_acell("A1", summary_tekst)
    print("Det er blevet uploadet nu")

except Exception as e:
    logging.error(f"Der opstod en fejl: {str(e)}", exc_info=True)
    print(f"Der opstod en fejl under kørslen. Tjek 'app.log' for detaljer.")



