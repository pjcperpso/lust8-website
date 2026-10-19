from sqlalchemy.orm import Session
from . import models
from .auth import hash_password


CATEGORIES = [
    {"slug": "wand", "name": "Wand Massagers", "name_zh": "震动棒", "icon": "wand", "sort_order": 1},
    {"slug": "suction", "name": "Clitoral Suction", "name_zh": "吮吸玩具", "icon": "drop", "sort_order": 2},
    {"slug": "rabbit", "name": "Rabbit Vibrators", "name_zh": "兔子跳蛋", "icon": "rabbit", "sort_order": 3},
    {"slug": "gspot", "name": "G-Spot Toys", "name_zh": "G点玩具", "icon": "spark", "sort_order": 4},
    {"slug": "kegel", "name": "Kegel Balls", "name_zh": "凯格尔球", "icon": "sphere", "sort_order": 5},
    {"slug": "couples", "name": "Couples Toys", "name_zh": "情侣玩具", "icon": "infinity", "sort_order": 6},
    {"slug": "male", "name": "Male Toys", "name_zh": "男用玩具", "icon": "bolt", "sort_order": 7},
    {"slug": "dildo", "name": "Dildos", "name_zh": "仿真阳具", "icon": "bar", "sort_order": 8},
    {"slug": "anal", "name": "Anal Toys", "name_zh": "后庭玩具", "icon": "teardrop", "sort_order": 9},
    {"slug": "bondage", "name": "Bondage", "name_zh": "束缚", "icon": "lock", "sort_order": 10},
    {"slug": "accessories", "name": "Accessories", "name_zh": "配件", "icon": "star", "sort_order": 11},
]

