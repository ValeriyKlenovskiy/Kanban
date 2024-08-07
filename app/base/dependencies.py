from copy import copy

from fastapi import HTTPException, status


def make_new_ordering(model_id: int, ordering: list[int], end_pos: int):
    if model_id not in ordering or end_pos > len(ordering) or end_pos < 1:
        return HTTPException(status_code=status.HTTP_409_CONFLICT)
    end_pos -= 1
    new_ordering = copy(ordering)
    new_ordering.remove(model_id)
    new_ordering.insert(end_pos, model_id)
    return new_ordering

