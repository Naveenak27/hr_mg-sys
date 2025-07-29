# app/routes/api_routes.py
from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional, Dict, Any
from app.controllers.data_controller import DataController
from app.models.firebase_models import FirebaseDocument
from app.services.firebase_service import FirebaseService  # Make sure this is correct

router = APIRouter()
firebase_service = FirebaseService()
router = APIRouter()
data_controller = DataController()

@router.get("/status")
async def status():
    return {"status": "ok"}

# Collection Management endpoints
@router.get("/collections", response_model=List[str])
async def get_all_collections():
    """Get all collection names in the database"""
    try:
        return data_controller.get_all_collections()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/collections/info", response_model=Dict[str, Dict[str, Any]])
async def get_collection_info():
    """Get detailed information about all collections including document counts"""
    try:
        return data_controller.get_collection_info()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# User Roles endpoints
@router.get("/user", response_model=List[FirebaseDocument])
async def get_user_roles():
    try:
        return data_controller.get_user_roles()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user/{role_id}", response_model=FirebaseDocument)
async def get_user_role_by_id(role_id: str):
    try:
        role = data_controller.get_user_role_by_id(role_id)
        if not role:
            raise HTTPException(status_code=404, detail="User role not found")
        return role
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Activity Lists endpoints
@router.get("/activities", response_model=List[FirebaseDocument])
async def get_activities():
    try:
        return data_controller.get_activity_lists()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/activities/{activity_id}", response_model=FirebaseDocument)
async def get_activity_by_id(activity_id: str):
    try:
        activity = data_controller.get_activity_by_id(activity_id)
        if not activity:
            raise HTTPException(status_code=404, detail="Activity not found")
        return activity
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Employee Lists endpoints
@router.get("/employees", response_model=List[FirebaseDocument])
async def get_employees():
    try:
        return data_controller.get_employee_lists()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/employees/{emp_id}", response_model=FirebaseDocument)
async def get_employee_by_id(emp_id: str):
    try:
        employee = data_controller.get_employee_by_id(emp_id)
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Vendor Lists endpoints
@router.get("/vendors", response_model=List[FirebaseDocument])
async def get_vendors():
    try:
        return data_controller.get_vendor_lists()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/vendors/{vendor_id}", response_model=FirebaseDocument)
async def get_vendor_by_id(vendor_id: str):
    try:
        vendor = data_controller.get_vendor_by_id(vendor_id)
        if not vendor:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return vendor
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Profiles endpoints
@router.get("/profiles", response_model=List[FirebaseDocument])
async def get_profiles():
    try:
        return data_controller.get_profiles()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/profiles/{profile_id}", response_model=FirebaseDocument)
async def get_profile_by_id(profile_id: str):
    try:
        profile = data_controller.get_profile_by_id(profile_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# Client Profiles endpoints
@router.get("/client-profiles", response_model=List[FirebaseDocument])
async def get_client_profiles():
    try:
        return data_controller.get_client_profiles()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/client-profiles/{client_id}", response_model=FirebaseDocument)
async def get_client_profile_by_id(client_id: str):
    try:
        client = data_controller.get_client_profile_by_id(client_id)
        if not client:
            raise HTTPException(status_code=404, detail="Client profile not found")
        return client
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Jobs endpoints
@router.get("/jobs", response_model=List[FirebaseDocument])
async def get_jobs():
    try:
        return data_controller.get_jobs()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/jobs/{job_id}", response_model=FirebaseDocument)
async def get_job_by_id(job_id: str):
    try:
        job = data_controller.get_job_by_id(job_id)
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        return job
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Skills endpoints
@router.get("/skills", response_model=List[FirebaseDocument])
async def get_skills():
    try:
        return data_controller.get_skills()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/skills/{skill_id}", response_model=FirebaseDocument)
async def get_skill_by_id(skill_id: str):
    try:
        skill = data_controller.get_skill_by_id(skill_id)
        if not skill:
            raise HTTPException(status_code=404, detail="Skill not found")
        return skill
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# IT Requests endpoints
@router.get("/it-requests", response_model=List[FirebaseDocument])
async def get_it_requests():
    try:
        return data_controller.get_it_requests()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/it-requests/{request_id}", response_model=FirebaseDocument)
async def get_it_request_by_id(request_id: str):
    try:
        request = data_controller.get_it_request_by_id(request_id)
        if not request:
            raise HTTPException(status_code=404, detail="IT request not found")
        return request
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Domains endpoints
@router.get("/domains", response_model=List[FirebaseDocument])
async def get_domains():
    try:
        return data_controller.get_domains()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/domains/{domain_id}", response_model=FirebaseDocument)
async def get_domain_by_id(domain_id: str):
    try:
        domain = data_controller.get_domain_by_id(domain_id)
        if not domain:
            raise HTTPException(status_code=404, detail="Domain not found")
        return domain
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Performance Reviews endpoints
@router.get("/performance-reviews", response_model=List[FirebaseDocument])
async def get_performance_reviews():
    try:
        return data_controller.get_performance_reviews()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/performance-reviews/{review_id}", response_model=FirebaseDocument)
async def get_performance_review_by_id(review_id: str):
    try:
        review = data_controller.get_performance_review_by_id(review_id)
        if not review:
            raise HTTPException(status_code=404, detail="Performance review not found")
        return review
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Client Performance Reviews endpoints
@router.get("/client-performance-reviews", response_model=List[FirebaseDocument])
async def get_client_performance_reviews():
    try:
        return data_controller.get_client_performance_reviews()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Configuration endpoints
@router.get("/config/generals", response_model=List[FirebaseDocument])
async def get_config_generals():
    try:
        return data_controller.get_config_generals()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/config/pdps", response_model=List[FirebaseDocument])
async def get_config_pdps():
    try:
        return data_controller.get_config_pdps()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/config/all", response_model=List[FirebaseDocument])
async def get_config_all():
    try:
        return data_controller.get_config_all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/config/gmls", response_model=List[FirebaseDocument])
async def get_gmls():
    try:
        return data_controller.get_gmls()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Leave endpoints
@router.get("/leave/summaries", response_model=List[FirebaseDocument])
async def get_leave_summaries():
    try:
        return data_controller.get_leave_summaries()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/leave/details", response_model=List[FirebaseDocument])
async def get_leave_details():
    try:
        return data_controller.get_leave_details()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Holidays endpoints
@router.get("/holidays", response_model=List[FirebaseDocument])
async def get_holidays():
    try:
        return data_controller.get_holidays()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Reviewers endpoints
@router.get("/reviewers", response_model=List[FirebaseDocument])
async def get_reviewers():
    try:
        return data_controller.get_reviewers()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import HTTPException
from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    passwd: str

@router.post("/auth/login")
async def login(login_request: LoginRequest):
    """Simple login endpoint"""
    try:
        # Find user by email and password
        user = data_controller.authenticate_user(
            email=login_request.email,
            password=login_request.passwd
        )
        
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        return {
            "success": True,
            "user": user["data"]
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
