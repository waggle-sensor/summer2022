# A Dockerfile is used to define how your code will be packaged. This includes
# your code, the base image and any additional dependencies you need.
FROM waggle/plugin-base:1.1.1-base

WORKDIR /app

# Now we include the Python requirements.txt file and install any missing dependencies.
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Next, we add our code.
COPY main.py .

# Finally, we specify the "main" thing that should be run.
ENTRYPOINT [ "python3", "main.py" ]