PRODUCTS = [
    {
        "slug": "aura-wand",
        "name": "Aura Wand",
        "name_zh": "Aura 震动棒",
        "tagline": "Luxury Body Massager",
        "tagline_zh": "奢华身体按摩棒",
        "description": "Experience ultimate relaxation with our premium silicone wand massager. Featuring 20 vibration modes, a whisper-quiet motor, and an ergonomic handle designed for extended play sessions.",
        "description_zh": "体验我们高级硅胶震动棒带来的极致放松。20种震动模式，超静音马达，符合人体工学的手柄设计，让你享受更长时间的玩耍。",
        "price": 89.99,
        "original_price": 119.99,
        "category_id": 1,
        "badge": "Bestseller",
        "badge_zh": "畅销",
        "colors": ["Deep Rose", "Midnight Black", "Lavender"],
        "features": [
            "20 vibration patterns & 8 speeds",
            "IPX7 fully waterproof",
            "USB-C rechargeable",
            "Medical-grade silicone",
            "Ultra-quiet (<50dB)",
            "4-hour battery life",
            "Travel lock included"
        ],
        "features_zh": [
            "20种震动模式 & 8种速度",
            "IPX7 全身防水",
            "USB-C 充电",
            "医疗级硅胶",
            "超静音 (<50dB)",
            "4小时续航",
            "旅行锁功能"
        ],
        "weight": "450g",
        "dimensions": "220 x 45mm",
        "stock": 500,
        "is_featured": True,
        "sort_order": 1,
    },
    {
        "slug": "luna-beads",
        "name": "Luna Beads",
        "name_zh": "Luna 凯格尔球",
        "tagline": "Kegel Trainer Set",
        "tagline_zh": "凯格尔训练套装",
        "description": "Strengthen your pelvic floor with our progressive weight Kegel training set. Perfect for postpartum recovery, enhanced intimacy, and improved bladder control.",
        "description_zh": "通过我们渐进重量的凯格尔训练套装增强盆底肌。非常适合产后恢复、提升亲密感和改善膀胱控制。",
        "price": 49.99,
        "original_price": 69.99,
        "category_id": 5,
        "badge": "New",
        "badge_zh": "新品",
        "colors": ["Blush Pink", "Pearl White"],
        "features": [
            "Set of 5 progressive weights",
            "Body-safe silicone coating",
            "Easy retrieval string",
            "Waterproof & easy to clean",
            "Doctor recommended",
            "Discreet storage pouch"
        ],
        "features_zh": [
            "5个渐进重量套装",
            "身体安全硅胶涂层",
            "易取出拉绳",
            "防水易清洁",
            "医生推荐",
            "私密收纳袋"
        ],
        "weight": "120g (set)",
        "dimensions": "Varies by size",
        "stock": 300,
        "is_featured": False,
        "sort_order": 2,
    },
    {
        "slug": "eclipse-duo",
        "name": "Eclipse Duo",
        "name_zh": "Eclipse 双人震动环",
        "tagline": "Couples Ring",
        "tagline_zh": "情侣震动环",
        "description": "Elevate intimacy together. The Eclipse Duo delivers synchronized pleasure with dual motors designed to enhance sensation for both partners simultaneously.",
        "description_zh": "一起提升亲密感。Eclipse Duo 双马达设计，同步为双方带来增强的愉悦感受。",
        "price": 59.99,
        "original_price": 79.99,
        "category_id": 6,
        "badge": "Hot",
        "badge_zh": "热卖",
        "colors": ["Gunmetal", "Rose Gold"],
        "features": [
            "Dual vibration motors",
            "App-controlled (iOS & Android)",
            "90+ vibration patterns",
            "Long-distance mode",
            "USB rechargeable",
            "Premium silicone",
            "One size fits most"
        ],
        "features_zh": [
            "双震动马达",
            "APP控制 (iOS & 安卓)",
            "90+种震动模式",
            "远程模式",
            "USB充电",
            "高级硅胶",
            "均码"
        ],
        "weight": "28g",
        "dimensions": "35 x 20mm",
        "stock": 250,
        "is_featured": False,
        "sort_order": 3,
    },
    {
        "slug": "velvet-curve",
        "name": "Velvet Curve",
        "name_zh": "Velvet G点震动棒",
        "tagline": "G-Spot Vibrator",
        "tagline_zh": "G点震动棒",
        "description": "Ergonomically curved for precise G-spot stimulation. The Velvet Curve features a flexible tip and multiple intensities to suit every preference.",
        "description_zh": "符合人体工学的弯曲设计，精准刺激G点。Velvet Curve 灵活的头部和多种强度选择，满足每个人的偏好。",
        "price": 79.99,
        "original_price": 99.99,
        "category_id": 4,
        "badge": "",
        "badge_zh": "",
        "colors": ["Deep Purple", "Ruby Red", "Ocean Teal"],
        "features": [
            "Curved G-spot tip",
            "12 vibration modes",
            "Flexible neck",
            "Medical-grade silicone",
            "USB rechargeable",
            "IPX7 waterproof",
            "Quiet operation"
        ],
        "features_zh": [
            "弯曲G点头部",
            "12种震动模式",
            "灵活颈部",
            "医疗级硅胶",
            "USB充电",
            "IPX7 防水",
            "静音运行"
        ],
        "weight": "140g",
        "dimensions": "190 x 32mm",
        "stock": 200,
        "is_featured": False,
        "sort_order": 4,
    },
    {
        "slug": "sensual-set",
        "name": "Sensual Set",
        "name_zh": "Sensual 按摩蜡烛套装",
        "tagline": "Massage Candle Collection",
        "tagline_zh": "按摩蜡烛系列",
        "description": "Set the mood with our luxury massage candle trio. Made with natural soy wax and premium essential oils for a warm, sensual massage experience.",
        "description_zh": "用我们的奢华按摩蜡烛三件套营造氛围。采用天然大豆蜡和优质精油，带来温暖、感性的按摩体验。",
        "price": 34.99,
        "original_price": 49.99,
        "category_id": 11,
        "badge": "",
        "badge_zh": "",
        "colors": ["Sandalwood", "Rose", "Jasmine"],
        "features": [
            "3 scents: Sandalwood, Rose, Jasmine",
            "100% natural soy wax",
            "Low-temperature burn",
            "Skin-safe oils",
            "40hr burn time each",
            "Vegan & cruelty-free"
        ],
        "features_zh": [
            "3种香型：檀香、玫瑰、茉莉",
            "100% 天然大豆蜡",
            "低温燃烧",
            "护肤精油",
            "每支40小时燃烧时间",
            "纯素 & 无动物实验"
        ],
        "weight": "3 x 120g",
        "dimensions": "60 x 80mm each",
        "stock": 400,
        "is_featured": False,
        "sort_order": 5,
    },
    {
        "slug": "nocturne-rabbit",
        "name": "Nocturne Rabbit",
        "name_zh": "Nocturne 兔子跳蛋",
        "tagline": "Dual Action Vibe",
        "tagline_zh": "双效震动棒",
        "description": "Dual-stimulation at its finest. The iconic rabbit design delivers simultaneous internal and external pleasure with independent motor controls.",
        "description_zh": "双重刺激的极致体验。标志性的兔子设计，独立马达控制，同时带来内部和外部的愉悦。",
        "price": 99.99,
        "original_price": 129.99,
        "category_id": 3,
        "badge": "Premium",
        "badge_zh": "高端",
        "colors": ["Black", "Pink", "Purple"],
        "features": [
            "Two independent motors",
            "15 vibration patterns",
            "Flexible bunny ears",
            "Heated tip (38°C)",
            "USB-C rechargeable",
            "Premium silicone",
            "Memory function"
        ],
        "features_zh": [
            "两个独立马达",
            "15种震动模式",
            "灵活兔耳",
            "加热头部 (38°C)",
            "USB-C 充电",
            "高级硅胶",
            "记忆功能"
        ],
        "weight": "180g",
        "dimensions": "205 x 40mm",
        "stock": 180,
        "is_featured": True,
        "sort_order": 6,
    },
    {
        "slug": "halo-clitoral",
        "name": "Halo Clitoral",
        "name_zh": "Halo 吮吸器",
        "tagline": "Air Pulse Stimulator",
        "tagline_zh": "气流吮吸刺激器",
        "description": "Revolutionary air-pulse technology delivers contact-free clitoral stimulation. 11 intensity levels from gentle teasing to intense pulses.",
        "description_zh": "革命性的气流脉冲技术，无接触式阴蒂刺激。11种强度级别，从轻柔挑逗到强烈脉冲。",
        "price": 109.99,
        "original_price": 149.99,
        "category_id": 2,
        "badge": "Top Rated",
        "badge_zh": "最高评分",
        "colors": ["Rose", "Mint", "Charcoal"],
        "features": [
            "Air-pulse suction technology",
            "11 intensity levels",
            "10 vibration patterns",
            "Ultra-quiet motor",
            "USB-C fast charging",
            "IPX7 waterproof",
            "Travel lock & pouch"
        ],
        "features_zh": [
            "气流吮吸技术",
            "11种强度级别",
            "10种震动模式",
            "超静音马达",
            "USB-C 快充",
            "IPX7 防水",
            "旅行锁 & 收纳袋"
        ],
        "weight": "95g",
        "dimensions": "110 x 45mm",
        "stock": 220,
        "is_featured": True,
        "sort_order": 7,
    },
    {
        "slug": "titan-pro",
        "name": "Titan Pro",
        "name_zh": "Titan Pro 男用飞机杯",
        "tagline": "Male Masturbator",
        "tagline_zh": "男用自慰器",
        "description": "Next-generation male stroker with realistic texture and adjustable suction. Featuring multiple vibration modes and a warming function for lifelike sensations.",
        "description_zh": "新一代男用飞机杯，逼真纹理，可调节吸力。多种震动模式和加热功能，带来真实感受。",
        "price": 79.99,
        "original_price": 99.99,
        "category_id": 7,
        "badge": "",
        "badge_zh": "",
        "colors": ["Clear", "Black", "Flesh"],
        "features": [
            "Realistic TPR sleeve",
            "10 vibration modes",
            "Adjustable suction",
            "Warming function (40°C)",
            "USB rechargeable",
            "Easy to clean",
            "Discreet design"
        ],
        "features_zh": [
            "逼真 TPR 内胆",
            "10种震动模式",
            "可调节吸力",
            "加热功能 (40°C)",
            "USB充电",
            "易清洁",
            "隐蔽设计"
        ],
        "weight": "380g",
        "dimensions": "180 x 80mm",
        "stock": 150,
        "is_featured": False,
        "sort_order": 8,
    },
    {
        "slug": "bondage-set",
        "name": "Bondage Set",
        "name_zh": "束缚套装",
        "tagline": "Beginner Restraint Kit",
        "tagline_zh": "入门束缚套装",
        "description": "Explore new horizons with our premium beginner bondage set. Soft, comfortable, and adjustable - perfect for couples looking to spice things up.",
        "description_zh": "用我们的高级入门束缚套装探索新领域。柔软舒适，可调节——非常适合想要增添情趣的情侣。",
        "price": 69.99,
        "original_price": 89.99,
        "category_id": 10,
        "badge": "",
        "badge_zh": "",
        "colors": ["Red", "Black", "Purple"],
        "features": [
            "Soft fur-lined handcuffs",
            "Adjustable silk ties",
            "Blindfold & feather teaser",
            "Body-safe metal hardware",
            "Travel storage bag",
            "Beginner guide included"
        ],
        "features_zh": [
            "柔软毛绒手铐",
            "可调节丝绸绑带",
            "眼罩 & 羽毛挑逗棒",
            "身体安全金属配件",
            "旅行收纳袋",
            "包含入门指南"
        ],
        "weight": "350g",
        "dimensions": "Multiple pieces",
        "stock": 200,
        "is_featured": False,
        "sort_order": 9,
    },
    {
        "slug": "dual-density-dildo",
        "name": "Dual Density Dildo",
        "name_zh": "双层密度仿真阳具",
        "tagline": "Realistic Silicone",
        "tagline_zh": "逼真硅胶",
        "description": "Ultra-realistic dual-density silicone dildo. Soft outer layer with a firm core for the perfect balance of feel and function.",
        "description_zh": "超逼真双层密度硅胶仿真阳具。柔软外层 + 坚硬内核，完美平衡触感和功能。",
        "price": 54.99,
        "original_price": 74.99,
        "category_id": 8,
        "badge": "",
        "badge_zh": "",
        "colors": ["Flesh", "Clear", "Black"],
        "features": [
            "Dual-density silicone",
            "Realistic texture",
            "Strong suction cup base",
            "Harness compatible",
            "Body-safe & phthalate-free",
            "Waterproof & easy to clean"
        ],
        "features_zh": [
            "双层密度硅胶",
            "逼真纹理",
            "强力吸盘底座",
            "可穿戴式兼容",
            "身体安全 & 无邻苯二甲酸盐",
            "防水易清洁"
        ],
        "weight": "280g",
        "dimensions": "180 x 38mm",
        "stock": 180,
        "is_featured": False,
        "sort_order": 10,
    },
    {
        "slug": "anal-trainer-kit",
        "name": "Anal Trainer Kit",
        "name_zh": "后庭训练套装",
        "tagline": "Progressive Plug Set",
        "tagline_zh": "渐进式肛塞套装",
        "description": "Safe and comfortable anal training with our graduated plug set. Start small and progress at your own pace with silky smooth silicone.",
        "description_zh": "安全舒适的后庭训练，渐进式肛塞套装。丝滑硅胶，从小号开始，按自己的节奏进阶。",
        "price": 44.99,
        "original_price": 59.99,
        "category_id": 9,
        "badge": "",
        "badge_zh": "",
        "colors": ["Black", "Purple", "Pink"],
        "features": [
            "Set of 3 progressive sizes",
            "Tapered tip for easy insertion",
            "Wide safety base",
            "Medical-grade silicone",
            "Waterproof & easy to clean",
            "Storage pouch included"
        ],
        "features_zh": [
            "3个渐进尺寸套装",
            "锥形尖端易插入",
            "宽大安全底座",
            "医疗级硅胶",
            "防水易清洁",
            "包含收纳袋"
        ],
        "weight": "150g (set)",
        "dimensions": "Varies by size",
        "stock": 220,
        "is_featured": False,
        "sort_order": 11,
    },
    {
        "slug": "silk-glide",
        "name": "Silk Glide",
        "name_zh": "Silk 润滑液套装",
        "tagline": "Lubricant Collection",
        "tagline_zh": "润滑液系列",
        "description": "Premium intimate lubricants crafted with natural ingredients. Three formulas for every occasion: water-based, silicone-based, and warming.",
        "description_zh": "采用天然成分的高级私密润滑液。三种配方适合各种场合：水基、硅基和热感型。",
        "price": 29.99,
        "original_price": 39.99,
        "category_id": 11,
        "badge": "",
        "badge_zh": "",
        "colors": ["Original", "Warming", "Silicone"],
        "features": [
            "3 pack variety set",
            "Water, silicone & warming",
            "Body-safe & pH balanced",
            "Paraben & glycerin free",
            "Travel size bottles",
            "Compatible with toys"
        ],
        "features_zh": [
            "3瓶装组合",
            "水基、硅基 & 热感型",
            "身体安全 & pH平衡",
            "无对羟基苯甲酸酯 & 无甘油",
            "旅行装瓶子",
            "玩具兼容"
        ],
        "weight": "3 x 60ml",
        "dimensions": "3 bottles",
        "stock": 350,
        "is_featured": False,
        "sort_order": 12,
    },
]


def seed_database(db: Session):
    """Seed initial data into the database."""

    # Seed categories
    existing_categories = db.query(models.Category).count()
    if existing_categories == 0:
        for cat_data in CATEGORIES:
            cat = models.Category(**cat_data)
            db.add(cat)
        db.commit()
        print(f"Seeded {len(CATEGORIES)} categories")

    # Seed products
    existing_products = db.query(models.Product).count()
    if existing_products == 0:
        for prod_data in PRODUCTS:
            prod = models.Product(**prod_data)
            db.add(prod)
        db.commit()
        print(f"Seeded {len(PRODUCTS)} products")

    # Seed admin user
    admin = db.query(models.User).filter(
        models.User.email == "admin@lust8.com"
    ).first()
    if not admin:
        admin = models.User(
            email="admin@lust8.com",
            name="Admin",
            hashed_password=hash_password("admin123"),
            role=models.UserRole.ADMIN,
        )
        db.add(admin)
        db.commit()
        print("Seeded admin user (admin@lust8.com / admin123)")
