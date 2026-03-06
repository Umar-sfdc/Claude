import random
from fastmcp import FastMCP

# Create a fastmcp server instance.

mcp = FastMCP(name="Demo Server")

@mcp.tool
def roll_dice(n_dice:int=1) -> list[int] : 
    """Roll n_dic 6 Sided-dice and return the result"""
    return [random.randint(1,6) for _in range(n_dice)]


@mcp.tool
def add_numbers(a:float=0, b:float=0) -> float : 
    """Add two numbers togather"""
    return a + b

if __name__ == "__main__":
    mcp.run()