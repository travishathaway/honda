import asyncio
from pathlib import Path
from typing import Optional
from urllib import parse

import aiofiles
import httpx

from honda.cli.display.managers import progress_ctx_manager, ProgressDisplayManager

CONCURRENT_LIMIT = 5


async def limited_download(
    urls: tuple[str],
    dest: Path,
    limit: int = CONCURRENT_LIMIT,
    display_ctx_manager: Optional[progress_ctx_manager] = None,
) -> None:
    """
    Downloads files asynchronously but limits concurrency to `limit`
    """
    client = httpx.AsyncClient(http2=True)
    sem = asyncio.Semaphore(limit)  # This allows us a to limit our concurrency.

    async def _download_url(url, progress):
        async with sem:
            await download_url(client, url, dest, progress)

    with display_ctx_manager() as display_manager:
        tasks = tuple(_download_url(url, display_manager) for url in urls)
        await asyncio.gather(*tasks)


async def download_url(
    client: httpx.AsyncClient,
    url: str,
    dest: Path,
    display_manager: ProgressDisplayManager,
) -> None:
    """Downloads single file using aiohttp.Session and saves file to disk"""
    file_url = parse.urlparse(url)
    file_name = f'{file_url.hostname}-{file_url.path.lstrip("/").replace("/", "-")}'
    dest = dest.joinpath(file_name)

    async with aiofiles.open(dest, "wb") as fp:

        async def write_data(data):
            await fp.write(data)

        h_resp = await client.head(
            url, headers={"accept-encoding": ""}
        )  # get "content-length first
        req = client.build_request("GET", url)
        resp = await client.send(req, stream=True)

        resp.raise_for_status()  # TODO: error-handling

        await display_manager.display(h_resp, resp, write_data)
