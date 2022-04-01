import seneca
from pprint import pprint


#This script will attempt to output answers from a seneca course

url = input('Please enter url for seneca course')
data = seneca.course.getAnswers(url)
pprint(data)
