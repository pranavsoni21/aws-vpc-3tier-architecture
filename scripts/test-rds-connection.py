import pymysql
import sys

def test_connection(host, user, password, database):
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("✓ Successfully connected to RDS!")
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"✓ MySQL version: {version[0]}")
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python3 test-rds-connection.py <host> <user> <password> <database>")
        sys.exit(1)
    
    test_connection(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])