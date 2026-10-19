# LUST8 - Adult Pleasure Products E-commerce

海外成人用品独立站 - Premium adult pleasure products for global B2C & B2B customers.

## Project Structure

```
website/
├── front/          # Frontend (Vue 3 + Vite) - Deploy to Vercel
│   ├── src/
│   │   ├── views/          # Page components
│   │   ├── components/     # Reusable components
│   │   ├── router/         # Vue Router config
│   │   ├── data/           # Product & content data
│   │   ├── composables/    # Vue composables
│   │   ├── App.vue
│   │   ├── main.js
│   │   └── style.css       # Global styles & design tokens
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
│
└── backend/        # Backend API (to be built) - Deploy to Vercel
    ├── server.js          # Express server / Vercel functions
    └── package.json
```

## Design Reference

UI style inspired by Elev8 H2O (onepagelove showcase):
- Light pastel background with theme color switching (strawberry / pineapple / peach)
- Plaster display font + Outfit body font (via Google Fonts)
- Smooth scroll animations & hover effects
- Geometric decorative corner elements
- Gooey loader animation on page transition

## Pages & Routes

| Path | Page | Description |
|------|------|-------------|
| `/` | Home | Hero carousel, featured products, brand values, wholesale CTA, newsletter |
| `/products` | Products | Product catalog with category filters and sorting |
| `/products/:id` | Product Detail | Full product page with images, options, add to cart |
| `/wholesale` | Wholesale | B2B wholesale inquiry form with pricing tiers |
| `/cart` | Cart | *(coming soon)* |
| `/account` | Account | *(coming soon)* |

## Product Categories (12 SKUs)

| Category 品类 | Example Product 代表产品 |
|----------|----------------|
| Wand Massagers (AV震动棒) | Aura Wand - Luxury Body Massager |
| Rabbit Vibrators (兔子振动器) | Nocturne Rabbit - Dual Action Vibe |
| Clitoral Suction (吸吮器) | Halo - Air Pulse Stimulator |
| G-Spot Toys (G点棒) | Velvet Curve - G-Spot Vibrator |
| Kegel Balls (凯格尔球/缩阴球) | Luna Beads - Kegel Trainer Set |
| Couples Toys (情侣共用玩具) | Eclipse Duo - Couples Ring |
| Male Toys (男用飞机杯) | Titan Pro - Male Masturbator |
| Dildos (仿真阳具) | Dual Density Dildo - Realistic Silicone |
| Anal Toys (后庭玩具) | Anal Trainer Kit - Progressive Plug Set |
| Bondage (SM束缚套装) | Bondage Set - Beginner Restraint Kit |
| Accessories - 润滑剂 | Silk Glide - Lubricant Collection |
| Accessories - 按摩蜡烛 | Sensual Set - Massage Candle Collection |

## Development

### Frontend

**Install dependencies:**
```bash
cd front
npm install
```

**Start dev server:**
```bash
cd front
npm run dev
```
- Local: http://localhost:5173/
- Hot Module Replacement (HMR) enabled
- Press `Ctrl + C` to stop

**Build for production:**
```bash
cd front
npm run build
```
Output: `front/dist/`

**Preview production build:**
```bash
cd front
npm run preview
```

### Backend

(TBD - to be built with Node.js + Express / Vercel serverless functions)

## Deployment

Both front and backend deploy to **Vercel**.

- **Frontend**: Vue 3 + Vite → Vercel (static + edge functions)
- **Backend**: Serverless functions → Vercel (Node.js runtime)

## Commands Quick Reference

```bash
# Start frontend dev server
cd front && npm run dev

# Stop dev server
# Press Ctrl + C in the terminal

# Build production
cd front && npm run build
```
