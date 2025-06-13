# 🎓 ElectraSyn Literature Mining Automation from Google Scholar

## 🌁 Overview

ElectraSyn, the product I manage at IKA, is a synthetic electrochemical platform that enables scientists to carry out chemical reactions. In academic research, it is standard practice to document experimental procedures in detail—including the brand and model of key instruments and their operating parameters. As a result, hundreds of published papers mention the use of ElectraSyn.

As a product manager, reviewing and analyzing these publications is essential to understand how ElectraSyn is applied in real-world research. However, filtering relevant information from the internet and managing a large volume of literature manually is time-consuming and inefficient.

To address this, I developed a Python script that automates the repetitive task of searching and retrieving relevant publications from Google Scholar. The script uses APIs such as SerpApi and Lens to collect enriched metadata, including author names, institutional affiliations, countries, and research fields. The data is organized into a pandas DataFrame and exported as an Excel file for further analysis.

This project serves as a valuable foundation for future automation of literature mining processes. It also provided me with hands-on experience in acquiring and managing API licenses, as well as a deeper understanding of how to work with scholarly data programmatically.

## ⚙️ Technologies Used

| Category              | Technology / Library                             | Description                                                                 |
|-----------------------|--------------------------------------------------|-----------------------------------------------------------------------------|
| Programming Language  | **Python 3.11**                                     | Core language used for scripting and automation                            |
| API - Data Retrieval  | [SerpApi](https://serpapi.com)                   | Retrieves scholarly data from Google Scholar via keyword + date filtering  |
| API - Metadata Enrich | [Lens.org Scholarly API](https://www.lens.org)  | Adds metadata: abstract, affiliations, fields of study, etc.               |
| Data Processing       | [pandas](https://pandas.pydata.org/)            | Structures and processes data; converts to DataFrame                       |
| Excel Export          | [XlsxWriter](https://xlsxwriter.readthedocs.io/) | Exports search results to `.xlsx` files via pandas                         |
| HTTP Requests         | [requests](https://requests.readthedocs.io/)    | Communicates with APIs via GET and POST requests                           |
| Date Handling         | [datetime](https://docs.python.org/3/library/datetime.html) | Formats timestamps and parses dates from metadata                |
| File I/O              | Built-in Python                                  | Saves memo files summarizing search coverage                               |
