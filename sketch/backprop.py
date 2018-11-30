from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Generic, NamedTuple, TypeVar

_INPUT = TypeVar('_INPUT', tuple)
_OUTPUT = TypeVar('_OUTPUT', tuple)


class Network(Generic[_INPUT, _OUTPUT]):

    def __init__(self, layers: List[Layer]):
        self.layers = layers
        self.ross = None

    @staticmethod
    def error(actual, expected) -> float:
        pass

    def learn(self, train: NamedTuple[_INPUT, _OUTPUT]) -> None:
        self.implement(train.input)
        self.request()
        self.update()

    def implement(self, input: _INPUT):
        """Call implement methods"""
        for layer in self.layers:
            results = layer.implement(input)
            layer._args = input
            layer._results = results
            input = results

    def request(self, output: _OUTPUT) -> None:
        """Call request methods"""
        for layer in self.layers[::-1]:
            pass

    def update(self) -> None:
        """Call update methods"""
        pass


class Layer:

    class Param(tuple):
        pass

    class Args(tuple):
        pass

    class Results(tuple):
        pass

    def __init__(self, nodes: List[Node], param: Param):
        self.nodes = nodes
        self._param = param
        self._args = None
        self._results = None

    def implement(self, args: Args) -> Results:
        self._args = args
        self._results = ...

        return self._results

    def request(self, args: Args, results: Results) -> Args:
        pass

    def update(self, args: Args, results: Results) -> None:
        pass
