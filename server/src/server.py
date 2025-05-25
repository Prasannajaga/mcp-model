from typing import Any
import psycopg2
from mcp.server.fastmcp import FastMCP
import json

# Initialize FastMCP server
mcp = FastMCP("postgres_server") 


@mcp.tool()
def query_data(query: str):
    """
    Query data from the database.
    """
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="db_movies",
        user="postgres",
        password="Prasa123",
        host="localhost",
        port="5500"
    )
    
    cursor = conn.cursor()
    
    # Execute a sample query
    cursor.execute(query=query)
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Close the connection
    cursor.close()
    conn.close()
    
    return json.dumps(results)


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
