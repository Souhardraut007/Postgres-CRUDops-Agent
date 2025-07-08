# tools/postgres_tools.py

import psycopg2
from langchain_core.tools import tool

# ✅ UPDATE these credentials with your PostgreSQL DB login
try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="persondb",
        user="postgres",       # <-- change this
        password="Ssr@172526"    # <-- and this
    )
    cursor = conn.cursor()
    print("✅ Connected to PostgreSQL")
except Exception as e:
    print("❌ Database connection failed:", e)


@tool
def create_user(name: str, email: str) -> str:
    """Create a new user in the users table with name and email."""
    print(f"📥 create_user: {name}, {email}")
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        return "✅ User created successfully"
    except Exception as e:
        conn.rollback()
        return f"❌ Error: {str(e)}"


@tool
def read_users() -> list:
    """Read all users from the users table."""
    print("📥 read_users")
    try:
        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()
        return [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]
    except Exception as e:
        conn.rollback()
        return [f"❌ Error: {str(e)}"]


@tool
def update_user_email(user_id: int, new_email: str) -> str:
    """Update a user's email using their ID."""
    print(f"📥 update_user_email: ID={user_id}, email={new_email}")
    try:
        cursor.execute("UPDATE users SET email = %s WHERE id = %s", (new_email, user_id))
        conn.commit()
        return "✅ User email updated successfully"
    except Exception as e:
        conn.rollback()
        return f"❌ Error: {str(e)}"


@tool
def delete_user(user_id: int) -> str:
    """Delete a user from the users table by ID."""
    print(f"📥 delete_user: ID={user_id}")
    try:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        return "✅ User deleted successfully"
    except Exception as e:
        conn.rollback()
        return f"❌ Error: {str(e)}"
