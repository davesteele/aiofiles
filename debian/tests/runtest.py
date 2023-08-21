#!/usr/bin/python3

import asyncio
import aiofiles

async def test_aiofiles():
    async with aiofiles.open('README.md', 'r') as fp:
        contents = await fp.read()

    assert('aiofiles' in contents)

asyncio.run(test_aiofiles())
