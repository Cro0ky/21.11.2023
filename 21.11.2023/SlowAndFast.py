import time
import asyncio


async def fast(a, b):
    await asyncio.sleep(1)
    print(a + b)


async def slow(a, b):
    await asyncio.sleep(5)
    print(a * b)


async def main():
    start = time.time()
    task_list = [fast(2, 3), slow(3, 4)]
    await asyncio.gather(*task_list)
    end = time.time()
    print(f'{end-start:.2f}')


if __name__ == '__main__':
    asyncio.run(main())
