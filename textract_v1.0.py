# -*- coding: utf-8 -*-
"""
Converts an uploaded file into a python string.
returns: str
"""
def text_converter(file_path, encoding=None, file_extension=None):
    import textract
    
    if file_extension==None and encoding==None:
        text = textract.process(file_path)
    elif file_extension==None:
        text = textract.process(file_path, encoding=encoding) 
    elif encoding==None:
        text = textract.process(file_path, extention=file_extension)

    if encoding!=None:
        text = text.decode(encoding=encoding)
    else:
        text = text.decode()
    
    return text

text = text_converter('Files/SQL.txt', encoding='ascii')
print(text)