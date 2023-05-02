from typing import Any, Tuple, Union, Callable, TypeVar

TCallable = TypeVar("TCallable", bound=Callable[..., Any])


def validate_string(s: str) -> bool: ...
def check_for_equivalence(func: TCallable) -> TCallable: ...
def check_for_none(func: TCallable) -> TCallable: ...
def check_empty_string(func: TCallable) -> TCallable: ...
def asciionly(s: str) -> str: ...
def asciidammit(s: Union[str, bytes]) -> str: ...
def make_type_consistent(s1: str, s2: str) -> Tuple[str, str]: ...
def full_process(s: str, force_ascii: bool = ...) -> str: ...
def intr(n: float) -> int: ...
