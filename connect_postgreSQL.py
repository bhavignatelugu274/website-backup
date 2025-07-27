import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="bhavi",
    host="localhost",  # or your server IP
    port="5432"         # default PostgreSQL port
)

# Create a cursor
cur = conn.cursor()

# Example: Create a table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100)
    )
""")

# Example: Insert data
cur.execute("""
    INSERT INTO users (name, email) VALUES (%s, %s)
""", ("Alice", "alice@example.com"))

# Commit the transaction
conn.commit()

# Example: Fetch data
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close connection
cur.close()
conn.close()
