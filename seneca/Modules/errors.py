class SenecaError (Exception):
    def CourseNotFound(self, course):
        raise SenecaError(f'\nCourse not found \n{course}')
    def InvalidUrl(self, url):
        raise SenecaError(f'\nInvalid Url: \n{url}')
errors = SenecaError()