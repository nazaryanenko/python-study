# Get text from file and remove all punctuations split text to list of words

def getFileContent(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("wrong path")

def cleanUpPunctuation(content):
    cleanUpChars = ".,!:;?\"\'"
    for char in cleanUpChars:
        content = content.replace(char, "")
    return content

def handleFile(path):
    content = getFileContent(path)
    return cleanUpPunctuation(content).split()

print(handleFile('./task_1/text.txt'))
