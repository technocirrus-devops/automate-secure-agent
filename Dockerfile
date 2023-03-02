# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /secure-agent-app
WORKDIR /secure-agent-app

# Copy the current directory contents into the container at /secure-agent-app
COPY . /secure-agent-app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Give execute permissions to the secureagent.sh script
RUN chmod a+x secureagent.sh

# Run the secureagent.sh script
CMD ["./secureagent.sh"]
