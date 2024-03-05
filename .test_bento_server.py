import aiohttp
import asyncio
import sys


async def sample_request(server_url="http://localhost:3000"):
    url = f"{server_url}/classify"
    payload = {"input_series": [[1, 1, 1, 1]]}

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url,
            json=payload,
            headers={"accept": "application/json", "Content-Type": "application/json"},
        ) as response:
            assert response.status == 200, response.status
            result = await response.json()
            assert result == [0], result


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if len(sys.argv) > 1:
        loop.run_until_complete(sample_request(sys.argv[1]))
    else:
        loop.run_until_complete(sample_request())
