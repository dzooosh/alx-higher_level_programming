-- converts hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0
ALTER TABLE first_table 
ALTER TABLE first_table MODIFY `name` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
