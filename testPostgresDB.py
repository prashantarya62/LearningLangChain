# from psycopg2 import pool
# import psycopg2.extensions

# # Create connection pool with keepalive
# connection_pool = pool.ThreadedConnectionPool(
#     minconn=5,
#     maxconn=20,
#     host='192.168.19.26',
#     port=5432,
#     database='ssct_251120',
#     user='postgres',
#     password='password',
#     keepalives=1,
#     keepalives_idle=60,
#     keepalives_interval=10,
#     keepalives_count=6,
#     connect_timeout=10
# )

# # Get connection with validation
# def get_db_connection():
#     try:
#         conn = connection_pool.getconn()
#         # Test connection before returning
#         conn.isolation_level
#         return conn
#     except psycopg2.OperationalError:
#         # Connection is dead, get a new one
#         connection_pool.putconn(conn, close=True)
#         return connection_pool.getconn()

# # Always return connection to pool
# def release_connection(conn):
#     connection_pool.putconn(conn)



import psycopg2
import schedule
import time

def check_db_connection():
    try:
        conn = psycopg2.connect(
            host='192.168.19.26',
            port=5432,
            database='ssct_251120',
            user='postgres',
            password='password',
            connect_timeout=5
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        conn.close()
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - DB connection OK")
    except Exception as e:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - DB connection FAILED: {e}")
        # Send alert/notification here

# Run health check every 30 seconds
schedule.every(30).seconds.do(check_db_connection)

while True:
    schedule.run_pending()
    time.sleep(1)