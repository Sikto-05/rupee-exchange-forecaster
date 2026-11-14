# 🪙 RupeeVision — AI Currency Exchange Forecaster

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Framework: Flask](https://img.shields.io/badge/framework-Flask-green.svg)](https://flask.palletsprojects.com/)
[![Live Demo](https://img.shields.io/badge/Live_Demo-Cloudflare_Tunnel-orange.svg)](https://authentication-lighter-vii-therefore.trycloudflare.com)

> **RupeeVision** is a financial intelligence and currency forecasting web platform. It analyzes **10 years of daily macroeconomic data (2,600+ trading days)** from the European Central Bank (ECB) to compute real-time cross-currency rates and forecast **3–4 day forward trajectories** for the US Dollar (USD/INR) and 15 world currencies against the Indian Rupee (INR).

---

## 🌟 Key Features

- **Single-Input Cross-Rate Engine:** Insert the day's US Dollar rate (USD/INR) to instantly derive equilibrium valuations in Indian Rupees for 15 world currencies.
- **✨ 10-Year AI Dollar Predictor:** Dedicated machine learning pipeline specifically analyzing 10 years of USD/INR market trends to predict today's rate and forward 4-day outlook with 90% confidence corridors.
- **Ensemble Forecasting Architecture:** Combines multi-lag autoregressive Ridge Regression ($\text{Lags}_{1..10}$, $\text{MA}_5$, $\text{MA}_{20}$, $\text{MA}_{50}$, Rolling Volatility, DOW Seasonality) with Exponential Weighted Moving Average (EWMA) momentum drift.
- **Brownian Diffusion Confidence Envelopes:** Real-time upper and lower limits scaling with $\sqrt{t}$ based on historical volatility.
- **Fintech Glassmorphism Dashboard:** Built in a deep navy and electric gold theme with interactive Chart.js graphs (1M, 3M, 6M, 1Y, 5Y, 10Y), real-time sparklines, sortable tables, and one-click CSV export.

---

## 🧮 Mathematical Formulation

### 1. Cross-Rate Determination
For any target world currency $C$, the exchange rate against the Indian Rupee is calculated via the vehicle US Dollar relation:

$$\text{Rate}(C \to \text{INR}) = \frac{\text{Rate}(\text{USD} \to \text{INR})}{\text{Rate}(\text{USD} \to C)}$$

### 2. Forward Trajectory & Uncertainty Corridor
For each forecast step $d \in \{1, 2, 3, 4\}$ trading days ahead:

$$R_{t+d} = R_{t+d-1} \cdot (1 + \hat{r}_d)$$

$$\text{Upper}_d = R_{t+d} + R_{t+d} \cdot (z_{0.90} \cdot \sigma_{\text{daily}} \cdot \sqrt{d})$$

$$\text{Lower}_d = R_{t+d} - R_{t+d} \cdot (z_{0.90} \cdot \sigma_{\text{daily}} \cdot \sqrt{d})$$

---

## 🌍 Supported Currencies (15 Pairs)

| Currency | Code | Country / Region | Peg / Valuation |
|:---:|:---:|:---|:---:|
| 🇺🇸 | **USD** | United States | Free Floating (10-Yr Model) |
| 🇪🇺 | **EUR** | European Union | Free Floating |
| 🇬🇧 | **GBP** | United Kingdom | Free Floating |
| 🇯🇵 | **JPY** | Japan | Free Floating |
| 🇦🇺 | **AUD** | Australia | Free Floating |
| 🇨🇦 | **CAD** | Canada | Free Floating |
| 🇨🇭 | **CHF** | Switzerland | Free Floating |
| 🇸🇬 | **SGD** | Singapore | Free Floating |
| 🇦🇪 | **AED** | United Arab Emirates | Pegged ($3.6725 / \text{USD}$) |
| 🇸🇦 | **SAR** | Saudi Arabia | Pegged ($3.7500 / \text{USD}$) |
| 🇨🇳 | **CNY** | China | Free Floating |
| 🇹🇭 | **THB** | Thailand | Free Floating |
| 🇲🇾 | **MYR** | Malaysia | Free Floating |
| 🇳🇿 | **NZD** | New Zealand | Free Floating |
| 🇰🇷 | **KRW** | South Korea | Free Floating |

---

## 🚀 Quick Start

### 1. Clone & Set Up Virtual Environment
```bash
git clone <your-repo-url>
cd rupee-exchange-forecaster
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```
Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📡 REST API Endpoints

- `GET /api/dollar-prediction` — Fetches 10-year USD/INR statistical analysis, equilibrium rate, and 4-day forward trajectory.
- `POST /api/calculate` — Accepts `{"usd_inr_rate": 84.50}` and returns cross-rates and 4-day forecasts for all 15 currencies.
- `GET /api/historical/<currency>?period=1Y&usd_inr=84.50` — Returns downsampled historical time-series data for charting.
- `GET /health` — Status and engine metadata.

---

## 📄 License
This project is licensed under the MIT License.
