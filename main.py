from fastmcp import FastMCP
mcp = FastMCP()

# write a function and register it as a mcp tool using the @mcp.tool() decorator
@mcp.tool()
def say_hello(name: str):
    '''
    NOTE: write the description of the tool here. A good description should include input and output specifications.
    
    Example of a good description:

    --------------------------------
    This tool is used to say hello to a person.
    
    Input:
    - name: str

    Output:
    - result: str
    '''
    
    return f"Hello {name}!"

def main():
    # test the functionality of the tool before deploying it
    print(say_hello("Peter"))

if __name__ == "__main__":
    main()