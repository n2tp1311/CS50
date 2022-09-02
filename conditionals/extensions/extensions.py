def main():
    images = ['gif', 'jpg', 'jpeg', 'png']
    texts = ['txt']
    applications = ['zip', 'pdf']
    fn = input('File name: ').lower().strip()
    # fn = 'cat.gif'
    suffix = findSuffix(fn)
    # lashSuffix = suffix.replace('.','') 
    # print(suffix)
    if suffix in images:
        print('image/'+suffix)
    elif suffix in texts:
        print('text/'+suffix)
    elif suffix in applications:
        print('application/'+suffix)
    else:
        print('application/octet-stream')

def findSuffix(fileName):
    dotPosition = fileName.find('.')
    suffix = fileName[dotPosition+1:len(fileName)]
    return suffix

main()