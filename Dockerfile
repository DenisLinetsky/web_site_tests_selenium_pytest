# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y wget unzip && \
    apt-get install -y chromium-driver && \
    apt-get install -y chromium

# Set the working directory in the container
WORKDIR /tests

# Copy the current directory contents into the container at /tests
ADD . /tests

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the command to start testing
CMD ["pytest", "tests/test_verify_test_case_page.py"]



