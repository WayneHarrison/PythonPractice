import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for p in doc.paragraphs:
        fullText.append(p.text)
    return '\n'.join(fullText)

print(getText(r'C:\Users\WayneJnr\Desktop\demo.docx'))
