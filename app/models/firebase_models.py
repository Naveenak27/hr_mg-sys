# app/models/firebase_models.py
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from datetime import datetime

class FirebaseDocument(BaseModel):
    id: str
    data: Dict[str, Any]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class UserRole(BaseModel):
    id: Optional[str] = None
    # Add specific fields based on your userroles collection structure
    role: Optional[str] = None
    permissions: Optional[List[str]] = None
    user_id: Optional[str] = None

class ActivityList(BaseModel):
    id: Optional[str] = None
    # Add specific fields based on your activitylists collection structure
    activity_name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class Employee(BaseModel):
    id: Optional[str] = None
    # Add specific fields based on your employeelists collection structure
    name: Optional[str] = None
    email: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None

class Vendor(BaseModel):
    id: Optional[str] = None
    # Add specific fields based on your vendorlists collection structure
    vendor_name: Optional[str] = None
    contact_info: Optional[str] = None

class Profile(BaseModel):
    id: Optional[str] = None
    # Add specific fields based on your profiles collection structure
    name: Optional[str] = None
    skills: Optional[List[str]] = None
    experience: Optional[int] = None

class ClientProfile(BaseModel):
    id: Optional[str] = None
    # Add specific fields based on your clientprofiles collection structure
    client_name: Optional[str] = None
    industry: Optional[str] = None

class Job(BaseModel):
    id: Optional[str] = None
    # Add specific fields based on your jobs collection structure
    title: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[List[str]] = None

class Skill(BaseModel):
    id: Optional[str] = None
    # Add specific fields based on your skills collection structure
    skill_name: Optional[str] = None
    category: Optional[str] = None

class ITRequest(BaseModel):
    id: Optional[str] = None
    # Add specific fields based on your itrequests collection structure
    request_type: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None

class Domain(BaseModel):
    id: Optional[str] = None
    # Add specific fields based on your domains collection structure
    domain_name: Optional[str] = None
    description: Optional[str] = None

class PerformanceReview(BaseModel):
    id: Optional[str] = None
    # Add specific fields based on your performancereviews collection structure
    employee_id: Optional[str] = None
    rating: Optional[float] = None
    review_period: Optional[str] = None

class ClientPerformanceReview(BaseModel):
    id: Optional[str] = None
    # Add specific fields based on your performancereviewsclient collection structure
    client_id: Optional[str] = None
    rating: Optional[float] = None
    review_period: Optional[str] = None