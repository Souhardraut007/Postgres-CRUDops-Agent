# Postgres CRUD Agent with MCP + Streamlit

This project is a simple but powerful agent-based backend and frontend system built using:

- LangChain tool interface (MCP-style)
- PostgreSQL for database storage
- FastAPI (with `uvicorn`) as a lightweight tool server
- Streamlit for a user-friendly frontend interface

It performs full **CRUD operations** (Create, Read, Update, Delete) on a `users` table in a PostgreSQL database using a dynamic tool-based structure — perfect for building LLM-integrated backend systems or teaching yourself database automation.


## Features

- LangChain-style `@tool` functions for modular database operations
- Implements a simplified **MCP (Model Context Protocol)** agent
- Full CRUD support:
  - Create user
  - Read all users
  - Update user email
  - Delete user
  - Backend tools served via FastAPI
  - Clean and functional Streamlit UI for quick interactions



## Technologies Used

- **Python 3.9+**
- **PostgreSQL**
- **psycopg2** – to connect to the DB
- **LangChain Core**
- **FastAPI**
- **Streamlit**
- 
