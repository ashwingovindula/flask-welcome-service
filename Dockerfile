# Step 1: Use a lightweight Python image
FROM python:3.9-slim

# Step 2: Set working directory in container
WORKDIR /app

# Step 3: Copy local code to container
COPY . .

# Step 4: Install dependencies
RUN pip install -r requirements.txt

# Step 5: Define default command to run the app
CMD ["python", "app.py"]
