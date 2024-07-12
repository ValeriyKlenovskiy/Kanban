from fastapi import HTTPException, status


class KanbanException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExists(KanbanException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class IncorrectEmailOrPassword(KanbanException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный логин или пороль"


class NotAllowed(KanbanException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Не разрешено"


class TokenExpired(KanbanException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен истек"


class TokenAbsent(KanbanException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class IncorrectTokenFormat(KanbanException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"


class UserAbsent(KanbanException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Нет пользователя"


class CannotAddDataToDatabase(KanbanException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Не удалось добавить запись"
