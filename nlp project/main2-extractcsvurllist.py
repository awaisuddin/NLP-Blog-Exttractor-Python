import nltk
import csv
from newspaper import Article
import tkinter
from textblob import TextBlob
import time


def printarticledata(url):

    article = Article(str(url).replace(" ",""))

    article.download()
    time.sleep(1)
    article.parse()

    article.nlp()

    data = str(article.title).replace("\n"," ").replace("\t"," ").replace(","," ")+" , "+str(article.summary).replace("\n"," ").replace("\t"," ").replace(","," ")

    file1 = open("myfile.txt", "a",encoding='utf8')  # append mode
    file1.write("\n"+str(data))
    file1.close()
    print(data)

if __name__=="__main__":
    with open('links(educative.io).csv', mode ='r',encoding='utf8')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            a=str(lines[0])
            print(a)

            url=str(lines[0])
            printarticledata(url)
            
        






           
