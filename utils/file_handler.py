from pypdf import PdfReader

def read_file(file):

    if file.name.endswith(".txt"):

        return file.read().decode()

    elif file.name.endswith(".pdf"):

        pdf = PdfReader(file)

        text = ""

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:

                text += extracted

        return text

    return ""