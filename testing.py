import seneca
import logging
from pprint import pprint
import json
# logging.basicConfig(level=logging.DEBUG)
x = seneca.course.getCourseInfo('https://app.senecalearning.com/classroom/course/58c6df33-dead-4916-a8eb-bf6ec2b42923/section/eacd05f3-7b86-46d5-a6f2-fad87788a0f4/session')
with open('bin\Course.json', 'w') as f:
    data = json.dumps(x, indent=4, sort_keys=True)
    f.write(data)