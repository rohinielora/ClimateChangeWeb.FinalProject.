def fetch_data(conn, column):
    cursor = conn.cursor()
    query = f"SELECT date, {column} FROM climate_data ORDER BY date"
    cursor.execute(query)
    return cursor.fetchall()
