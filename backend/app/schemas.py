from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List
from enum import Enum


# ============ Auth ============
class UserRole(str, Enum):
    CUSTOMER = "customer"
    ADMIN = "admin"


class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class UserBase(BaseModel):
    email: EmailStr
    name: str


class UserCreate(UserBase):
    password: str = Field(min_length=6)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: int
    role: UserRole
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


# ============ Category ============
class CategoryBase(BaseModel):
    name: str
    name_zh: str
    slug: str
    icon: str = ""
    sort_order: int = 0


class CategoryResponse(CategoryBase):
    id: int
    product_count: Optional[int] = 0

    class Config:
        from_attributes = True


# ============ Product ============
class ProductBase(BaseModel):
    name: str
    name_zh: str
    slug: str
    tagline: str = ""
    tagline_zh: str = ""
    description: str = ""
    description_zh: str = ""
    price: float
    original_price: Optional[float] = None
    category_id: int
    badge: str = ""
    badge_zh: str = ""
    colors: List[str] = []
    features: List[str] = []
    features_zh: List[str] = []
    weight: str = ""
    dimensions: str = ""
    stock: int = 100
    is_active: bool = True
    is_featured: bool = False


class ProductResponse(ProductBase):
    id: int
    category: Optional[CategoryResponse] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ProductListItem(BaseModel):
    id: int
    name: str
    name_zh: str
    slug: str
    tagline: str
    tagline_zh: str
    price: float
    original_price: Optional[float] = None
    category_id: int
    badge: str
    badge_zh: str
    colors: List[str] = []
    is_featured: bool = False

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    items: List[ProductListItem]
    total: int
    page: int
    page_size: int
    total_pages: int


# ============ Cart ============
class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(ge=1, default=1)
    selected_color: str = ""


class CartItemUpdate(BaseModel):
    quantity: int = Field(ge=1)


class CartItemResponse(BaseModel):
    id: int
    product_id: int
    product_name: str
    product_name_zh: str
    quantity: int
    selected_color: str
    price: float
    subtotal: float
    added_at: datetime

    class Config:
        from_attributes = True


class CartResponse(BaseModel):
    items: List[CartItemResponse]
    total_items: int
    total_price: float


# ============ Order ============
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)
    color: str = ""


class OrderCreate(BaseModel):
    items: List[OrderItemCreate]
    customer_name: str
    customer_email: EmailStr
    customer_phone: str = ""
    shipping_address: str
    shipping_city: str = ""
    shipping_country: str
    shipping_zip: str = ""
    payment_method: str = ""
    notes: str = ""


class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    product_name: str
    quantity: int
    price: float
    color: str

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: int
    order_number: str
    status: OrderStatus
    subtotal: float
    shipping: float
    tax: float
    discount: float
    total: float
    customer_name: str
    customer_email: str
    customer_phone: str
    shipping_address: str
    shipping_city: str
    shipping_country: str
    shipping_zip: str
    payment_status: str
    notes: str
    items: List[OrderItemResponse]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ============ Wholesale ============
class WholesaleInquiryCreate(BaseModel):
    company_name: str
    contact_person: str
    email: EmailStr
    phone: str = ""
    country: str
    business_type: str = ""
    interests: List[str] = []
    quantity: str = ""
    whitelabel: str = "no"
    message: str = ""


class WholesaleInquiryResponse(BaseModel):
    id: int
    company_name: str
    contact_person: str
    email: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


# ============ Newsletter ============
class NewsletterSubscribe(BaseModel):
    email: EmailStr


class NewsletterResponse(BaseModel):
    id: int
    email: str
    subscribed_at: datetime

    class Config:
        from_attributes = True


# ============ Generic ============
class MessageResponse(BaseModel):
    message: str
    success: bool = True
