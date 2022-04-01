import seneca
from pprint import pprint


#This script will attempt to output answers from a seneca course

url = input('Please enter url for seneca course')
data = seneca.course.getAnswers(url)
pprint(data)

#so this is python
#python is a basic program languages geared towards beginers
#it is very cool
#this code does stuff with seneca
#and is made by larry rennoldson
