import asyncio


async def async_func(num):
    print(f'start {num}...')
    await asyncio.sleep(3)
    print(f'{num} finish!')


async def main():
    task_a = asyncio.create_task(async_func('A'))
    task_b = asyncio.create_task(async_func('B'))
    task_c = asyncio.create_task(async_func('C'))
    await asyncio.wait([task_a, task_b, task_c])


if __name__ == '__main__':
    asyncio.run(main())
