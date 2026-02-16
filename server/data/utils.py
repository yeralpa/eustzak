import random
from enum import Enum
from typing import Type, TypeVar, List, Union

T = TypeVar('T', bound=Enum)

def randomEnum(clazz: Type[T], exclude: Union[List[T], None] = None) -> T:
    exclude = exclude or []
    choices = [member for member in clazz if member not in exclude]
    
    if not choices:
        raise ValueError("No valid enum members left after exclusion.")
        
    return random.choice(choices)