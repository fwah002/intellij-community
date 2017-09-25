# Stubs for pprint

# Based on http://docs.python.org/2/library/pprint.html
# Based on http://docs.python.org/3/library/pprint.html

from typing import Any, Dict, Tuple, IO

def pformat(o: object, indent: int = ..., width: int = ...,
            depth: int = ...) -> str: ...
def pprint(o: object, stream: IO[str] = ..., indent: int = ..., width: int = ...,
           depth: int = ...) -> None: ...
def isreadable(o: object) -> bool: ...
def isrecursive(o: object) -> bool: ...
def saferepr(o: object) -> str: ...

class PrettyPrinter:
    def __init__(self, indent: int = ..., width: int = ..., depth: int = ...,
                 stream: IO[str] = ...) -> None: ...
    def pformat(self, o: object) -> str: ...
    def pprint(self, o: object) -> None: ...
    def isreadable(self, o: object) -> bool: ...
    def isrecursive(self, o: object) -> bool: ...
    def format(self, o: object, context: Dict[int, Any], maxlevels: int,
               level: int) -> Tuple[str, bool, bool]: ...
