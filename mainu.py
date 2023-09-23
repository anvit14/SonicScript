import PyPDF2
from gtts import gTTS

pdfreader = PyPDF2.PdfReader('book.pdf')
pdf_text = ""

for page in pdfreader.pages:
    text = page.extract_text()
    clean_text = text.strip().replace('\n', ' ')
    pdf_text += clean_text + ' '

# Save the PDF text as an MP3 file
tts = gTTS(text=pdf_text, lang='en')
tts.save('story.mp3')
