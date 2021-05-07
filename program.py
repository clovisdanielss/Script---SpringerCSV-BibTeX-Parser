import urllib.request
import urllib.parse
import re

file = open('./SearchResults.csv',encoding="utf8")

result = []
for linha in file:
    print(linha)
    try:
        result.append(linha.split(",")[5])
    except:
        print("Faltou atributo na leitura...")

resultText = ""
index = 1
for doi in result[1:]:
    doi = doi.replace("\"","")
    url = "https://citation-needed.springer.com/v2/references/" + doi + "?format=bibtex&flavour=citation"
    print(url)
    try:
        response = urllib.request.urlopen(url)
        if(response.status < 300):
            contents = response.read()
            contents = contents.decode("utf-8")
            print("Artigo " + str(index))
            index += 1
            resultText += contents
        else:
            print("Houve um erro")
    except:
        print("Houve um erro")


file.close()
print("Resultado Final:",resultText)
file = open("teste.txt", "w",encoding="utf8")
file.write(resultText)
file.close()
