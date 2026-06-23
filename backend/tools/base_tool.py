from abc import ABC, abstractmethod


class BaseTool(ABC):

    @abstractmethod
    def get_metadata(self):
        pass

    @abstractmethod
    def execute(self, **kwargs):
        pass