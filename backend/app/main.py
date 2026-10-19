from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .database import engine, Base, SessionLocal
from . import models  # noqa: F401 - ensures models are registered
from .seed import seed_database
from .api.products import router as products_router
from .api.auth import router as auth_router
from .api.cart import router as cart_router
from .api.orders import router as orders_router
from .api.wholesale import router as wholesale_router
from .api.newsletter import router as newsletter_router
from .api.admin import router as admin_router

# Create tables
Base.metadata.create_all(bind=engine)

# Seed initial data
db = SessionLocal()
try:
    seed_database(db)
finally:
    db.close()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="LUST8 Adult Wellness Products API",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
def root():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "docs": "/docs",
    }


@app.get("/health", tags=["Root"])
def health_check():
    return {"status": "healthy"}


# Register API routers
app.include_router(products_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
app.include_router(cart_router, prefix="/api")
app.include_router(orders_router, prefix="/api")
app.include_router(wholesale_router, prefix="/api")
app.include_router(newsletter_router, prefix="/api")
app.include_router(admin_router, prefix="/api")
