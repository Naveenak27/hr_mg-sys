"""
Firebase Collections Debug Script
Run this to diagnose why collections() method is missing some collections
"""

import firebase_admin
from firebase_admin import credentials, firestore
from typing import List
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FirebaseCollectionsDebugger:
    def __init__(self, service_account_path: str, project_id: str = 'selfserviceportal-aa3f2'):
        """
        Initialize Firebase connection
        
        Args:
            service_account_path: Path to your service account JSON file
            project_id: Your Firebase project ID
        """
        try:
            # Initialize Firebase Admin SDK
            if not firebase_admin._apps:
                cred = credentials.Certificate(service_account_path)
                firebase_admin.initialize_app(cred, {
                    'projectId': project_id
                })
            
            self.db = firestore.client()
            self.project_id = project_id
            print(f"🚀 Firebase initialized successfully for project: {project_id}")
            
        except Exception as e:
            print(f"❌ Firebase initialization error: {e}")
            raise e

    def verify_connection(self):
        """Verify Firebase connection details"""
        print("\n🔍 VERIFYING CONNECTION")
        print("-" * 40)
        
        try:
            import firebase_admin
            
            # Check if app is initialized
            app = firebase_admin.get_app()
            print(f"🔗 Connected to project: {app.project_id}")
            
            # Check Firebase Admin SDK version
            print(f"📦 Firebase Admin SDK version: {firebase_admin.__version__}")
            
            # Test basic Firestore connection
            collections = list(self.db.collections())
            print(f"📚 Basic collections() call works: {len(collections)} collections found")
            
            return True
            
        except Exception as e:
            print(f"❌ Connection verification error: {e}")
            return False

    def check_database_info(self):
        """Check which Firestore database we're connected to"""
        print("\n🗄️ CHECKING DATABASE INFO")
        print("-" * 40)
        
        try:
            print(f"📊 Database client type: {type(self.db)}")
            print(f"📊 Database client: {self.db}")
            
            # Try to get database info if available
            if hasattr(self.db, '_database_string'):
                print(f"📊 Database string: {self.db._database_string}")
            
            if hasattr(self.db, '_database_string_internal'):
                print(f"📊 Database string internal: {self.db._database_string_internal}")
                
        except Exception as e:
            print(f"❌ Database info error: {e}")

    def debug_collections_detailed(self):
        """Detailed debugging of collection visibility"""
        print("\n🔍 DETAILED COLLECTIONS DEBUG")
        print("-" * 40)
        
        try:
            # What collections() method returns
            collections = self.db.collections()
            found_collections = [collection.id for collection in collections]
            print(f"🐍 Python collections() found: {found_collections}")
            print(f"📊 Total collections found by collections(): {len(found_collections)}")
            
            # Test direct access to userroles
            print(f"\n🔍 Testing direct access to 'userroles':")
            try:
                userroles_ref = self.db.collection('userroles')
                docs = userroles_ref.limit(3).get()
                print(f"✅ userroles: Can access directly, found {len(docs)} documents")
                for doc in docs:
                    print(f"  📄 Document ID: {doc.id}")
            except Exception as e:
                print(f"❌ userroles: Cannot access directly - {e}")
                
            # Test if it's in the collections list
            if 'userroles' in found_collections:
                print("✅ userroles IS in collections() result")
            else:
                print("❌ userroles is NOT in collections() result")
                
            return found_collections
            
        except Exception as e:
            print(f"❌ Debug error: {e}")
            return []

    def get_all_collections_alternative(self) -> List[str]:
        """Alternative method to find all collections"""
        print("\n🎯 ALTERNATIVE COLLECTION DETECTION")
        print("-" * 40)
        
        try:
            # Method 1: Standard collections() 
            collections = self.db.collections()
            standard_collections = [collection.id for collection in collections]
            print(f"📚 Standard method found: {standard_collections}")
            
            # Method 2: Try known collection names from your JS
            known_collections = [
                'userroles', 'activitylists', 'employeelists', 'vendorlists',
                'profiles', 'clientprofiles', 'jobs', 'skills', 'itrequests',
                'domains', 'performancereviews', 'performancereviewsclient',
                'configgenerals', 'configpdps', 'leavesummaries', 'leavedetails',
                'holidays', 'configgmls', 'configall', 'reviewers'
            ]
            
            print(f"\n🧪 Testing {len(known_collections)} known collections:")
            verified_collections = []
            missing_from_standard = []
            
            for collection_name in known_collections:
                try:
                    # Try to get at least one document
                    docs = self.db.collection(collection_name).limit(1).get()
                    if len(docs) > 0:
                        verified_collections.append(collection_name)
                        status = "✅ EXISTS"
                        if collection_name not in standard_collections:
                            missing_from_standard.append(collection_name)
                            status += " (MISSING FROM collections())"
                        print(f"  {status}: {collection_name} - {len(docs)} docs")
                    else:
                        print(f"  ⚠️ EMPTY: {collection_name}")
                except Exception as e:
                    print(f"  ❌ ERROR: {collection_name} - {e}")
            
            # Show what's missing from standard method
            if missing_from_standard:
                print(f"\n⚠️ COLLECTIONS MISSING FROM collections() METHOD:")
                for missing in missing_from_standard:
                    print(f"  - {missing}")
            
            # Combine both methods
            all_collections = list(set(standard_collections + verified_collections))
            print(f"\n🎯 FINAL COMBINED LIST ({len(all_collections)} total):")
            for col in sorted(all_collections):
                print(f"  - {col}")
            
            return all_collections
            
        except Exception as e:
            print(f"❌ Error in alternative collection detection: {e}")
            return []

    def test_specific_collection_operations(self, collection_name: str = 'userroles'):
        """Test various operations on a specific collection"""
        print(f"\n🧪 TESTING OPERATIONS ON '{collection_name}'")
        print("-" * 40)
        
        try:
            collection_ref = self.db.collection(collection_name)
            
            # Test 1: Get documents
            print("Test 1: Getting documents...")
            docs = collection_ref.limit(5).get()
            print(f"✅ Retrieved {len(docs)} documents")
            
            # Test 2: Count documents (if available)
            print("Test 2: Counting documents...")
            try:
                # This might not be available in all SDK versions
                count_query = collection_ref.count()
                count_result = count_query.get()
                print(f"✅ Total document count: {count_result[0][0].value}")
            except Exception as e:
                print(f"⚠️ Count not available: {e}")
                # Alternative count method
                all_docs = collection_ref.get()
                print(f"✅ Document count (manual): {len(all_docs)}")
            
            # Test 3: Get collection metadata
            print("Test 3: Collection reference info...")
            print(f"✅ Collection ID: {collection_ref.id}")
            print(f"✅ Collection path: {collection_ref.path}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error testing {collection_name}: {e}")
            return False

    def complete_debug(self):
        """Run all debug methods"""
        print("=" * 60)
        print("🔍 FIREBASE COLLECTIONS COMPLETE DEBUG")
        print("=" * 60)
        
        # Step 1: Verify connection
        if not self.verify_connection():
            print("❌ Connection failed, stopping debug")
            return []
        
        # Step 2: Check database info
        self.check_database_info()
        
        # Step 3: Detailed collections debug
        standard_collections = self.debug_collections_detailed()
        
        # Step 4: Alternative collection detection
        all_collections = self.get_all_collections_alternative()
        
        # Step 5: Test specific collection operations
        self.test_specific_collection_operations('userroles')
        
        # Final summary
        print("\n" + "=" * 60)
        print("📋 FINAL SUMMARY")
        print("=" * 60)
        print(f"🎯 Total collections found: {len(all_collections)}")
        print(f"📚 Standard collections() method: {len(standard_collections)}")
        print(f"🔍 Alternative method found: {len(all_collections) - len(standard_collections)} additional")
        
        return all_collections


def main():
    """
    Main function to run the debug
    
    IMPORTANT: Update these values before running!
    """
    
    # TODO: UPDATE THESE PATHS/VALUES
    SERVICE_ACCOUNT_PATH = "firebase-service-account.json"  # ← UPDATE THIS
    PROJECT_ID = "selfserviceportal-aa3f2"
    
    print("🚀 Starting Firebase Collections Debug...")
    print(f"📁 Service Account: {SERVICE_ACCOUNT_PATH}")
    print(f"🎯 Project ID: {PROJECT_ID}")
    
    try:
        # Create debugger instance
        debugger = FirebaseCollectionsDebugger(SERVICE_ACCOUNT_PATH, PROJECT_ID)
        
        # Run complete debug
        collections = debugger.complete_debug()
        
        print(f"\n✅ Debug completed! Found {len(collections)} collections total.")
        
        return collections
        
    except Exception as e:
        print(f"❌ Debug failed: {e}")
        return []


if __name__ == "__main__":
    # Run the debug
    result = main()
    
    # You can also run individual methods like this:
    # debugger = FirebaseCollectionsDebugger("path/to/serviceAccount.json")
    # debugger.verify_connection()
    # debugger.debug_collections_detailed()