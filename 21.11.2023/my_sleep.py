import asyncio


async def my_sleep():
    print('sleep start')
    await asyncio.sleep(3)
    print('sleep end')

async def work():
    print('work start')
    await asyncio.sleep(5)
    print('work end')


async def main():
    task1 = asyncio.create_task(my_sleep())

    print('rest start')
    await task1
    print('rest end')

    task2 = asyncio.create_task(work())
    await task2


asyncio.run(main())
