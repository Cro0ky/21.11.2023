import asyncio
import httpx


async def download(current):
    url = f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail'

    async with httpx.AsyncClient() as client:
        result = await client.get(url)
        if result.status_code == 200:
            my_res = result.json()
            print_info(my_res['drinks'], current)
        else:
            print(result.status_code)
        print(f'Result №{current}')


def print_info(info, current):
    # print(f'Name {info["first_name"]} lastname {info["last_name"]}, E-mail {info["email"]}')
    print(info[current]['strDrinks'])


async def main():
    users_count = int(input('How many peoples? '))
    current = 0
    task_list = []
    while current < users_count:
        
        task = asyncio.create_task(download(current))
        task_list.append(task)
        current += 1
    await asyncio.gather(*task_list)
    print('Done')


asyncio.run(main())
