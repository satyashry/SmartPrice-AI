# 🧠 SmartPrice AI
### AI-Powered Laptop Price Intelligence Engine

> Predicts fair market prices for laptops based on specs — trained on real Flipkart data scraped from scratch.

🔗 **Live Demo:** [smartprice-ai-fm1f.onrender.com](https://smartprice-ai-fm1f.onrender.com)

---

## What is this?

SmartPrice AI is an end-to-end machine learning project that:
1. **Scrapes real laptop listings** from Flipkart using Selenium
2. **Cleans and engineers features** from raw product names using regex
3. **Trains 6 ML models** and picks the best one automatically
4. **Deploys as a live web app** where users enter specs and get a predicted price

No Kaggle datasets. No tutorials. Built from scratch.

---

## Project Structure

```
SmartPrice-AI/
├── src/
│   ├── components/
│   │   ├── data_ingestion.py        # loads CSV, splits train/test
│   │   ├── data_transformation.py   # encodes + scales features
│   │   └── model_trainer.py         # trains 6 models, saves best
│   ├── pipeline/
│   │   ├── predict_pipeline.py      # loads model, predicts from input
│   │   └── train_pipeline.py        # runs full training pipeline
│   ├── exception.py                 # custom exception handler
│   ├── logger.py                    # logging setup
│   └── utils.py                     # save/load model, evaluate models
├── notebook/
│   ├── data/
│   │   ├── raw/laptops_raw.csv           # scraped data (984 rows)
│   │   └── processed/laptops_cleaned.csv # cleaned data (614 rows)
│   ├── data_cleaning.ipynb               # cleaning notebook
│   └── eda/data_visual.ipynb             # EDA + visualisations
├── scraper/
│   └── flipkart_scraper.py          # Selenium + BS4 scraper
├── artifacts/
│   ├── model.pkl                    # trained model
│   ├── preprocessor.pkl             # fitted transformer
│   ├── train.csv
│   └── test.csv
├── app.py                           # Streamlit web app
├── render.yaml                      # Render deployment config
├── requirements.txt
└── README.md
```

---

## How It Works

### Step 1 — Web Scraping
- Selenium controls a real Chrome browser
- BeautifulSoup parses the HTML
- Scraped 984 products across 90 Flipkart pages
- Extracted: product name, original price, current price

### Step 2 — Feature Engineering
Raw product name:
```
HP Victus AMD Ryzen 7 - (24 GB/1 TB SSD/Windows 11/8 GB NVIDIA)
```
Extracted using regex:

| Feature | Value |
|---------|-------|
| `brand` | HP |
| `ram` | 24 GB |
| `storage` | 1024 GB |
| `processor` | AMD Ryzen 7 |
| `graphics` | 8 GB Graphics |
| `os` | Windows 11 |

### Step 3 — Model Training
6 models trained with GridSearchCV hyperparameter tuning:

| Model | R² Score | MAE |
|-------|----------|-----|
| Linear Regression | 0.442 | ₹15,855 |
| Ridge | 0.441 | ₹15,847 |
| KNN | 0.678 | ₹7,996 |
| XGBoost | 0.724 | ₹7,435 |
| Gradient Boosting | 0.712 | ₹7,658 |
| **Random Forest** ✅ | **0.743** | **₹6,768** |

Best model selected and saved automatically.

### Step 4 — Deployment
- UI built with **Streamlit**
- Deployed on **Render**

---

## Key EDA Insights

- RAM is the strongest predictor of laptop price
- Budget laptops (₹25k–₹50k) get higher discounts (60–90%)
- Premium laptops (₹1L+) hold their price
- Storage has lower correlation with price than RAM

---

## Tech Stack

| Layer | Tools |
|-------|-------|
| Scraping | Selenium, BeautifulSoup4 |
| Data | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| ML | Scikit-learn, XGBoost, GridSearchCV |
| App | Streamlit |
| Deployment | Render |

---

## Run Locally

```bash
git clone https://github.com/yourusername/smartprice-ai.git
cd smartprice-ai
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/pipeline/train_pipeline.py
streamlit run app.py
```

---

## Roadmap

- [x] Laptop price prediction
- [x] Live deployment
- [ ] Smartphone price prediction
- [ ] Smartwatch price prediction
- [ ] SHAP explainability in UI
- [ ] Multi-category home page

---

## What I Learned

- Scraping real websites with Selenium + BeautifulSoup
- Extracting structured features from messy text using regex
- Building production ML pipelines with proper exception handling
- Training and comparing multiple models automatically
- Deploying a live ML app end to end

---

> *"No Kaggle. No tutorials. Real data, real code, built from scratch in 4 days."*
