from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.api_routes import router as api_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Firebase Python Backend",
        description="Python backend with MVC pattern for Firebase Firestore",
        version="1.0.0"
    )

    # ✅ CORS configuration
    origins = [
        "http://localhost:3000",      # React/Vite dev
        "http://127.0.0.1:5500",      # HTML/JS static dev
        "https://your-frontend.com",  # Your production domain (if applicable)
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,        # Or ["*"] for all (not safe for production)
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ✅ Register API routes
    app.include_router(api_router, prefix="/api/v1")

    # ✅ Health check routes
    @app.get("/")
    async def root():
        return {"message": "Firebase Python Backend API is running!"}

    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}

    return app
