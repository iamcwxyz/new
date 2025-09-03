
"""
MySQL Database Configuration for Local Development with XAMPP
"""
import mysql.connector
from mysql.connector import Error
import os

# MySQL Configuration
MYSQL_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',  # Default XAMPP MySQL user
    'password': '',  # Default XAMPP MySQL password (empty)
    'database': 'payroll_system',
    'charset': 'utf8mb4',
    'autocommit': True
}

def get_mysql_connection():
    """Get MySQL database connection for XAMPP"""
    try:
        connection = mysql.connector.connect(**MYSQL_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def test_mysql_connection():
    """Test MySQL connection"""
    conn = get_mysql_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        print("✅ MySQL connection successful!")
        return True
    else:
        print("❌ MySQL connection failed!")
        return False

def create_mysql_database():
    """Create MySQL database if it doesn't exist"""
    try:
        # Connect without specifying database
        config_no_db = MYSQL_CONFIG.copy()
        del config_no_db['database']
        
        connection = mysql.connector.connect(**config_no_db)
        cursor = connection.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS payroll_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print("✅ Database 'payroll_system' created/verified")
        
        cursor.close()
        connection.close()
        return True
        
    except Error as e:
        print(f"Error creating database: {e}")
        return False

if __name__ == "__main__":
    print("Testing MySQL connection for XAMPP...")
    create_mysql_database()
    test_mysql_connection()
