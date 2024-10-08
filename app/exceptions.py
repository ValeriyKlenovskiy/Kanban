from fastapi import HTTPException, status


class KanbanException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExists(KanbanException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User Already Exists"


class IncorrectEmailOrPassword(KanbanException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect Email Or Password"


class NotAllowed(KanbanException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Not Allowed"


class TokenExpired(KanbanException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token Expired"


class TokenAbsent(KanbanException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token Absent"


class IncorrectTokenFormat(KanbanException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect Token Format"


class IncorrectToken(KanbanException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Incorrect Token"


class UserAbsent(KanbanException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User Absent"


class CannotAddDataToDatabase(KanbanException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Can not Add Data To Database"


class NoSpace(KanbanException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "No Space with this id"


class NoBoard(KanbanException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "No Board with this id"


class NoList(KanbanException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "No List with this id"


class AlreadyInAllowed(KanbanException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Already In Allowed"


class NotInAllowed(KanbanException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Not In Allowed"


class NoVerificationTokenForYourEmail(KanbanException):
    status_code = status.HTTP_409_CONFLICT
    detail = "No Verification Token For Your Email"


class AlreadyVerified(KanbanException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Already Verified"

class DeadlineBeforeAdding(KanbanException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Deadline Before Adding"
    HTTPException(status_code=status.HTTP_409_CONFLICT)
