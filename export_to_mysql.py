
#!/usr/bin/env python3
"""
Export SQLite database to MySQL format for phpMyAdmin/XAMPP
"""
import sqlite3
import json
from datetime import datetime

def export_sqlite_to_mysql():
    """Export current SQLite data to MySQL INSERT statements"""
    
    # Connect to SQLite database
    conn = sqlite3.connect('payroll_system.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    mysql_script = []
    mysql_script.append("-- MySQL Export from Replit SQLite Database")
    mysql_script.append(f"-- Generated on: {datetime.now()}")
    mysql_script.append("-- Run this script in phpMyAdmin after creating the database using payroll.sql")
    mysql_script.append("")
    mysql_script.append("SET FOREIGN_KEY_CHECKS = 0;")
    mysql_script.append("")
    
    # Export employees
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    if employees:
        mysql_script.append("-- Insert employees")
        for emp in employees:
            values = []
            for col in emp.keys():
                value = emp[col]
                if value is None:
                    values.append("NULL")
                elif isinstance(value, str):
                    # Escape single quotes
                    escaped_value = value.replace("'", "''")
                    values.append(f"'{escaped_value}'")
                else:
                    values.append(str(value))
            
            columns = ", ".join(emp.keys())
            values_str = ", ".join(values)
            mysql_script.append(f"INSERT INTO employees ({columns}) VALUES ({values_str});")
        mysql_script.append("")
    
    # Export attendance
    cursor.execute("SELECT * FROM attendance")
    attendance = cursor.fetchall()
    if attendance:
        mysql_script.append("-- Insert attendance")
        for att in attendance:
            values = []
            for col in att.keys():
                value = att[col]
                if value is None:
                    values.append("NULL")
                elif isinstance(value, str):
                    escaped_value = value.replace("'", "''")
                    values.append(f"'{escaped_value}'")
                else:
                    values.append(str(value))
            
            columns = ", ".join(att.keys())
            values_str = ", ".join(values)
            # Map employee_ref to employee_id for MySQL
            mysql_script.append(f"INSERT INTO attendance ({columns.replace('employee_ref', 'employee_id')}) VALUES ({values_str});")
        mysql_script.append("")
    
    # Export leaves
    cursor.execute("SELECT * FROM leaves")
    leaves = cursor.fetchall()
    if leaves:
        mysql_script.append("-- Insert leaves")
        for leave in leaves:
            values = []
            for col in leave.keys():
                value = leave[col]
                if value is None:
                    values.append("NULL")
                elif isinstance(value, str):
                    escaped_value = value.replace("'", "''")
                    values.append(f"'{escaped_value}'")
                else:
                    values.append(str(value))
            
            columns = ", ".join(leave.keys())
            values_str = ", ".join(values)
            # Map employee_ref to employee_id and type to leave_type for MySQL
            columns = columns.replace('employee_ref', 'employee_id').replace('type', 'leave_type')
            mysql_script.append(f"INSERT INTO leaves ({columns}) VALUES ({values_str});")
        mysql_script.append("")
    
    # Export applications
    cursor.execute("SELECT * FROM applications")
    applications = cursor.fetchall()
    if applications:
        mysql_script.append("-- Insert applications")
        for app in applications:
            values = []
            for col in app.keys():
                value = app[col]
                if value is None:
                    values.append("NULL")
                elif isinstance(value, str):
                    escaped_value = value.replace("'", "''")
                    values.append(f"'{escaped_value}'")
                else:
                    values.append(str(value))
            
            columns = ", ".join(app.keys())
            values_str = ", ".join(values)
            mysql_script.append(f"INSERT INTO applications ({columns}) VALUES ({values_str});")
        mysql_script.append("")
    
    # Export settings
    cursor.execute("SELECT * FROM settings")
    settings = cursor.fetchall()
    if settings:
        mysql_script.append("-- Insert settings")
        for setting in settings:
            values = []
            for col in setting.keys():
                value = setting[col]
                if value is None:
                    values.append("NULL")
                elif isinstance(value, str):
                    escaped_value = value.replace("'", "''")
                    values.append(f"'{escaped_value}'")
                else:
                    values.append(str(value))
            
            columns = ", ".join(setting.keys())
            values_str = ", ".join(values)
            mysql_script.append(f"INSERT INTO settings ({columns}) VALUES ({values_str});")
        mysql_script.append("")
    
    mysql_script.append("SET FOREIGN_KEY_CHECKS = 1;")
    mysql_script.append("-- End of export")
    
    # Write to file
    with open('mysql_data_export.sql', 'w', encoding='utf-8') as f:
        f.write('\n'.join(mysql_script))
    
    conn.close()
    print("✅ MySQL export created: mysql_data_export.sql")
    print("📋 Steps to import:")
    print("1. Start XAMPP and open phpMyAdmin")
    print("2. Create a new database called 'payroll_system'")
    print("3. Import the payroll.sql file first (creates tables)")
    print("4. Then import mysql_data_export.sql (inserts data)")

if __name__ == "__main__":
    export_sqlite_to_mysql()
