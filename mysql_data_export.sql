-- MySQL Export from Replit SQLite Database
-- Generated on: 2025-08-26 14:14:33.351425
-- Run this script in phpMyAdmin after creating the database using payroll.sql

SET FOREIGN_KEY_CHECKS = 0;

-- Insert employees
INSERT INTO employees (id, employee_id, username, password, name, department, position, salary_rate, role, status, profile_picture, nfc_id, qr_code_path, phone) VALUES (1, 'EMP001', 'admin', '$2b$12$QYFy8DznYMAGvaM81l0mg.baX2mX/Krnwkbszl6Ru6Hrl/PnCfNju', 'System Administrator', 'IT', 'Administrator', 0.0, 'Admin', 'Active', '20250825_050046_FEN_DWG_.jpg', NULL, NULL, NULL);
INSERT INTO employees (id, employee_id, username, password, name, department, position, salary_rate, role, status, profile_picture, nfc_id, qr_code_path, phone) VALUES (2, 'EMP002', 'majjoy', '$2b$12$KZwo2ueh34qCySSsfS3fH.RKPPUk2pP1nngfbDJsixweQ7lNhgfTO', 'Marie Joy De Guzman', 'Operations Department', 'Procurement', 580.0, 'Employee', 'Active', '', NULL, NULL, '0987654321');
INSERT INTO employees (id, employee_id, username, password, name, department, position, salary_rate, role, status, profile_picture, nfc_id, qr_code_path, phone) VALUES (3, 'EMP003', 'hr1', '$2b$12$2O74Pz86KvUP3pqxxzl3HOfG6RLbFzk1kxoMlfyQxhi2zJW832bdG', 'hr1', 'HR', 'Recruitment and Staffing', 700.0, 'HR', 'Active', '20250825_045151_Have_a_Nice_Day_icecube_.jpg', NULL, NULL, NULL);
INSERT INTO employees (id, employee_id, username, password, name, department, position, salary_rate, role, status, profile_picture, nfc_id, qr_code_path, phone) VALUES (4, 'EMP004', 'elrondgalut', '$2b$12$lDhlGZw33pP/3RInVW5EyeYXVYogsLnytGJG97vBqRavQHnJMcMhu', 'John Elrond Galut', 'Operations Department', 'Operations Manager', 450.0, 'Employee', 'Active', '20250825_055218_Icon___.jpg', NULL, NULL, NULL);
INSERT INTO employees (id, employee_id, username, password, name, department, position, salary_rate, role, status, profile_picture, nfc_id, qr_code_path, phone) VALUES (5, 'EMP005', 'kristel', '$2b$12$CzFz.uzL9XsgOrNuaSDcI.WNlTGJi7gvzPl0HaXpx0sSSW9b9ms0S', 'Kristel Joy Tejada', 'Security', 'Security Guard ni Jalah', 1000.0, 'Employee', 'Active', '20250825_062716_Sunflower.jpg', NULL, NULL, NULL);
INSERT INTO employees (id, employee_id, username, password, name, department, position, salary_rate, role, status, profile_picture, nfc_id, qr_code_path, phone) VALUES (6, 'EMP006', 'dj', '$2b$12$kJHVP73lx9wRRZDFXcm/9.PhfhzjfR3JLIpeyNzaH9bIbb9CXRiMC', 'Dee Jay Cristobal', 'IT Department', 'Web Developer', 800.0, 'Employee', 'Active', '20250826_120352_hey_Guys_go_go_go___1.jpg', '', NULL, '+639363822159');

-- Insert attendance
INSERT INTO attendance (id, employee_id, date, time_in, time_out) VALUES (1, 3, '2025-08-25', '04:58:39', '06:48:01');
INSERT INTO attendance (id, employee_id, date, time_in, time_out) VALUES (2, 1, '2025-08-25', '04:58:53', NULL);
INSERT INTO attendance (id, employee_id, date, time_in, time_out) VALUES (3, 4, '2025-08-25', '08:15:39', NULL);
INSERT INTO attendance (id, employee_id, date, time_in, time_out) VALUES (4, 3, '2025-08-26', '09:09:41', '09:18:54');
INSERT INTO attendance (id, employee_id, date, time_in, time_out) VALUES (5, 2, '2025-08-26', '09:19:17', '09:19:30');
INSERT INTO attendance (id, employee_id, date, time_in, time_out) VALUES (6, 1, '2025-08-26', '09:19:37', NULL);
INSERT INTO attendance (id, employee_id, date, time_in, time_out) VALUES (7, 4, '2025-08-26', '09:19:46', '09:20:00');
INSERT INTO attendance (id, employee_id, date, time_in, time_out) VALUES (8, 6, '2025-08-26', '13:39:28', NULL);

