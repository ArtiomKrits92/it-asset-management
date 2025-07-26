# Use Ubuntu as base image
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-flask \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /var/www/it-asset-management

# Copy website files from the correct path
COPY website/ ./

# Install Flask using pip (backup)
RUN pip3 install flask

# Expose port 31415 web access
EXPOSE 31415

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run when container starts
CMD ["python3", "-m", "flask", "run", "--port=31415"]