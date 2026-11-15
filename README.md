# 🪙 RupeeVision — AI Currency Exchange Forecaster

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Framework: Flask](https://img.shields.io/badge/framework-Flask-green.svg)](https://flask.palletsprojects.com/)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Live_Portal-blue.svg)](https://sikto-05.github.io/rupee-exchange-forecaster/)

> **RupeeVision** is a financial intelligence and foreign exchange forecasting web platform. It analyzes **10 years of daily macroeconomic data (2,600+ trading days)** from the European Central Bank (ECB) and regional central banks to compute real-time cross-currency rates and forecast **3–4 day forward trajectories** for the US Dollar (USD/INR), **India's neighbouring countries**, and major global vehicle currencies against the Indian Rupee (INR).

---

## 🌟 Key Features

- **Single-Input Cross-Rate Engine:** Simply input today's US Dollar rate (USD/INR) to instantly derive equilibrium valuations in Indian Rupees for **23 currencies**.
- **🌍 Current World Politics & Breaking News Synthesis:** The next 4-day forecasts dynamically factor in live geopolitical catalysts, central bank policy divergence (US Fed, ECB, BoJ, PBOC), Middle East energy/crude shipping security, trade tariff policies, and regional South Asian developments (Bangladesh interim stability, Pakistan IMF review, Sri Lanka debt accords, India-Maldives currency swaps).
- **🇮🇳 India's Neighbours Coverage:** Full support for India's immediate neighbouring economies — Bangladesh (BDT), Pakistan (PKR), Nepal (NPR), Sri Lanka (LKR), Bhutan (BTN), Myanmar (MMK), Afghanistan (AFN), Maldives (MVR), and China (CNY) with official peg handling (NPR 1.60 peg, BTN 1:1 parity).
- **📊 10-Year AI Forward Trajectory for Dollar & All Currencies:** Forward 4-day econometric outlook with 90% Brownian confidence corridors, geopolitical volatility scalers ($\kappa_{\text{geo}}$), and momentum indicators.
- **Ensemble Forecasting Architecture:** Combines multi-lag autoregressive Ridge Regression ($\text{Lags}_{1..10}$, $\text{MA}_5$, $\text{MA}_{20}$, $\text{MA}_{50}$, Rolling Volatility, DOW Seasonality) with Exponential Weighted Moving Average (EWMA) momentum drift and geopolitical news sentiment.
- **Dual Deployment Ready:** Seamlessly works with the Python/Flask backend and standalone as an interactive static web portal on **GitHub Pages**.
- **Fintech Glassmorphism Dashboard:** Built in a deep navy and electric gold theme with interactive Chart.js graphs (1M, 3M, 6M, 1Y, 5Y, 10Y), real-time sparklines, category filters, a live Geopolitical News Intelligence Terminal, sortable tables, and one-click CSV export.

---

## 🧮 Mathematical Formulation

### 1. Cross-Rate Determination
For any target world currency $C$, the exchange rate against the Indian Rupee is calculated via the vehicle US Dollar relation:

$$\text{Rate}(C \to \text{INR}) = \frac{\text{Rate}(\text{USD} \to \text{INR})}{\text{Rate}(\text{USD} \to C)}$$

For pegged currencies (e.g. Bhutanese Ngultrum BTN at 1:1, Nepalese Rupee NPR at 1.60 per INR), the official parity is strictly preserved.

### 2. Forward Trajectory with Geopolitical News Drift
For each forecast step $d \in \{1, 2, 3, 4\}$ trading days ahead:

$$R_{t+d} = R_{t+d-1} \cdot (1 + \hat{r}_d)$$

Where predicted return $\hat{r}_d$ synthesizes 10-year quantitative momentum with geopolitical news drift ($\delta_{\text{geo}}$):

$$\hat{r}_d = \hat{r}_{\text{quant}} \cdot e^{-0.25(d-1)} + \delta_{\text{geo}} + \epsilon_{\text{shock}}$$

$$\text{Upper}_d = R_{t+d} + R_{t+d} \cdot (z_{0.90} \cdot \sigma_{\text{daily}} \cdot \kappa_{\text{geo}} \cdot \sqrt{d})$$

$$\text{Lower}_d = R_{t+d} - R_{t+d} \cdot (z_{0.90} \cdot \sigma_{\text{daily}} \cdot \kappa_{\text{geo}} \cdot \sqrt{d})$$

---

## 🌍 Supported Currencies (23 Pairs)

### 🇮🇳 India's Immediate Neighbours (9 Currencies)
| Flag | Code | Country | Currency | Valuation / Peg Status |
|:---:|:---:|:---|:---|:---:|
| 🇧🇩 | **BDT** | Bangladesh | Bangladeshi Taka | Free Floating |
| 🇵🇰 | **PKR** | Pakistan | Pakistani Rupee | Free Floating |
| 🇳🇵 | **NPR** | Nepal | Nepalese Rupee | Fixed Peg (1 INR = 1.60 NPR / 1 NPR = 0.625 INR) |
| 🇱🇰 | **LKR** | Sri Lanka | Sri Lankan Rupee | Free Floating |
| 🇧🇹 | **BTN** | Bhutan | Bhutanese Ngultrum | Fixed At Par (1 BTN = 1 INR) |
| 🇲🇲 | **MMK** | Myanmar | Myanmar Kyat | Free Floating |
| 🇦🇫 | **AFN** | Afghanistan | Afghan Afghani | Free Floating |
| 🇲🇻 | **MVR** | Maldives | Maldivian Rufiyaa | Pegged ($15.42 / \text{USD}$) |
| 🇨🇳 | **CNY** | China | Chinese Yuan | Managed Float |

### 🌐 Major Global Currencies (14 Currencies)
| Flag | Code | Country / Region | Currency | Valuation / Peg Status |
|:---:|:---:|:---|:---|:---:|
| 🇺🇸 | **USD** | United States | US Dollar | Vehicle Anchor Currency |
| 🇪🇺 | **EUR** | European Union | Euro | Free Floating |
| 🇬🇧 | **GBP** | United Kingdom | British Pound | Free Floating |
| 🇯🇵 | **JPY** | Japan | Japanese Yen | Free Floating |
| 🇦🇺 | **AUD** | Australia | Australian Dollar | Free Floating |
| 🇨🇦 | **CAD** | Canada | Canadian Dollar | Free Floating |
| 🇨🇭 | **CHF** | Switzerland | Swiss Franc | Free Floating |
| 🇸🇬 | **SGD** | Singapore | Singapore Dollar | Managed Float |
| 🇦🇪 | **AED** | United Arab Emirates | UAE Dirham | Pegged ($3.6725 / \text{USD}$) |
| 🇸🇦 | **SAR** | Saudi Arabia | Saudi Riyal | Pegged ($3.7500 / \text{USD}$) |
| 🇹🇭 | **THB** | Thailand | Thai Baht | Free Floating |
| 🇲🇾 | **MYR** | Malaysia | Malaysian Ringgit | Free Floating |
| 🇳🇿 | **NZD** | New Zealand | New Zealand Dollar | Free Floating |
| 🇰🇷 | **KRW** | South Korea | South Korean Won | Free Floating |

---

## 🚀 Quick Start

### 1. Clone & Set Up Virtual Environment
```bash
git clone https://github.com/Sikto-05/rupee-exchange-forecaster.git
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

- `POST /api/calculate` — Accepts `{"usd_inr_rate": 84.50}` and returns cross-rates and 4-day forecasts synthesized with geopolitical drift for all 23 currencies.
- `GET /api/geopolitical-news` — Fetches real-time world politics landscape, global risk indices, and currency-specific news catalysts.
- `GET /api/dollar-prediction` — Fetches 10-year USD/INR statistical analysis, equilibrium rate, and 4-day forward trajectory.
- `GET /api/historical/<currency>?period=1Y&usd_inr=84.50` — Returns downsampled historical time-series data for charting.
- `GET /health` — Status and engine metadata.

---

## 📄 License
This project is licensed under the MIT License.
