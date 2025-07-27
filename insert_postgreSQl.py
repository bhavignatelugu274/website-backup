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

#cur.execute("""
 # INSERT INTO users (user_id, full_name,email,password,phone,registration_date) VALUES (%d,%s,%c,%d,%d,%d) """, ("1","Alice", "alice@example.com","alice","1234","123456","2025-07-18"))

cur.execute("INSERT INTO registration_form (user_id, full_name,email,password,phone,registration_date) VALUES ('3','venkat','venkat@example.com','venku','1234567890','18-07-2025')")


# Commit the transaction
conn.commit()

# Close connection
cur.close()
conn.close()
