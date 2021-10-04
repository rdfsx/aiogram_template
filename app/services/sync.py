import asyncio
from collections.abc import Callable
from functools import wraps, partial
from typing import Any, Awaitable


def run_sync(func: Callable[..., Any]):

    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any):
        return await asyncio.get_running_loop().run_in_executor(
            None, partial(func, *args, **kwargs)
        )

    return wrapper
