from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI

app = FastAPI()

# Database configuration
MONGO_DETAILS = "mongodb://localhost:27017"  # Adjust as necessary

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.library
