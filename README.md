OLX Car Cover Scraper
This project is a simple Python-based web scraper that fetches car cover listings from OLX India. It extracts key details like title, price, and location of each listing and saves them in a text file.

📌 Features
Scrapes real-time search results for "Car Cover" on OLX.

Extracts:

Title of the listing

Price (if available)

Location

Saves results in a clean and readable format to car_covers.txt.

🛠️ Tech Stack
Python 3

Requests

BeautifulSoup4 (bs4)

🚀 How to Run
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/olx-scraper.git
cd olx-scraper
Install dependencies

bash
Copy
Edit
pip install requests beautifulsoup4
Run the script

bash
Copy
Edit
python olx_scraper.py
View results

Open car_covers.txt to see the list of car covers from OLX.

📂 Output Example
yaml
Copy
Edit
Title: Car Cover for SUV
Price: ₹499
Location: Hyderabad

---
Title: Waterproof Car Body Cover
Price: ₹799
Location: Delhi
📎 Notes
This scraper uses static HTML parsing. If OLX changes their structure, selectors may need updates.

Make sure your network allows access to OLX.
