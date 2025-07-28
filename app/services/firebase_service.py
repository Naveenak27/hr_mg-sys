# app/services/firebase_service.py
from typing import List, Dict, Any, Optional
from app.config.firebase_config import db
from app.models.firebase_models import FirebaseDocument
import logging

logger = logging.getLogger(__name__)

class FirebaseService:
    def __init__(self):
        self.db = db
    
    def get_collection_info(self) -> Dict[str, Dict[str, Any]]:
        """Get detailed information about all collections including document counts"""
        try:
            collections = self.db.collections()
            collection_info = {}
            
            for collection in collections:
                collection_name = collection.id
                try:
                    # Get document count
                    docs = list(collection.stream())
                    doc_count = len(docs)
                    
                    # Get sample document structure (first document)
                    sample_doc = None
                    if docs:
                        sample_doc = docs[0].to_dict()
                        # Only show keys for structure, not actual data
                        sample_structure = list(sample_doc.keys()) if sample_doc else []
                    else:
                        sample_structure = []
                    
                    collection_info[collection_name] = {
                        "document_count": doc_count,
                        "sample_fields": sample_structure,
                        "has_documents": doc_count > 0
                    }
                    
                    logger.info(f"📊 Collection '{collection_name}': {doc_count} documents")
                    
                except Exception as e:
                    logger.warning(f"⚠️ Could not get info for collection '{collection_name}': {e}")
                    collection_info[collection_name] = {
                        "document_count": 0,
                        "sample_fields": [],
                        "has_documents": False,
                        "error": str(e)
                    }
            
            return collection_info
        except Exception as e:
            logger.error(f"❌ Error getting collection info: {e}")
            raise e
    
    def get_collection_data(self, collection_name: str) -> List[FirebaseDocument]:
        """Get all documents from a collection"""
        try:
            docs = self.db.collection(collection_name).stream()
            documents = []
            for doc in docs:
                doc_data = doc.to_dict()
                document = FirebaseDocument(
                    id=doc.id,
                    data=doc_data,
                    created_at=doc_data.get('created_at'),
                    updated_at=doc_data.get('updated_at')
                )
                documents.append(document)
                logger.info(f"📄 Document ID: {doc.id}")
                logger.info(f"📦 Data: {doc_data}")
            
            logger.info(f"✅ Retrieved {len(documents)} documents from '{collection_name}'")
            return documents
        except Exception as e:
            logger.error(f"❌ Error getting documents from {collection_name}: {e}")
            raise e
    
    def get_document_by_id(self, collection_name: str, doc_id: str) -> Optional[FirebaseDocument]:
        """Get a specific document by ID"""
        try:
            doc = self.db.collection(collection_name).document(doc_id).get()
            if doc.exists:
                doc_data = doc.to_dict()
                return FirebaseDocument(
                    id=doc.id,
                    data=doc_data,
                    created_at=doc_data.get('created_at'),
                    updated_at=doc_data.get('updated_at')
                )
            return None
        except Exception as e:
            logger.error(f"❌ Error getting document {doc_id} from {collection_name}: {e}")
            raise e
    
    def get_collection_with_filter(self, collection_name: str, field: str, operator: str, value: Any) -> List[FirebaseDocument]:
        """Get documents from a collection with filter"""
        try:
            query = self.db.collection(collection_name).where(field, operator, value)
            docs = query.stream()
            documents = []
            for doc in docs:
                doc_data = doc.to_dict()
                document = FirebaseDocument(
                    id=doc.id,
                    data=doc_data,
                    created_at=doc_data.get('created_at'),
                    updated_at=doc_data.get('updated_at')
                )
                documents.append(document)
            return documents
        except Exception as e:
            logger.error(f"❌ Error getting filtered documents from {collection_name}: {e}")
            raise e
    
    def get_collection_with_pagination(self, collection_name: str, limit: int = 10, offset: int = 0) -> List[FirebaseDocument]:
        """Get documents with pagination"""
        try:
            query = self.db.collection(collection_name).limit(limit).offset(offset)
            docs = query.stream()
            documents = []
            for doc in docs:
                doc_data = doc.to_dict()
                document = FirebaseDocument(
                    id=doc.id,
                    data=doc_data,
                    created_at=doc_data.get('created_at'),
                    updated_at=doc_data.get('updated_at')
                )
                documents.append(document)
            return documents
        except Exception as e:
            logger.error(f"❌ Error getting paginated documents from {collection_name}: {e}")
            raise e

    def get_all_collections(self) -> List[str]:
            """Get all collection names in the database"""
            try:
                collections = self.db.collections()
                collection_names = [collection.id for collection in collections]
                logger.info(f"📚 Found collections: {collection_names}")
                return collection_names
            except Exception as e:
                logger.error(f"❌ Error getting collection names: {e}")
                raise e