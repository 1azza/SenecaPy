
"""File for defining errors"""


class SenecaError(Exception):
    """Base class for Seneca errors."""

class CourseNotFound(SenecaError):
    pass


class InvalidUrl(SenecaError):
    def __init__(self, url):
        super().__init__(str(url))

class InvalidCredentials(SenecaError):
    pass


class ServerError(SenecaError):
    pass