class APIResponseCode(object):
    FAILURE = {"code": -1, "message": 'General failure'}  # General logic error
    SUCCESS = {"code": 0, "message": 'Success'}  # Successful response
    SERVER_ERROR = {"code": 1, "message": 'Server error'}  # Unexpected error during handling the request
    BAD_REQUEST = {"code": 2, "message": 'Bad request'}  # Error returned by DRF serializer
    NO_PERMISSION = {"code": 3, "message": 'No permission'}  # Error related to permissions
    NOT_FOUND = {"code": 4, "message": 'Not found'}  # Object not found
    ALREADY_EXISTS = {"code": 5, "message": 'Already exists'}  # Object already exists
    VALIDATION_ERROR = {"code": 6, "message": 'Validation error'}  # Error related to invalidated input
    INVALID_ACTION = {"code": 7, "message": 'Invalid request'}  # Invalid action (stateful)
    ACTION_DENIED = {"code": 8, "message": 'Action denied'}  # Invalid action (stateless)
    FILE_ERROR = {"code": 9, "message": 'File error'}  # Error related to file handling
    DB_ERROR = {"code": 10, "message": 'Database error'}  # Error related to database
    EXT_API_ERROR = {"code": 11, "message": 'External API error'}  # Error related to calling external API
    TIMEOUT = {"code": 12, "message": 'Request timed out'}  # Timeout when handling a request
    EXPIRED = {"code": 13, "message": 'Request expired'}
    TOO_MANY_REQUEST = {"code": 14, "message": 'Too many request'}

    @classmethod
    def is_success(cls, code):
        return code == cls.SUCCESS

    @classmethod
    def is_failure(cls, code):
        return code != cls.SUCCESS
