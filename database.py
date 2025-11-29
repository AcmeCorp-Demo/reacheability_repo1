"""
Database operations module with MongoDB and SQLAlchemy support.
"""

from typing import List, Dict, Any, Optional
import logging
from pymongo import MongoClient
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from config import Config

logger = logging.getLogger(__name__)

Base = declarative_base()


class User(Base):
    """SQLAlchemy User model."""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"


class DatabaseManager:
    """Manage database connections and operations."""
    
    def __init__(self):
        self.mongo_client = None
        self.mongo_db = None
        self.sql_engine = None
        self.sql_session = None
    
    def connect_mongo(self):
        """Connect to MongoDB."""
        try:
            self.mongo_client = MongoClient(Config.MONGO_URI)
            self.mongo_db = self.mongo_client[Config.MONGO_DB_NAME]
            logger.info("Connected to MongoDB successfully")
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
    
    def connect_sql(self):
        """Connect to SQL database using SQLAlchemy."""
        try:
            self.sql_engine = create_engine(Config.get_database_url())
            Base.metadata.create_all(self.sql_engine)
            Session = sessionmaker(bind=self.sql_engine)
            self.sql_session = Session()
            logger.info("Connected to SQL database successfully")
        except Exception as e:
            logger.error(f"Failed to connect to SQL database: {e}")
    
    def insert_mongo_document(self, collection_name: str, document: Dict[str, Any]) -> Optional[str]:
        """
        Insert a document into MongoDB collection.
        
        Args:
            collection_name: Name of the collection
            document: Document to insert
            
        Returns:
            Inserted document ID
        """
        if not self.mongo_db:
            self.connect_mongo()
        
        try:
            collection = self.mongo_db[collection_name]
            result = collection.insert_one(document)
            logger.info(f"Inserted document with ID: {result.inserted_id}")
            return str(result.inserted_id)
        except Exception as e:
            logger.error(f"Failed to insert document: {e}")
            return None
    
    def find_mongo_documents(self, collection_name: str, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Find documents in MongoDB collection.
        
        Args:
            collection_name: Name of the collection
            query: Query dictionary
            
        Returns:
            List of matching documents
        """
        if not self.mongo_db:
            self.connect_mongo()
        
        try:
            collection = self.mongo_db[collection_name]
            documents = list(collection.find(query))
            logger.info(f"Found {len(documents)} documents")
            return documents
        except Exception as e:
            logger.error(f"Failed to find documents: {e}")
            return []
    
    def create_user(self, username: str, email: str) -> Optional[User]:
        """
        Create a new user in SQL database.
        
        Args:
            username: Username
            email: Email address
            
        Returns:
            Created User object
        """
        if not self.sql_session:
            self.connect_sql()
        
        try:
            user = User(username=username, email=email)
            self.sql_session.add(user)
            self.sql_session.commit()
            logger.info(f"Created user: {username}")
            return user
        except Exception as e:
            self.sql_session.rollback()
            logger.error(f"Failed to create user: {e}")
            return None
    
    def close_connections(self):
        """Close all database connections."""
        if self.mongo_client:
            self.mongo_client.close()
            logger.info("Closed MongoDB connection")
        
        if self.sql_session:
            self.sql_session.close()
            logger.info("Closed SQL connection")
