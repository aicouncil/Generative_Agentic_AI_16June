# Explanation of the Code (Step-by-Step)

This document explains the provided Python code for extracting, cleaning, splitting, and searching a PDF company manual. Each code section is explained with comments and examples.

---

## 1. Extracting Text from a PDF

```python
import PyPDF2

def extract_data_from_pdf(pdf_path):
    with open(pdf_path , 'rb') as file:
        pdfreader = PyPDF2.PdfReader(file)
        full_text = ''
        for page in pdfreader.pages:
            full_text += page.extract_text()
    return full_text

extracted_text = extract_data_from_pdf('/content/company_manual.pdf')
print(extracted_text)
```

**Explanation:**  
- `PyPDF2` is a Python library for working with PDF files.
- The function `extract_data_from_pdf` takes a PDF file path as input.
- It opens the PDF in binary read mode (`'rb'`).
- `PyPDF2.PdfReader(file)` reads the PDF file.
- It loops over all pages and extracts text from each, concatenating into a single string (`full_text`).
- The function returns the combined text.
- Example: If your PDF has 3 pages, all their text will be joined and printed.

---

## 2. Cleaning Extracted Text

```python
import re

def clean_text(text):
    # remove extra spaces
    text = re.sub(r'\s+' , ' ' , text)
    # remove non-ascii characters (if any)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    return text

cleaned_text = clean_text(extracted_text)
print(cleaned_text)
```

**Explanation:**  
- `re` is Python's regular expression module.
- `re.sub(r'\s+', ' ', text)` replaces all whitespace (spaces, newlines, tabs) with a single space.
- `re.sub(r'[^\x00-\x7F]+', '', text)` removes all non-ASCII characters (special symbols, etc.).
- The cleaned text is easier to process and search.

---

## 3. Splitting Text by Section

```python
sections = {
    "About the Company": cleaned_text.split('About the Company')[1].split('Return Policy')[0],
    "Return Policy": cleaned_text.split('Return Policy')[1].split('Warranty')[0],
    "Warranty": cleaned_text.split('Warranty')[1].split('Customer Service')[0],
    "Customer Service": cleaned_text.split('Customer Service')[1].split('Environmental Commitment')[0],
    "Environmental Commitment": cleaned_text.split('Environmental Commitment')[1]
}
print(sections.items())

for section_title, content in sections.items():
    print(f"Section Title: {section_title}")
    print(f"Content: {content}")
```

**Explanation:**  
- The manual is split into sections using known headings.
- For each section, `split` is used to extract the text between headings.
    - E.g., `"About the Company"` section is found between "About the Company" and "Return Policy".
- All sections are stored in a dictionary called `sections`.
- Loop prints the section title and its content.

**Example Output:**
```
Section Title: About the Company
Content: TechNova Solutions Pvt. Ltd. is a global leader in consumer electronics...
```

---

## 4. Case-Insensitive Keyword Search in a String

```python
sample_text = "About the company"
print('about' in sample_text.lower())
```

**Explanation:**  
- Converts the string to lowercase for case-insensitive search.
- Checks if "about" is in the text.
- Output: `True`

---

## 5. Simple Query Matching Function

```python
def query_matching(query, sections):
    query = query.lower()
    for section_title, content in sections.items():
        if query in content.lower():
            return f"Bot: Section Title: {section_title}\nContent: {content}"
    return "Bot: I couldn't find the relevant result"

user_query = "what is the return policy?"
responses = query_matching(user_query, sections)
print(responses)
```

**Explanation:**  
- The function checks if the user's query (converted to lower-case) appears anywhere in the contents of any section.
- If found, returns the section title and content.
- If not found, returns a fallback message.
- Example: Searching for "return policy" will return the full "Return Policy" section.

---

## 6. Improved Query Matching (Keyword Hits)

```python
def query_matching(query , sections):
    query_keywords = re.findall(r'\w+', query.lower())
    max_hits = 2
    best_match = None

    for section_title, content in sections.items():
        content_lower = content.lower()
        hits = 0
        for word in query_keywords:
            if (word in content_lower) or (word in section_title.lower()):
                hits += 1
        print(f"Checking in section: {section_title} - matched {hits} keyword")
        if hits > max_hits:
            max_hits = hits
            best_match = (section_title, content)

    if best_match:
        title, content = best_match
        return f"Bot: Section Title: {title}\nContent: {content}"
    else:
        return "Bot: I couldn't find the relevant result"

user_query = "tell me about company"
responses = query_matching(user_query, sections)
print(responses)

user_query = "what is your warranty process"
responses = query_matching(user_query, sections)
print(responses)

user_query = "I want to return?"
responses = query_matching(user_query, sections)
print(responses)
```

**Explanation:**  
- Splits the query into keywords (words).
- For each section, counts how many keywords appear in the section title or content.
- Keeps track of the section with the highest keyword matches (must be more than 2).
- Returns the best-matching section's title and content.
- If nothing matches well, returns a fallback message.
- Example: For `user_query = "what is your warranty process"`, the function will likely match the "Warranty" section.

---

# Summary Table

| Code Section                   | Purpose                                           |
|------------------------------- |--------------------------------------------------|
| Extracting PDF Text            | Read and combine text of all pages from PDF       |
| Cleaning Extracted Text        | Remove extra spaces and special characters        |
| Splitting Text by Section      | Organize manual into key sections by headings     |
| Case-Insensitive Search        | Demonstrate simple search technique               |
| Simple Query Matching          | Find section containing query string              |
| Improved Query Matching        | Find section with most keywords from the query    |

---
