FROM python:3.10-buster

# Create workspace directory
RUN mkdir -p /workspace && \
    chmod 777 /workspace

# Copy requirements file from workspace root
COPY requirements.txt /requirements.txt

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

WORKDIR /workspace