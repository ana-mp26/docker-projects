# Use an official PHP image with the built-in web server as a parent image
FROM php:latest

# Set the working directory
WORKDIR /var/www/html

# Copy PHP files to the working directory
COPY . .

# Command to run the PHP built-in web server
CMD ["php", "-S", "0.0.0.0:80"]
