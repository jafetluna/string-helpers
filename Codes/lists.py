import pyperclip
import re

def is_all_numeric(text):
    return bool(re.fullmatch(r'[\s\d]+', text))

def sql_format():
    return init(True)

def text_format():
    return init(False)
 
def init(Sql = False):
    clipboard_text = pyperclip.paste()
    if(is_all_numeric(clipboard_text)):
        line_text = clipboard_text.replace('\r','').replace(' ','').split('\n')
        clipboard_text = ''
        for line in line_text:
            if line == '':
                continue
            clipboard_text += f'{line},'
            clipboard_text = clipboard_text[:-1]
    else:
        line_text = clipboard_text.replace('\r','').replace(' ','').split('\n')
        caracter = '\'' if Sql else '"'
        clipboard_text = ''
        for line in line_text:
            if line == '':
                continue
            clipboard_text +=  f'{caracter}{line}{caracter}, '
        clipboard_text = clipboard_text[:-2]

    pyperclip.copy(clipboard_text)

