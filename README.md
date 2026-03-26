# Smart Scraping Toolkit

![Language](https://img.shields.io/badge/Language-Python-blue)
![Type](https://img.shields.io/badge/Type-Web%20Scraping-purple)
![Focus](https://img.shields.io/badge/Focus-Automation-orange)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

Adaptive scraping toolkit for extracting structured data from static and dynamic websites.

---

## 🧾 Overview

This project provides a flexible and reusable approach to web scraping by automatically selecting the appropriate scraping strategy based on the target website.

Instead of building one-off scripts, this toolkit aims to:

- detect page type (static vs dynamic)
- select the correct scraping method
- extract structured data consistently
- output clean datasets for downstream systems

---

## 🚀 Core Capabilities

- 🌐 Static scraping (HTML parsing)
- ⚡ Dynamic scraping (JavaScript-rendered pages)
- 🔄 Strategy selection based on page behaviour
- 📊 Structured data extraction (JSON / CSV)

---

## 🔄 Planned Workflow

1. Provide a target URL  
2. Detect page type  
3. Select scraping method  
4. Extract structured content  
5. Save structured output  

---
## ▶️ How to Run

1. Install dependencies:

```bash 
pip install -r requirements.txt
playright install
```

2. Run the scraper using the CLI:

```bash 
python src/main.py --url https://example.com
```

3. Force static mode if needed:

```bash 
python src/main.py --url https://example.com --mode static
```

4. Force dynamic mode if needed:

```bash 
python src/main.py --url https://example.com --mode dynamic
```

5. Optionally specify a custom output directory:

```bash 
python src/main.py --url https://example.com --mode auto --output results
```

---
## 💻 CLI Usage

Auto detection
```bash 
python src/main.py --url https://example.com
```

Static mode
```bash 
python src/main.py --url https://example.com --mode static
```

Dynamic mode
```bash 
python src/main.py --url https://example.com --mode dynamic
```

Custom output folder
```bash 
python src/main.py --url https://example.com --mode auto --output results
```

Then commit with:

```bash 
Add Playwright dynamic scraping and mode flag
```

One important note: after installing dependencies locally, you must run:

```bash 
playwright install
```

That installs the browser binaries Playwright needs.

---

## 📂 Project Structure

```bash
smart-scraping-toolkit/
  src/
    detector.py
    static_scraper.py
    dynamic_scraper.py
    extractor.py
    main.py
  config/
    settings.json
  output/
    .gitkeep
```

## 📦 Example Output

---

```bash
{
  "url": "https://example.com",
  "scrape_mode": "static",
  "title": "Example Domain",
  "paragraphs": [
    "This domain is for use in illustrative examples in documents."
  ],
  "links": [
    {
      "text": "More information...",
      "href": "https://www.iana.org/domains/example"
    }
  ]
}
```
---

## 🛠 Tech Stack
Python
Requests
BeautifulSoup
Playwright 

---

## 📌 Status

Early-stage development.
Currently supports static scraping with CLI interface.
Dynamic scraping support is planned next.

