class SenecaError (Exception):
    def CourseNotFound(self, course):
        raise Exception(f'Course not found \n{course}')
    def InvalidUrl(self, url):
        raise Exception(f'Invalid Url: \n{url}')
errors = SenecaError()