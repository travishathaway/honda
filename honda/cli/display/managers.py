import abc
from contextlib import contextmanager
from urllib import parse
from typing import Callable, Optional

import httpx
from rich.progress import Progress


class DisplayManager(abc.ABC):
    @abc.abstractmethod
    async def display(
        self,
        header_resp: httpx.Response,
        resp: httpx.Response,
        callback: Optional[Callable] = None,
    ):
        """Abstract method for a display managers"""


class ProgressDisplayManager(DisplayManager):
    """
    This class wraps the "Progress" class, which allows us to add some extra methods to it.
    """

    def __init__(self, progress: Progress) -> None:
        self.progress = progress

    async def display(
        self,
        header_resp: httpx.Response,
        resp: httpx.Response,
        callback: Optional[Callable] = None,
    ) -> None:
        url = parse.urlparse(str(resp.url))
        size_bytes = int(self.__get_content_length(header_resp.headers))
        task = self.progress.add_task(f"{url.hostname}{url.path}", total=size_bytes)

        async for data in resp.aiter_bytes(chunk_size=1024):
            if callback:
                await callback(data)
            self.progress.update(task, advance=1024)

    @staticmethod
    def __get_content_length(headers) -> str:
        return headers.get("Content-Length") or headers.get("content-length", "0")


@contextmanager
def progress_ctx_manager() -> ProgressDisplayManager:
    with Progress() as progress:
        yield ProgressDisplayManager(progress)


class SilentDisplayManager(DisplayManager):
    async def display(
        self,
        header_resp: httpx.Response,
        resp: httpx.Response,
        callback: Optional[Callable] = None,
    ):
        """Write the file incrementally"""
        async for data in resp.aiter_bytes(chunk_size=1024):
            if callback:
                await callback(data)


@contextmanager
def silent_ctx_manager() -> None:
    """
    Dummy context manager that doesn't do anything. This is meant to be used when
    turning off any output.
    """
    yield SilentDisplayManager()
