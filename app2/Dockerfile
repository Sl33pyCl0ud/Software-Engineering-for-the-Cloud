# Use an official Python runtime as a parent image
FROM python:3.11.5

# Set the working directory to /app
WORKDIR /app2

# Copy the current directory contents into the container at /app
COPY . /app2

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org flask flask_sqlalchemy

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app2.py when the container launches
CMD ["python", "app2.py"]

