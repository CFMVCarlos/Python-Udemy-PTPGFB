# call func1(delay=2)
# call func2(delay=1)
# func2() has finished
# func1() has finished

import asyncio
from asyncio import Future, Task
from datetime import datetime


async def fetch_data(
    input_data: int, *, delay: int = 3, fails: bool = False
) -> dict[str, int | str]:
    print(f"[{input_data}] Fetching data...")
    start_time: datetime = datetime.now()
    await asyncio.sleep(delay)
    end_time: datetime = datetime.now()

    if fails:
        raise ValueError("Failed to fetch data...")

    print(f"[{input_data}] Data retireved!")
    return {
        "input": input_data,
        "start_time": f"{start_time:%H:%M:%S}",
        "end_time": f"{end_time:%H:%M:%S}",
    }


async def main1() -> None:
    task1: Task[dict[str, int | str]] = asyncio.create_task(fetch_data(input_data=1))
    task2: Task[dict[str, int | str]] = asyncio.create_task(fetch_data(input_data=2))
    data1: dict[str, int | str] = await task1
    data2: dict[str, int | str] = await task2
    print(f"{data1=}")
    print(f"{data2=}")


async def main2() -> None:
    task: Task[dict[str, int | str]] = asyncio.create_task(fetch_data(1, delay=3))
    await asyncio.sleep(1)
    print("Running other code...")
    data: dict[str, int | str] = await task
    print(f"{data=}")

    print()

    task2: Task[dict[str, int | str]] = asyncio.create_task(fetch_data(2, delay=10))
    await asyncio.sleep(1)
    task2.cancel(msg="Took too long...")
    try:
        data2: dict[str, int | str] = await task2
        print(f"{data2=}")
    except asyncio.CancelledError as e:
        print("\tTask was cancelled...", e, task2.cancelled(), sep="\n\t")

    print()

    task3: Task[dict[str, int | str]] = asyncio.create_task(fetch_data(3, delay=3))
    await asyncio.sleep(1)
    task3.cancel(msg="Took too long...")
    try:
        data3: dict[str, int | str] = task3.result()
        print(f"{data3=}")
    except asyncio.InvalidStateError as e:
        print(f"\t{e}")

    print()

    task4: Task[dict[str, int | str]] = asyncio.create_task(fetch_data(4, delay=3))
    print(task4.done())
    data4: dict[str, int | str] = await task4
    print(f"{data4=}")
    print(task4.done())

    print()

    task5: Task[dict[str, int | str]] = asyncio.create_task(fetch_data(5, delay=30))
    try:
        data5: dict[str, int | str] = await asyncio.wait_for(task5, timeout=3)
        print(f"{data5=}")
    except asyncio.TimeoutError as e:
        print(f"\tRequest took too long: {e}")


async def main3() -> None:
    tasks: Future = asyncio.gather(
        fetch_data(1, delay=1, fails=True),
        fetch_data(2, delay=2),
        fetch_data(3, delay=1),
        return_exceptions=True,
    )

    results: list[dict[str, int | str]] = await tasks
    for result in results:
        print(result)


if __name__ == "__main__":
    # asyncio.run(main=main1())
    # asyncio.run(main=main2())
    asyncio.run(main=main3())
