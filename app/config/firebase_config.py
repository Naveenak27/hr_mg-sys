import firebase_admin
from firebase_admin import credentials, firestore
import os
import json
from dotenv import load_dotenv

load_dotenv()

class FirebaseConfig:
    def __init__(self):
        self.db = None
        self.initialize_firebase()
    
    def initialize_firebase(self):
        """Initialize Firebase Admin SDK"""
        try:
            # Method 1: Service account JSON file (most reliable)
            service_account_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH")
            if service_account_path and os.path.exists(service_account_path):
                print("🔄 Using service account JSON file...")
                cred = credentials.Certificate(service_account_path)
                firebase_admin.initialize_app(cred)
                self.db = firestore.client()
                print("✅ Firebase initialized with JSON file!")
                return
            
            # Method 2: Complete service account JSON as environment variable
            service_account_json = os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON")
            if service_account_json:
                print("🔄 Using service account JSON from environment variable...")
                try:
                    service_account_info = json.loads(service_account_json)
                    cred = credentials.Certificate(service_account_info)
                    firebase_admin.initialize_app(cred)
                    self.db = firestore.client()
                    print("✅ Firebase initialized with JSON environment variable!")
                    return
                except json.JSONDecodeError as e:
                    print(f"❌ Invalid JSON in FIREBASE_SERVICE_ACCOUNT_JSON: {e}")
            
            # If neither method works
            print("❌ No valid Firebase configuration found")
            print("\n💡 Setup options:")
            print("Option 1 (Recommended): Download JSON file and set FIREBASE_SERVICE_ACCOUNT_PATH")
            print("Option 2: Set FIREBASE_SERVICE_ACCOUNT_JSON with complete JSON content")
            raise ValueError("No valid Firebase configuration found")
                
        except Exception as e:
            print(f"❌ Error initializing Firebase: {e}")
            raise e

# Singleton instance
firebase_config = FirebaseConfig()
db = firebase_config.db