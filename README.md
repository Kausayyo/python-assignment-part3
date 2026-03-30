# Assignment Part 3 — File I/O, APIs & Exception Handling

## Overview

This project demonstrates a complete Python workflow combining file handling, API integration, exception handling, and logging.

The goal was to build a **product explorer system** that interacts with a public API, processes data, handles failures gracefully, and logs errors like a real-world application.

API used: https://dummyjson.com 

---

## Features Implemented

### 1. File Handling (python_notes.txt)

* Created a file using write mode
* Appended additional content using append mode
* Read and displayed content with line numbering
* Counted total lines
* Implemented keyword-based search (case-insensitive)

---

### 2. API Integration

#### Fetch Products

* Retrieved 20 products from API
* Displayed in structured table format (ID, Title, Category, Price, Rating)

#### Filter & Sort

* Filtered products with rating ≥ 4.5
* Sorted results by price (descending)

#### Category Search

* Fetched all products under **laptops category**
* Displayed product name and price

#### POST Request (Simulated)

* Sent product data to API
* Printed server response

---

### 3. Exception Handling

#### Safe Division Function

* Handles:

  * Division by zero
  * Invalid input types

#### Safe File Reader

* Reads file safely
* Handles missing file errors
* Always executes cleanup using `finally`

#### API Error Handling

* Handled:

  * ConnectionError
  * Timeout
  * Generic exceptions

#### Input Validation Loop

* Accepts only valid product IDs (1–100)
* Prevents invalid API calls
* Gracefully handles 404 responses

---

### 4. Error Logging (error_log.txt)

* Built a custom logging function
* Logs include:

  * Timestamp
  * Error source
  * Error type
  * Message

Example log entry:

```
[2025-01-15 14:33:10] ERROR in lookup_product: HTTPError — 404 Not Found for product ID 999
```

#### Intentional Error Triggers

* Connection error using invalid URL
* HTTP 404 using non-existent product ID

Logs are appended and persist across runs.

---

## Project Structure

```
.
├── part3_api_files.py
├── python_notes.txt
├── error_log.txt
├── README.md
```

---

## How to Run

### 1. Install dependencies

```
pip install requests
```

### 2. Run the script

```
python part3_api_files.py
```

### 3. Provide input when prompted

Example:

```
Enter a keyword to search: python
```

---

## Key Learnings

* File handling with write, append, and read modes
* Real-world API interaction using `requests`
* Difference between HTTP errors and Python exceptions
* Writing resilient programs with proper error handling
* Building a basic logging system

---

## Notes

* `python_notes.txt` and `error_log.txt` are generated automatically by the script
* DummyJSON API is a mock API — POST requests do not persist data
* Logging is intentionally triggered to demonstrate functionality

---

## Status

All tasks completed as per assignment requirements:

* File operations
* API integration
* Exception handling
* Logging system

---

## Author

Kauseyo Basak
