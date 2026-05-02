🧠 SmartPrice AI — Laptop Price Intelligence Engine
Predicts fair market laptop prices from specs alone — trained on real Flipkart data scraped from scratch. No Kaggle. No shortcuts.
🔗 Live Demo: smartprice-ai-fm1f.onrender.com

🎯 What is this?
SmartPrice AI is a full end-to-end ML project built in 4 days from zero:

🕷️ Scrapes real Flipkart listings using Selenium — no pre-made datasets
🧹 Cleans & engineers features from raw messy product names using regex
🤖 Trains 6 ML models with GridSearchCV and auto-selects the best
🚀 Deployed live as a web app anyone can use right now


📁 Project Structure
SmartPrice-AI/
│
├── 📂 src/
│   ├── 📂 components/
│   │   ├── data_ingestion.py        ← loads CSV, creates train/test split
│   │   ├── data_transformation.py   ← encodes categories, scales features
│   │   └── model_trainer.py         ← trains 6 models, saves the best
│   │
│   ├── 📂 pipeline/
│   │   ├── predict_pipeline.py      ← loads model + preprocessor, predicts
│   │   └── train_pipeline.py        ← runs full pipeline in one command
│   │
│   ├── exception.py                 ← custom exception handler
│   ├── logger.py                    ← logging
│   └── utils.py                     ← save/load model, evaluate models
│
├── 📂 scraper/
│   └── flipkart_scraper.py          ← Selenium + BeautifulSoup scraper
│
├── 📂 notebook/
│   ├── 📂 data/
│   │   ├── raw/laptops_raw.csv           ← 984 scraped rows
│   │   └── processed/laptops_cleaned.csv ← 614 clean rows
│   ├── data_cleaning.ipynb               ← cleaning + feature extraction
│   └── eda/data_visual.ipynb             ← charts + insights
│
├── 📂 artifacts/
│   ├── model.pkl          ← trained Random Forest model
│   ├── preprocessor.pkl   ← fitted OrdinalEncoder + StandardScaler
│   ├── train.csv
│   └── test.csv
│
├── app.py              ← Streamlit web app
├── render.yaml         ← Render deployment config
├── requirements.txt
└── README.md

⚙️ How It Works
🕷️ Step 1 — Web Scraping

Selenium opens a real Chrome browser and navigates Flipkart
BeautifulSoup parses the HTML and extracts product data
Scraped 984 laptops across 90 pages
Collected: product name, original price, current price

🧹 Step 2 — Feature Engineering
Raw product name from Flipkart:
HP Victus AMD Ryzen 7 - (24 GB/1 TB SSD/Windows 11/8 GB NVIDIA)
Extracted using regex into clean ML features:
FeatureExtractedbrandHPram24 GBstorage1024 GBprocessorAMD Ryzen 7graphics8 GB GraphicsosWindows 11
🤖 Step 3 — Model Training
╔══════════════════════════════════════════════════════════╗
║              MODEL COMPARISON RESULTS                    ║
╠═══════════════════════╦══════════╦══════════╦═══════════╣
║ Model                 ║ R² Score ║ MAE      ║ RMSE      ║
╠═══════════════════════╬══════════╬══════════╬═══════════╣
║ Linear Regression     ║  0.442   ║ ₹15,855  ║ ₹20,276   ║
║ Ridge                 ║  0.441   ║ ₹15,847  ║ ₹20,279   ║
║ KNN                   ║  0.678   ║  ₹7,996  ║ ₹15,393   ║
║ XGBoost               ║  0.724   ║  ₹7,435  ║ ₹14,247   ║
║ Gradient Boosting     ║  0.712   ║  ₹7,658  ║ ₹14,553   ║
║ ✅ Random Forest      ║  0.743   ║  ₹6,768  ║ ₹13,747   ║  ← BEST
╚═══════════════════════╩══════════╩══════════╩═══════════╝
  Predicts from: RAM · Processor · Storage · Brand · OS · GPU
🚀 Step 4 — Deployment

UI built with Streamlit
Deployed on Render with render.yaml


📊 Key EDA Insights

💡 RAM is the #1 price driver — strongest correlation with price
💸 Budget laptops (₹25k–₹50k) get aggressive discounts of 60–90%
🏷️ Premium laptops (₹1L+) hold their MRP with under 20% discount
💾 Storage has weaker price correlation than RAM
🍎 Apple 24GB outlier (₹2.1L) kept — it's real premium pricing


🛠️ Tech Stack
LayerTools🕷️ ScrapingSelenium, BeautifulSoup4, fake-useragent🧹 DataPandas, NumPy, Regex📊 VisualisationMatplotlib, Seaborn🤖 MLScikit-learn, XGBoost, GridSearchCV🖥️ AppStreamlit☁️ DeployRender

🚀 Run Locally
bash# Clone
git clone https://github.com/yourusername/smartprice-ai.git
cd smartprice-ai

# Setup
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
pip install -r requirements.txt

# Train
python src/pipeline/train_pipeline.py

# Run app
streamlit run app.py

🗺️ Roadmap

 ✅ Laptop price prediction
 ✅ Live deployment on Render


🧠 What I Learned

Building a real web scraper with Selenium + BeautifulSoup from scratch
Extracting structured features from messy text using regex
Writing production-grade ML pipelines with proper exception handling & logging
Training and auto-comparing multiple models with GridSearchCV
Deploying a live ML app end to end



💬 "No Kaggle datasets. No copy-paste tutorials. Real data scraped by hand, cleaned from scratch, and deployed live — built in 5 days."
