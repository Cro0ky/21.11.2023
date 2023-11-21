import asyncio
import time


async def call():
    print('начался звонок')
    await asyncio.sleep(2)
    print('Звонок закончился ')


async def prin_pos():
    print('пришел посетитель')
    await asyncio.sleep(2)
    print('Посетитель ушел ')


async def grafiks():
    print('начало работы с графиками')
    await asyncio.sleep(2)
    print('Графики сделаны')


async def aeroticket():
    print('Выбор авиабилетов')
    await asyncio.sleep(5)
    print('Покупка авиабилетов ')


async def documents():
    print('начался заполнения')
    await asyncio.sleep(3)
    print('Документы заполнены')


async def main():

    print('9:00')
    await prin_pos()
    print('10:00')
    await asyncio.gather(aeroticket(), documents())
    print('11:00')
    await call()
    print('12:00')
    await grafiks()
    print('13:00')
    await asyncio.gather(aeroticket(), documents())

asyncio.run(main())



