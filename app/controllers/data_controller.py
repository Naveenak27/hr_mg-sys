# app/controllers/data_controller.py
from typing import List, Optional, Dict, Any
from app.services.firebase_service import FirebaseService
from app.models.firebase_models import FirebaseDocument

class DataController:
    def __init__(self):
        self.firebase_service = FirebaseService()
    
    # Collection Management
    def get_all_collections(self) -> List[str]:
        """Get all collection names"""
        return self.firebase_service.get_all_collections()
    
    def get_collection_info(self) -> Dict[str, Dict[str, Any]]:
        """Get detailed information about all collections"""
        return self.firebase_service.get_collection_info()
    
    # User Roles
    def get_user_roles(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("userroles")
    
    def get_user_role_by_id(self, role_id: str) -> Optional[FirebaseDocument]:
        return self.firebase_service.get_document_by_id("userroles", role_id)
    
    # Activity Lists
    def get_activity_lists(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("activitylists")
    
    def get_activity_by_id(self, activity_id: str) -> Optional[FirebaseDocument]:
        return self.firebase_service.get_document_by_id("activitylists", activity_id)
    
    # Employee Lists
    def get_employee_lists(self) -> List[FirebaseDocument]:
        
        return self.firebase_service.get_collection_data("employeelists")
    
    def get_employee_by_id(self, emp_id: str) -> Optional[FirebaseDocument]:
        return self.firebase_service.get_document_by_id("employeelists", emp_id)
    
    # Vendor Lists
    def get_vendor_lists(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("performancereviews")
    
    def get_vendor_by_id(self, vendor_id: str) -> Optional[FirebaseDocument]:
        return self.firebase_service.get_document_by_id("performancereviews", vendor_id)
    
    # Profiles (Recruitment)
    def get_profiles(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("profiles")
    
    def get_profile_by_id(self, profile_id: str) -> Optional[FirebaseDocument]:
        return self.firebase_service.get_document_by_id("profiles", profile_id)
    
    # Client Profiles
    def get_client_profiles(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("clientprofiles")
    
    def get_client_profile_by_id(self, client_id: str) -> Optional[FirebaseDocument]:
        return self.firebase_service.get_document_by_id("clientprofiles", client_id)
    
    # Jobs
    def get_jobs(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("jobs")
    
    def get_job_by_id(self, job_id: str) -> Optional[FirebaseDocument]:
        return self.firebase_service.get_document_by_id("jobs", job_id)
    
    # Skills
    def get_skills(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("skills")
    
    def get_skill_by_id(self, skill_id: str) -> Optional[FirebaseDocument]:
        return self.firebase_service.get_document_by_id("skills", skill_id)
    
    # IT Requests
    def get_it_requests(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("itrequests")
    
    def get_it_request_by_id(self, request_id: str) -> Optional[FirebaseDocument]:
        return self.firebase_service.get_document_by_id("itrequests", request_id)
    
    # Domains
    def get_domains(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("domains")
    
    def get_domain_by_id(self, domain_id: str) -> Optional[FirebaseDocument]:
        return self.firebase_service.get_document_by_id("domains", domain_id)
    
    # Performance Reviews
    def get_performance_reviews(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("performancereviews")
    
    def get_performance_review_by_id(self, review_id: str) -> Optional[FirebaseDocument]:
        return self.firebase_service.get_document_by_id("performancereviews", review_id)
    
    # Client Performance Reviews
    def get_client_performance_reviews(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("performancereviewsclient")
    
    def get_client_performance_review_by_id(self, review_id: str) -> Optional[FirebaseDocument]:
        return self.firebase_service.get_document_by_id("performancereviewsclient", review_id)
    
    # Config Generals
    def get_config_generals(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("configgenerals")
    
    # Config PDPs
    def get_config_pdps(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("configpdps")
    
    # Leave Summaries
    def get_leave_summaries(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("leavesummaries")
    
    # Leave Details
    def get_leave_details(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("leavedetails")
    
    # Holidays
    def get_holidays(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("holidays")
    
    # GMls
    def get_gmls(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("configgmls")
    
    # Config All
    def get_config_all(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("configall")
    
    # Reviewers
    def get_reviewers(self) -> List[FirebaseDocument]:
        return self.firebase_service.get_collection_data("reviewers")
    # Add this method to your data_controller class

# Add this method inside your DataController class

    def authenticate_user(self, email: str, password: str):
        """Simple authentication by email and password"""
        try:
            # Get all users from userroles collection
            users = self.firebase_service.get_collection_data("userroles")
            
            # Find user with matching email and password
            for user in users:
                if (user.data.get("email") == email and 
                    user.data.get("passwd") == password):
                    return {
                        "id": user.id,
                        "data": user.data
                    }
            
            return None
            
        except Exception as e:
            print(f"Authentication error: {e}")
            return None