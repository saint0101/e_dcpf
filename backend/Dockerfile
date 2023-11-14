# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

RUN git clone -b testprod https://github.com/saint0101/e_dcpf.git

# Copy the current directory contents into the container at /app
COPY . /app

WORKDIR /app/e_dcpf/backend

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app/e_dcpf/backend/app/

RUN ls .

# Run app.py when the container launches
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
