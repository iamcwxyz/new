import sqlite3
import mysql.connector
from mysql.connector import Error
from config_mysql import get_mysql_connection

def migrate_employees(sqlite_cursor, mysql_conn):
    """Migrate employees table"""
    sqlite_cursor.execute("SELECT id, name, email, position, salary, created_at FROM employees")
    rows = sqlite_cursor.fetchall()

    cursor = mysql_conn.cursor()
    for row in rows:
        try:
            cursor.execute("""
                INSERT INTO employees (id, name, email, position, salary, created_at)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE 
                    name=VALUES(name), 
                    email=VALUES(email),
                    position=VALUES(position),
                    salary=VALUES(salary)
            """, row)
        except Error as e:
            print(f"⚠️ Error migrating employee {row[0]}: {e}")

    mysql_conn.commit()
    cursor.close()
    print(f"✅ Migrated {len(rows)} employees")

def migrate_attendance(sqlite_cursor, mysql_conn):
    """Migrate attendance table"""
    sqlite_cursor.execute("SELECT id, employee_id, time_in, time_out FROM attendance")
    rows = sqlite_cursor.fetchall()

    cursor = mysql_conn.cursor()
    for row in rows:
        try:
            cursor.execute("""
                INSERT INTO attendance (id, employee_id, time_in, time_out)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE 
                    time_in=VALUES(time_in),
                    time_out=VALUES(time_out)
            """, row)
        except Error as e:
            print(f"⚠️ Error migrating attendance {row[0]}: {e}")

    mysql_conn.commit()
    cursor.close()
    print(f"✅ Migrated {len(rows)} attendance records")

def migrate_sqlite_to_mysql():
    # Connect to SQLite
    sqlite_conn = sqlite3.connect("payroll_system.db")
    sqlite_cursor = sqlite_conn.cursor()

    # Connect to MySQL
    mysql_conn = get_mysql_connection()
    if not mysql_conn:
        print("❌ Cannot connect to MySQL. Migration aborted.")
        return

    migrate_employees(sqlite_cursor, mysql_conn)
    migrate_attendance(sqlite_cursor, mysql_conn)

    # Close connections
    sqlite_cursor.close()
    sqlite_conn.close()
    mysql_conn.close()
    print("🎉 Migration completed successfully!")

if __name__ == "__main__":
    migrate_sqlite_to_mysql()
