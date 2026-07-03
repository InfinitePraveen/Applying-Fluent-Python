# Create a class 'ReadOnlyList' that takes a list at init.
# It should support __getitem__, __len__, and __iter__,
# but raise TypeError when someone tries __setitem__ or append/del.

from typing import Any, Iterable, Iterator, List

class ReadOnlyList:
    def __init__(self, initial_list: Iterable[Any]):
        # Store a shallow copy to prevent the internal list 
        # from being modified externally through its original reference
        self._data: List[Any] = list(initial_list)

    def __getitem__(self, index: int | slice) -> Any:
        return self._data[index]

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[Any]:
        return iter(self._data)

    def __setitem__(self, index: int | slice, value: Any) -> None:
        raise TypeError("'ReadOnlyList' object does not support item assignment")

    def __delitem__(self, index: int | slice) -> None:
        raise TypeError("'ReadOnlyList' object does not support item deletion")

    def __repr__(self) -> str:
        return f"ReadOnlyList({self._data})"

    # Explicitly prevent common mutation methods by raising an AttributeError
    # or a TypeError depending on your architectural choice.
    def append(self, value: Any) -> None:
        raise TypeError("'ReadOnlyList' object has no mutation attribute 'append'")
    

# DO NOT inherit from list.