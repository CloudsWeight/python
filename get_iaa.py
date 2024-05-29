'''
Convert PDF to Folder with text pages...
+ Creates a folder within the current directory.
+ pages in the folder are labeled as [pagexx.txt]
+ plenty of room for AI text scraping o_0**

'''
#######################
from PyPDF2 import PdfReader
import requests, os, shutil
from pathlib import Path
########################
#### URL of any pdf 
url = 'https://www.cia.gov/readingroom/docs/DOC_0001247372.pdf'
r = requests.get(url)
chunk_size = 2000 #bs for stream download

#############
def get_url(url = 'https://www.cia.gov/readingroom/docs/DOC_0001247372.pdf'):
    url = url
    r = requests.get(url)
    with open('test.pdf', 'wb') as fd: #label downloaded pdf as test.pdf
        for chunk in r.iter_content(chunk_size):#iterate over byte stream
            fd.write(chunk) #write chunk to file 
    fd.close()
    return 'test.pdf' #function returns downloaded pdf as this value

def take_and_change(file):
    file = file
    current_dir = os.getcwd()
    src = f"{current_dir}/{file}"

    try:
        os.mkdir('NewDir')
    except:
        'already exists'
    dst = f"{current_dir}/NewDir"
    os.chdir(dst)
    pwd = os.getcwd()
    print(pwd)
    try:
        shutil.move(src, dst)
    except:
        'already exists'
    print(os.listdir(dst))
    return f"{dst}"

################
def read_pdf(pdf):
    pdf = pdf #set pdf from input
    os.chdir(take_and_change(pdf))  
    reader = PdfReader(pdf) # use PDFReader on our pdf
    length = (len(reader.pages)) #use pages function of PdfReade class
    i = 0 # use i for page number
    while i < length:
        file = f"page{i}.txt" # very detailed
        page  = reader.pages[i]
        text = page.extract_text() # use extract_text function
        with open (file, 'w') as fd: # current text page file
            fd.write(text) # write extracted text
        i += 1


if __name__ == '__main__':
    pdf = get_url()
    read_pdf(pdf)
    
 
