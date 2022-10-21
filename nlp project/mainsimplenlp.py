import nltk
from newspaper import Article
import tkinter
from textblob import TextBlob
import csv



# opening the CSV file
with open('links(educative.io).csv', mode ='r',encoding='utf8')as file:
    csvFile = csv.reader(file)

    for lines in csvFile:
        
        a=str(lines[0])

        print(a)

        url=str(lines[0])

        try:


            article = Article(url)

            article.download()
            article.parse()

            article.nlp()

            data = str(article.title).replace("\n"," ").replace("\t"," ").replace(","," ")+" , "+str(article.summary).replace("\n"," ").replace("\t"," ").replace(","," ")

            file1 = open("myfile.txt", "a",encoding='utf8')  # append mode
            file1.write(str(data))
            file1.close()
            print(data)
        except:
            print("article not found:::::::::::")

