import asyncio
from asyncio import Future
from datetime import datetime

import requests
from requests import Response


async def check_status(url: str) -> dict[str, int | str]:
    start_time: datetime = datetime.now()
    response: Response = await asyncio.to_thread(requests.get, url, None)
    end_time: datetime = datetime.now()

    return {
        "url": url,
        "status": response.status_code,  # type: ignore
        "start_time": f"{start_time:%H:%M:%S}",
        "end_time": f"{end_time:%H:%M:%S}",
    }


async def main() -> None:
    print("Fetching data...")
    tasks: Future = asyncio.gather(
        check_status("https://www.google.com"),
        check_status("https://www.facebook.com"),
        check_status("https://www.youtube.com"),
        check_status("https://www.twitter.com"),
        check_status("https://www.linkedin.com"),
        check_status("https://www.instagram.com"),
        check_status("https://www.pinterest.com"),
        check_status("https://www.snapchat.com"),
        check_status("https://www.abcdefghijklmnopqrstuvwxyz.com"),
        return_exceptions=True,
    )

    results: list[dict[str, int | str]] = await tasks
    print("Data fetched!")
    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main=main())
