import asyncio
import time


async def make_coffee():
    print('start make coffee')
    await asyncio.sleep(3)
    print('finish make coffee')
    return 'coffee is ready'


async def toast_brew():
    print('start toast brew')
    await asyncio.sleep(2)
    print('finish toast brew')
    return 'toast is ready'


async def main():
    start = time.time()
    work = asyncio.gather(make_coffee(), toast_brew())
    res_coffee, res_toast = await work
    end = time.time()
    print(f'Времени прошло {end - start:.2f} минуты')
    print(res_coffee, res_toast)


if __name__ == '__main__':
    asyncio.run(main())
