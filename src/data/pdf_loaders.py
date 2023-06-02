# code for loading pdfs and saving them as texts

import PyPDF2

class PdfToTextLoader:
    """
        Class for loading pdfs and saving them as texts
    """

    def __init__(self, pdf_path, output_path):
        """
            Args:
                pdf_path (str): path to pdf file
                output_path (str): path to save text file
        """
        self.pdf_path = pdf_path
        self.output_path = output_path

    def load_pdf(self):
        """
            Loads pdf file and saves it as text file
        """
        with open(self.pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            num_pages = pdf_reader.numPages
            text = ''
            for page in range(num_pages):
                page = pdf_reader.getPage(page)
                text += page.extractText()
            with open(self.output_path, 'w') as text_file:
                text_file.write(text)
        return text