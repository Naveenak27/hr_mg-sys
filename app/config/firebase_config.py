import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

load_dotenv()

class FirebaseConfig:
    def __init__(self):
        self.db = None
        self.initialize_firebase()
    
    def initialize_firebase(self):
        """Initialize Firebase Admin SDK using environment variables"""
        try:
            # Required environment variables
            required_vars = [
                "FIREBASE_TYPE", "FIREBASE_PROJECT_ID", "FIREBASE_PRIVATE_KEY_ID",
                "FIREBASE_PRIVATE_KEY", "FIREBASE_CLIENT_EMAIL", "FIREBASE_CLIENT_ID",
                "FIREBASE_AUTH_URI", "FIREBASE_TOKEN_URI", "FIREBASE_AUTH_PROVIDER_X509_CERT_URL",
                "FIREBASE_CLIENT_X509_CERT_URL"
            ]
            
            # Check if all required variables exist
            missing_vars = [var for var in required_vars if not os.getenv(var)]
            if missing_vars:
                raise ValueError(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
            
            print("🔄 Using environment variables...")
            
            # Build service account info from environment variables
            service_account_info = {
                "type": os.getenv("FIREBASE_TYPE"),
                "project_id": os.getenv("FIREBASE_PROJECT_ID"),
                "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
                "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace('\\n', '\n'),
                "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
                "client_id": os.getenv("FIREBASE_CLIENT_ID"),
                "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
                "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
                "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
                "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL"),
                "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN", "googleapis.com")
            }
            
            cred = credentials.Certificate(service_account_info)
            firebase_admin.initialize_app(cred)
            self.db = firestore.client()
            print("✅ Firebase initialized successfully!")
                
        except Exception as e:
            print(f"❌ Error initializing Firebase: {e}")
            raise e

# Singleton instance
firebase_config = FirebaseConfig()
db = firebase_config.db
