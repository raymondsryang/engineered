from typing import Protocol, Any


class Picklable(Protocol):
    def __getstate__(self) -> Any:
        ...

    def __setstate__(self, state: Any) -> None:
        ...