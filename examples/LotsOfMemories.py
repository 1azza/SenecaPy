from pprint import pprint
import seneca
import time


#This script will attempt to add a ton of memories to your account

User = seneca.User('USERNAME', 'PASSWORD')
courses = seneca.course.QueryCourses()
country =  User.memories.AllCountries()
x = 0
print(len(courses))
for i in courses:
    CourseId = i.get('_id')
    SectionIds = i.get('_source').get('sectionIds')

    for i in SectionIds:
        User.memories.SetMemory(CourseId, i, '58385a25-e8a6-448b-8445-713a85085217', str(time.gmtime()), str(time.gmtime()))
        x += 1
        print(x)
