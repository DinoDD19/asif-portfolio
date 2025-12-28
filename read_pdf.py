import sys

try:
    import PyPDF2
    pdf_path = r"C:\Users\siyad\Downloads\CV.pdf"
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        print(text)
except ImportError:
    print("PyPDF2 not installed. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    print("\nPlease run this script again.")
except Exception as e:
    print(f"Error reading PDF: {e}")
    print("\nTrying alternative method with pdfplumber...")
    try:
        import pdfplumber
        pdf_path = r"C:\Users\siyad\Downloads\CV.pdf"
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            print(text)
    except ImportError:
        print("Please install: pip install PyPDF2 or pip install pdfplumber")
