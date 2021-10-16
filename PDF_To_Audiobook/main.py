import pyttsx3  # Package to convert text to speech
import PyPDF2   # Library to read PDFs

pdf_location = input('Please provide the location of pdf to read: ')

pdf = open(pdf_location, 'rb')

reader = PyPDF2.PdfFileReader(pdf)

total_pages = reader.numPages   # Gives total pages in the pdf

speaker = pyttsx3.init()  # Initialize the speaker

entire_text = ""    # Contains the entire text of the pdf

for page_num in range(0, total_pages):

    read_page = reader.getPage(page_num)

    text = read_page.extractText()  # Extracts the text from the page

    entire_text += text

speaker.save_to_file(entire_text, 'audiobook.mp3')

speaker.runAndWait()
