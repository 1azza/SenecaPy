import requests
from pprint import pprint
from seneca.Modules.errors import (CourseNotFound, InvalidUrl)
from seneca.Modules.key import CORRELATOINID
class Course:
    def __init__(self):
        pass


    def _parseUrl(self, url):
        try:
            courseId = url.split('course/')[1].split('/section')[0]
            SectionId = url.split('section/')[1].split('/session')[0]
            return [courseId, SectionId]
        except:
            raise InvalidUrl(url)





    
    def _Parse(self, data):
                
        #Finds Modules Ids and Number of Modules
            NumberOfModules = 0
            ModuleIds = []
            for i in data.get("moduleIds"):
                NumberOfModules += 1
                ModuleIds.append(i)
                
                
            #Finds title
            title = data.get('title')

            #Output
            print(f'---{title}---')
            print(f'NumberOfQuestions:\n{NumberOfModules}\n')



            Modules = []
            contents = data.get('contents')
            Question = 0
            for i in contents:
                contentModules = i.get('contentModules')
                for i in contentModules:
                    Modules.append({ Question:[i.get('content'), i.get('moduleType')]})
                    
                    Question += 1


            def Calculate(Type, q):
                if Type == 'equation':
                    a = [q.get('title')]
                    a.append(q.get('blocks')[0].get('word'))
                    return a
                elif Type == 'multiple-choice':
                    a = [q.get('statement')]
                    a.append(q.get('correctAnswer'))
                    return a
                elif Type == 'toggles':
                    a = [q.get('statement')]
                    amount = q.get('toggles')
                    Correct = []
                    for i in amount:
                        Correct.append(i.get('correctToggle'))
                    a.append(Correct)
                    return a
                elif Type == 'wordfill':
                    a = [Type]
                    a.append(q.get('words')[-2].get('word'))
                    return a
                elif Type == 'worked-example':
                    a = [q.get('question')]
                    steps = q.get('steps')
                    Correct = []
                    for i in steps:
                        try:
                            Correct.append(i.get('equation')[1].get('word'))
                        except:
                            continue
                    a.append(Correct)
                    return a
                
                elif Type == 'grid':
                    a = [q.get('title')]
                    Correct = []
                    for i in q.get('definitions'):
                        try:
                            Correct.append(i.get('word')[1].get('word'))
                        except:
                            continue
                    a.append(Correct)
                    return a
                
                elif Type == 'exact-list':
                    a = [q.get('statement')]
                    Correct = []
                    for i in q.get('values'):
                        Correct.append(i.get('value')[0].get('word'))
                    a.append(Correct)
                    return a
                
                elif Type == 'multiSelect':
                    a = [q.get('question')]
                    Correct = []
                    for i in q.get('options'):
                        if i.get('correct') == True:
                            Correct.append(i.get('text'))
                    a.append(Correct)
                    return a
                elif Type == 'image':
                    a = [Type]
                    a.append(q)
                    return a
            
                
            Answers = {}
            for i in range(len(Modules)):
                q = Modules[i].get(i)
                Type = q[1]
                Content = q[0]
                # continue
                Result = Calculate(Type, Content)
                if Result:
                    Answers[i] = Result

            return Answers
        
        
        
        
    def QueryCourses(self, number:int):

        url = "https://course.app.senecalearning.com/api/courses/queryCourses"

        payload = {
                "sort": ["firstPublished:desc"],
                "size": number
            }
        headers = {"correlationid": "1647887386631::02e946994d35a04376af966b404386fc"}

        response = requests.request("POST", url, json=payload, headers=headers)
        courses = response.json()
        courses = courses.get('results').get('hits')
        return courses        
        
    def getAnswers(self, url:str):
        Course = self.getCourseInfo(url)
        Answers = self._Parse(Course)
        return Answers
    def getCourseInfo(self, url:str):

        Template = ['https://course.app.senecalearning.com/api/courses/', '/signed-url']
        Ids = self._parseUrl(url)
        Template.insert(1, Ids[0])
        self.url = ''.join(Template)
        querystring = {"sectionId":Ids[1]}
        headers = {
            "authority": "course.app.senecalearning.com",
            "correlationid": CORRELATOINID,
        }
      
        response = requests.request("GET", self.url, headers=headers, params=querystring)
        if response.status_code != 200:
            raise CourseNotFound()
        self.url =  response.json().get('url')
        response = requests.request("GET", self.url, headers=headers)
        Course = response.json()
        return Course
