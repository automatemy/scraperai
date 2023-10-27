from abc import abstractmethod, ABC


class BrowserScraper(ABC):
    def get(self, url: str):
        ...

    @property
    @abstractmethod
    def page_source(self) -> str:
        ...

    @abstractmethod
    def wait(self, timeout: float, locator):
        ...

    @abstractmethod
    def set_storage(self, key, value):
        ...

    @abstractmethod
    def execute_cdp_cmd(self, cmd: str, cmd_args: dict):
        ...

    @abstractmethod
    def close(self):
        ...
