
"""
Database Adapter - Works with both SQLite (Replit) and MySQL (Local XAMPP)
"""
import os
import sqlite3
from contextlib import contextmanager

# Check environment to determine database type
USE_MYSQL = os.environ.get('USE_MYSQL', 'false').lower() == 'true'

if USE_MYSQL:
    try:
        import mysql.connector
        from config_mysql import get_mysql_connection, MYSQL_CONFIG
        print("📊 Using MySQL database (XAMPP)")
    except ImportError:
        print("⚠️ MySQL connector not found, falling back to SQLite")
        USE_MYSQL = False

if not USE_MYSQL:
    from database import get_db_connection as get_sqlite_connection
    print("📊 Using SQLite database (Replit)")

class DatabaseAdapter:
    """Database adapter that works with both SQLite and MySQL"""
    
    @staticmethod
    @contextmanager
    def get_connection():
        """Get database connection with context manager"""
        if USE_MYSQL:
            conn = get_mysql_connection()
            if conn is None:
                raise Exception("Failed to connect to MySQL database")
            try:
                yield conn
            finally:
                if conn.is_connected():
                    conn.close()
        else:
            conn = get_sqlite_connection()
            try:
                yield conn
            finally:
                conn.close()
    
    @staticmethod
    def execute_query(query, params=None, fetch_one=False, fetch_all=False):
        """Execute a query and return results"""
        with DatabaseAdapter.get_connection() as conn:
            if USE_MYSQL:
                cursor = conn.cursor(dictionary=True)
                cursor.execute(query, params or ())
                
                if fetch_one:
                    result = cursor.fetchone()
                elif fetch_all:
                    result = cursor.fetchall()
                else:
                    result = cursor.rowcount
                
                cursor.close()
                return result
            else:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(query, params or ())
                
                if fetch_one:
                    result = cursor.fetchone()
                elif fetch_all:
                    result = cursor.fetchall()
                else:
                    result = cursor.rowcount
                    conn.commit()
                
                return result
    
    @staticmethod
    def get_last_insert_id(conn, cursor):
        """Get last inserted ID (handles difference between SQLite and MySQL)"""
        if USE_MYSQL:
            return cursor.lastrowid
        else:
            return cursor.lastrowid

# Example usage functions
def get_all_employees():
    """Get all employees using the adapter"""
    query = "SELECT * FROM employees WHERE status = 'Active' ORDER BY name"
    return DatabaseAdapter.execute_query(query, fetch_all=True)

def get_employee_by_id(employee_id):
    """Get employee by ID using the adapter"""
    query = "SELECT * FROM employees WHERE employee_id = %s" if USE_MYSQL else "SELECT * FROM employees WHERE employee_id = ?"
    return DatabaseAdapter.execute_query(query, (employee_id,), fetch_one=True)

def create_employee(employee_data):
    """Create new employee using the adapter"""
    if USE_MYSQL:
        query = """INSERT INTO employees (employee_id, username, password, name, phone, department, position, salary_rate, role, status)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    else:
        query = """INSERT INTO employees (employee_id, username, password, name, phone, department, position, salary_rate, role, status)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    
    return DatabaseAdapter.execute_query(query, employee_data)
