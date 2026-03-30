# ============================================================
# Part 3: File I/O, APIs & Exception Handling
# ============================================================

import requests
from datetime import datetime

# ============================================================
# Task 4 Helper — Error Logger (defined early, used throughout)
# ============================================================

def log_error(source, error_type, message):
    """Writes a timestamped error entry to error_log.txt."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] ERROR in {source}: {error_type} — {message}\n"
    with open("error_log.txt", "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"  [Logged] {entry.strip()}")


# ============================================================
# Task 1 — File Read & Write Basics (6 marks)
# ============================================================

# --- Part A: Write 5 lines using write mode ---

notes = [
    "Topic 1: Variables store data. Python is dynamically typed.\n",
    "Topic 2: Lists are ordered and mutable.\n",
    "Topic 3: Dictionaries store key-value pairs.\n",
    "Topic 4: Loops automate repetitive tasks.\n",
    "Topic 5: Exception handling prevents crashes.\n",
]

with open("python_notes.txt", "w", encoding="utf-8") as f:
    f.writelines(notes)

print("File written successfully.")

# Append 2 more lines using append mode
extra = [
    "Topic 6: Functions help organise and reuse code.\n",
    "Topic 7: Modules allow importing external functionality.\n",
]

with open("python_notes.txt", "a", encoding="utf-8") as f:
    f.writelines(extra)

print("Lines appended.")

# --- Part B: Read back, number each line ---

with open("python_notes.txt", "r", encoding="utf-8") as f:
    all_lines = f.readlines()

print("\nFile contents:")
for i, line in enumerate(all_lines, start=1):
    print(f"{i}. {line.rstrip()}")  # rstrip removes trailing \n

print(f"\nTotal number of lines: {len(all_lines)}")

# Keyword search (case-insensitive)
keyword = input("\nEnter a keyword to search: ").strip()
matches = [line.rstrip() for line in all_lines if keyword.lower() in line.lower()]

if matches:
    print(f"\nLines containing '{keyword}':")
    for match in matches:
        print(f"  {match}")
else:
    print(f"No lines found containing '{keyword}'.")


# ============================================================
# Task 2 — API Integration (8 marks)
# ============================================================

BASE_URL = "https://dummyjson.com/products"
products = []  # store fetched products for use in Step 2

# --- Step 1: Fetch and display 20 products ---

print("\n========== Fetching 20 Products ==========")

try:
    response = requests.get(f"{BASE_URL}?limit=20", timeout=5)
    products = response.json()["products"]

    # Print formatted table header
    print(f"{'ID':<4} | {'Title':<30} | {'Category':<14} | {'Price':<9} | Rating")
    print("-" * 70)

    for p in products:
        print(f"{p['id']:<4} | {p['title']:<30} | {p['category']:<14} | ${p['price']:<8} | {p['rating']}")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
    log_error("fetch_products", "ConnectionError", "Failed to connect to dummyjson.com")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
    log_error("fetch_products", "Timeout", "Request to dummyjson.com timed out")
except Exception as e:
    print(f"Unexpected error: {e}")
    log_error("fetch_products", "Exception", str(e))

# --- Step 2: Filter rating >= 4.5, sort by price descending ---

print("\n========== Products with Rating ≥ 4.5 (Sorted by Price ↓) ==========")

try:
    # Filter products with rating >= 4.5
    high_rated = []
    for p in products:
        if p["rating"] >= 4.5:
            high_rated.append(p)

    # Bubble sort by price descending
    for i in range(len(high_rated)):
        for j in range(i + 1, len(high_rated)):
            if high_rated[j]["price"] > high_rated[i]["price"]:
                high_rated[i], high_rated[j] = high_rated[j], high_rated[i]

    print(f"{'ID':<4} | {'Title':<30} | {'Price':<9} | Rating")
    print("-" * 55)
    for p in high_rated:
        print(f"{p['id']:<4} | {p['title']:<30} | ${p['price']:<8} | {p['rating']}")

except Exception as e:
    print(f"Error during filtering/sorting: {e}")

# --- Step 3: Fetch laptops category ---

print("\n========== Laptops Category ==========")

try:
    response = requests.get(f"{BASE_URL}/category/laptops", timeout=5)
    laptops = response.json()["products"]

    for laptop in laptops:
        print(f"  {laptop['title']:<35} ${laptop['price']}")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
    log_error("fetch_laptops", "ConnectionError", "Failed to fetch laptops category")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
    log_error("fetch_laptops", "Timeout", "Laptops category request timed out")
except Exception as e:
    print(f"Unexpected error: {e}")
    log_error("fetch_laptops", "Exception", str(e))

# --- Step 4: POST request — simulated product creation ---

print("\n========== POST: Add Custom Product ==========")

new_product = {
    "title":       "My Custom Product",
    "price":       999,
    "category":    "electronics",
    "description": "A product I created via API"
}

try:
    response = requests.post(f"{BASE_URL}/add", json=new_product, timeout=5)
    print("Server response:")
    print(response.json())

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
    log_error("post_product", "ConnectionError", "Failed to POST new product")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
    log_error("post_product", "Timeout", "POST request timed out")
except Exception as e:
    print(f"Unexpected error: {e}")
    log_error("post_product", "Exception", str(e))


# ============================================================
# Task 3 — Exception Handling (7 marks)
# ============================================================

# --- Part A: Guarded Calculator ---

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print("\n========== Safe Divide Tests ==========")
print(safe_divide(10, 2))       # normal: 5.0
print(safe_divide(10, 0))       # ZeroDivisionError
print(safe_divide("ten", 2))    # TypeError

# --- Part B: Guarded File Reader ---

def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        # Always runs whether file was found or not
        print("File operation attempt complete.")

print("\n========== Safe File Reader Tests ==========")

print("\nReading python_notes.txt:")
content = read_file_safe("python_notes.txt")
if content:
    print(content)

print("\nReading ghost_file.txt:")
read_file_safe("ghost_file.txt")

# --- Part C: Robust API Calls ---
# Every requests call above already has full try-except.
# Demonstrating once more explicitly here:

print("\n========== Robust API Call Demo ==========")

try:
    response = requests.get(f"{BASE_URL}/1", timeout=5)
    if response.status_code == 200:
        p = response.json()
        print(f"Product: {p['title']} — ${p['price']}")
    else:
        print(f"Unexpected status: {response.status_code}")
        log_error("robust_api_demo", "HTTPError", f"{response.status_code} for product ID 1")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
    log_error("robust_api_demo", "ConnectionError", "Could not reach server")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
    log_error("robust_api_demo", "Timeout", "Request timed out")
except Exception as e:
    print(f"Unexpected error: {e}")
    log_error("robust_api_demo", "Exception", str(e))

# --- Part D: Input Validation Loop ---

print("\n========== Product ID Lookup ==========")

while True:
    user_input = input("Enter a product ID to look up (1–100), or 'quit' to exit: ").strip()

    if user_input.lower() == "quit":
        print("Exiting product lookup.")
        break

    # Validate: must be a digit string
    if not user_input.isdigit():
        print("  ⚠ Warning: Please enter a valid integer.")
        continue

    product_id = int(user_input)

    # Validate: must be within range 1–100
    if product_id < 1 or product_id > 100:
        print("  ⚠ Warning: ID must be between 1 and 100.")
        continue

    # Valid input — make API call
    try:
        response = requests.get(f"{BASE_URL}/{product_id}", timeout=5)

        if response.status_code == 404:
            print("  Product not found.")
            log_error("lookup_product", "HTTPError", f"404 Not Found for product ID {product_id}")
        elif response.status_code == 200:
            p = response.json()
            print(f"  Title: {p['title']}  |  Price: ${p['price']}")
        else:
            print(f"  Unexpected status: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("  Connection failed. Please check your internet.")
        log_error("lookup_product", "ConnectionError", f"Failed for product ID {product_id}")
    except requests.exceptions.Timeout:
        print("  Request timed out. Try again later.")
        log_error("lookup_product", "Timeout", f"Timeout for product ID {product_id}")
    except Exception as e:
        print(f"  Unexpected error: {e}")
        log_error("lookup_product", "Exception", str(e))


# ============================================================
# Task 4 — Logging to File (4 marks)
# ============================================================

print("\n========== Intentional Log Triggers ==========")

# Trigger 1: ConnectionError — genuinely unreachable URL
print("\nTrigger 1: Unreachable URL")
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except requests.exceptions.ConnectionError:
    print("  Connection failed as expected.")
    log_error("fetch_products", "ConnectionError", "No connection could be made to unreachable host")
except requests.exceptions.Timeout:
    print("  Request timed out.")
    log_error("fetch_products", "Timeout", "Unreachable host timed out")

# Trigger 2: HTTP 404 — non-existent product ID
# Note: 404 is NOT a Python exception — detected via status_code check
print("\nTrigger 2: Non-existent product ID 999")
try:
    response = requests.get(f"{BASE_URL}/999", timeout=5)
    if response.status_code != 200:
        print(f"  HTTP {response.status_code} — product not found.")
        log_error("lookup_product", "HTTPError", "404 Not Found for product ID 999")
    else:
        print(f"  Product: {response.json()['title']}")
except Exception as e:
    log_error("lookup_product", "Exception", str(e))

# Print full error_log.txt contents
print("\n========== error_log.txt Contents ==========")
with open("error_log.txt", "r", encoding="utf-8") as f:
    print(f.read())
