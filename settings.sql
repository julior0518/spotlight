-- settings.sql
CREATE DATABASE spotlight;
CREATE USER spotlight_user WITH PASSWORD 'spot';
GRANT ALL PRIVILEGES ON DATABASE spotlight TO spotlight_user;