-- Insert leaves
INSERT INTO leaves (id, employee_id, leave_type, duration, start_date, end_date, reason, status) VALUES (1, 2, 'Sick', 'Full', '2025-08-25', '2025-08-30', 'Sick Leave Nganiiiii', 'Approved');
INSERT INTO leaves (id, employee_id, leave_type, duration, start_date, end_date, reason, status) VALUES (2, 4, 'Vacation', 'Full', '2025-09-06', '2027-01-07', 'Magbabakasyon po ako ng one year sa Japan! pero dapat may pay parin!!!!!!!!', 'Rejected');
INSERT INTO leaves (id, employee_id, leave_type, duration, start_date, end_date, reason, status) VALUES (3, 5, 'Personal', 'Full', '2025-08-25', '2027-08-25', 'Mag aasawa lang po ako ng AFAM! Para may malaki akong kapalaran! 
Bahala na kayo jan sa Company niyo, balik din ako!  Pero dapat may Leave pay parin ako ah! Thankies!', 'Approved');

-- Insert applications
INSERT INTO applications (id, application_id, full_name, email, phone, address, position_applied, resume_file, work_experience, education, skills, status, applied_date, processed_by, processed_date, notes) VALUES (1, 'APP0001', 'John Elrond Galut', 'galutelrond@gmail.com', '0987654321', 'Basta', 'Operations Manager', 'APP0001_DEE_JAY_CRISTOBAL_Resume.docx', 'Wala', 'wala', 'awla', 'Approved', '2025-08-25 05:31:58', 1, '2025-08-25 05:53:00', 'approved ka na pre pwede mo na akong mahalin! hahahahcharo lang! Start ka na bukas!

ito username and password mo re!

elrondgalut
13572468');
INSERT INTO applications (id, application_id, full_name, email, phone, address, position_applied, resume_file, work_experience, education, skills, status, applied_date, processed_by, processed_date, notes) VALUES (2, 'APP0002', 'basta applicant!', 'basta@email.com', '09876543212', 'ugedgywdcqvdw qwd gevgqdyvg8qt7ev', 'IT Specialist', 'APP0002_reco.pdf', 'gntggn', 'fgjjkgr', 'fgmtkrgn', 'In Review', '2025-08-26 12:31:21', 3, '2025-08-26 12:32:51', 'wag ka na magapply! Hinayupak ka!');

-- Insert settings
INSERT INTO settings (id, setting_name, setting_value, description, updated_by, updated_at) VALUES (1, 'office_hours_per_day', '8', 'Standard daily work hours for payroll calculation', 3, '2025-08-25 06:04:15');
INSERT INTO settings (id, setting_name, setting_value, description, updated_by, updated_at) VALUES (2, 'overtime_multiplier', '1.5', 'Overtime pay multiplier (e.g., 1.5 = time and a half)', 3, '2025-08-25 06:04:15');
INSERT INTO settings (id, setting_name, setting_value, description, updated_by, updated_at) VALUES (3, 'tax_rate', '0.12', 'Standard tax deduction rate', 3, '2025-08-25 06:04:15');
INSERT INTO settings (id, setting_name, setting_value, description, updated_by, updated_at) VALUES (4, 'insurance_deduction', '500', 'Monthly insurance deduction amount', 3, '2025-08-25 06:04:15');
INSERT INTO settings (id, setting_name, setting_value, description, updated_by, updated_at) VALUES (5, 'company_name', 'Federal Agency', 'Company name for reports and documents', 3, '2025-08-25 06:04:15');
INSERT INTO settings (id, setting_name, setting_value, description, updated_by, updated_at) VALUES (6, 'payroll_period', 'biweekly', 'Payroll generation period (monthly/biweekly)', 3, '2025-08-25 06:04:15');
INSERT INTO settings (id, setting_name, setting_value, description, updated_by, updated_at) VALUES (7, 'system_logo', 'logo_20250825_060415__d259b265-9fd9-4ea0-8991-efe44b4dca55.jpg', 'System logo image file', 3, '2025-08-25 06:04:15');

SET FOREIGN_KEY_CHECKS = 1;
-- End of export