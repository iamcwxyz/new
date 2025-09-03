
# Setup Instructions for Visual Studio Code + XAMPP

## Prerequisites
1. **Visual Studio Code** - Download from https://code.visualstudio.com/
2. **XAMPP** - Download from https://www.apachefriends.org/

## Step 1: Download Project from Replit

1. In Replit, click on your username (top-right) → **My Repls**
2. Find your payroll project and click the **⋮** menu
3. Select **Download as zip**
4. Extract the zip file to your desired folder (e.g., `C:\Projects\payroll-system`)

## Step 2: Setup XAMPP and MySQL

1. **Install and Start XAMPP**:
   - Install XAMPP
   - Open XAMPP Control Panel
   - Start **Apache** and **MySQL** services

2. **Create Database**:
   - Open browser and go to `http://localhost/phpmyadmin`
   - Click **New** on the left sidebar
   - Database name: `payroll_system`
   - Collation: `utf8mb4_unicode_ci`
   - Click **Create**

3. **Import Database Structure**:
   - Select the `payroll_system` database
   - Click **Import** tab
   - Choose file: `payroll.sql` (from your project folder)
   - Click **Go**

## Step 3: Export Data from Replit (Run this in Replit)

1. In your Replit project, run:
   ```bash
   python export_to_mysql.py
   ```
2. Download the generated `mysql_data_export.sql` file
3. In phpMyAdmin, import this file to insert your existing data

## Step 4: Setup Visual Studio Code

1. **Open Project**:
   - Open Visual Studio Code
   - File → Open Folder → Select your extracted project folder

2. **Install Python Extension**:
   - Go to Extensions (Ctrl+Shift+X)
   - Search and install "Python" by Microsoft

3. **Install Python Dependencies**:
   - Open terminal in VS Code (Terminal → New Terminal)
   - Run:
     ```bash
     pip install flask flask-wtf bcrypt email-validator openpyxl werkzeug cryptography flask-limiter bleach qrcode pillow mysql-connector-python
     ```

## Step 5: Configure for Local Development

1. **Set Environment Variable for MySQL**:
   - Create a file named `.env` in your project root:
     ```
     USE_MYSQL=true
     SESSION_SECRET=your-secret-key-here
     ```

2. **Test MySQL Connection**:
   ```bash
   python config_mysql.py
   ```

3. **Update app.py** (if needed):
   - Change the import from `database` to `database_adapter`
   - Update any database calls to use the adapter

## Step 6: Run the Application

1. **Start the Flask App**:
   ```bash
   python app.py
   ```

2. **Access the Application**:
   - Open browser and go to `http://localhost:5000`

## Troubleshooting

### MySQL Connection Issues:
- Ensure XAMPP MySQL is running
- Check if port 3306 is available
- Verify database name is `payroll_system`

### Python Package Issues:
- Try: `pip install --upgrade pip`
- Install packages one by one if needed

### File Upload Issues:
- Ensure `static/uploads` folder exists and has write permissions

## Development Workflow

1. **Code in VS Code** with full IntelliSense and debugging
2. **Database Management** through phpMyAdmin
3. **File Management** through Windows Explorer
4. **Version Control** can be set up with Git

## Switching Between Environments

- **Local (XAMPP)**: Set `USE_MYSQL=true` in `.env`
- **Replit**: Don't set the environment variable (defaults to SQLite)

This setup gives you the best of both worlds:
- Full-featured local development with VS Code
- Professional database management with phpMyAdmin
- Easy deployment back to Replit when needed
