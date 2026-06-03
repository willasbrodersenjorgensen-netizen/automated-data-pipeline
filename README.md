# automated-data-pipeline


This repository includes an Excel to Google Sheets data pipeline.
Building this project learned me to apply the modules Pandas, OS, Logging, and Gspread to build a clean automation tool. I've used a local CSV file to test the script before uploading it to the Google Sheets API.

With Pandas i have learned to read CSV files, clean data by dropping empty rows with `dropna`, and strip hidden spaces from column headers.
With OS i have learned to check if the file actually exists before running the script so the program doesn't crash.
With Logging i have learned to build a professional "app.log" file to track what the script is doing and capture errors if something goes wrong.
With Gspread i have learned to connect with Google Cloud Platform, authorize with a JSON key, clear a worksheet, and upload rows to a specific range.

I have also created a `creds.json.example` file to document how the Google credentials file should look, without revealing my real private keys.

Over all ive spent a week learning the exact modules and finaly build a solid data sync tool.

What Could be added?
Automate the script using Windows Task Scheduler or GitHub Actions so it runs every night without me pushing play.
Learning SQL to fetch data directly from a real database instead of a local CSV file.
Connect to a real web API (like Shopify or Stripe) to sync live sales data directly to Google Sheets.
