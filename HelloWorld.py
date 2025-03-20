from smartspace.core import Block, step, Output, State

from typing import Annotated, Any


class HelloWorld(Block):
    message: Output[str]
    count: Annotated[int, State()] = 0

    @step()
    async def run(self, run: Any):
        self.count += 1
        self.message.send("Hello World" + "!" * self.count)