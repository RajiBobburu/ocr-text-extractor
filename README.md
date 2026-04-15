# Advanced OCR Text Extractor

An advanced OCR (Optical Character Recognition) web application built using **EasyOCR** and **Streamlit**.  
This app extracts text from images with **visualization, confidence filtering, and export features**.
---
## Overview
This project allows users to upload an image and extract text from it in real time.  
It enhances traditional OCR by adding:
- Bounding box visualization (text detection areas)
- Confidence-based filtering
- Text statistics (words, characters, confidence)
- Download options (TXT & JSON)
---
## Features
- Multi-language OCR support (English, Hindi, etc.)
- Adjustable confidence threshold
- Bounding box visualization on detected text
- Segment-wise detection with confidence scores
- Extracted text display
- Word & character count
- Download extracted text as TXT
- Download structured data as JSON
- Interactive UI using Streamlit
---
## Architecture
- User Input → OCR Engine → Text Extraction → Filtering → Visualization → Output
---
## Tech Stack
- **Python**
- **EasyOCR**
- **Streamlit**
- **NumPy**
- **Pillow**
---
## How to Run
### 1️. Clone the Repository
### 2️. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️. Run the Application
```bash
streamlit run app.py
```
---
## Sample Use Cases
- Document digitization
- Business card information extraction
- Invoice processing
- Sreenshot text extraction
- Multilingual text recognition
---
## Limitations
- Accuracy depends on image quality
- Handwritten text may have lower accuracy
- Complex layouts (tables/forms) may not be perfectly structured
---
## Demo
<img width="1883" height="951" alt="image" src="https://github.com/user-attachments/assets/5b7530af-cad8-4d15-afdd-9a1db103a71d" />
<img width="1876" height="901" alt="image" src="https://github.com/user-attachments/assets/0a6113b2-eea3-4370-be7e-8980fe2df499" />
<img width="1849" height="888" alt="image" src="https://github.com/user-attachments/assets/5b070197-c2d2-4dbb-9839-2883d858425b" />


Author : Raji Bobburu



