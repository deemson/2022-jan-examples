from typing import Mapping, TypeVar, Iterator

K = TypeVar("K")
V = TypeVar("V")


class FrozenDict(Mapping[K, V]):
    def __init__(self, key_value_pairs: Mapping[K, V]) -> None:
        self._key_value_pairs = dict(key_value_pairs)

    def __getitem__(self, key: K) -> V:
        return self._key_value_pairs[key]

    def __len__(self) -> int:
        return len(self._key_value_pairs)

    def __iter__(self) -> Iterator[K]:
        return iter(self._key_value_pairs)

    def __hash__(self) -> int:
        return hash(frozenset({
            (key, value)
            for key, value in self._key_value_pairs.items()
        }))
