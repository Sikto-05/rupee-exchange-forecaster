"""
geopolitical_news.py — World Politics & Current News Intelligence Engine
========================================================================
Synthesizes current geopolitical developments, trade policies, central bank
decisions, and regional South Asian news to parameterize the 4-day currency
forecasting model with real-world geopolitical drift and volatility factors.
"""

from datetime import datetime

# ── Overall Global Geopolitical Landscape Assessment ─────────────────────────
GLOBAL_GEOPOLITICAL_LANDSCAPE = {
    "last_updated": "November 2026",
    "global_risk_index": "Moderate-Elevated",
    "primary_macro_drivers": [
        {
            "topic": "US Monetary Policy & Dollar Yields",
            "tag": "US Fed",
            "sentiment": "USD Bullish",
            "summary": "Cautious Federal Reserve rate-cut trajectory and elevated US Treasury yields sustain strong structural demand for the US Dollar across international clearing corridors.",
        },
        {
            "topic": "Global Trade Policies & Tariff Rhetoric",
            "tag": "Trade / Tariffs",
            "sentiment": "Cautious",
            "summary": "Heightened trade protectionism discussions and proposed tariffs on export-dependent economies induce periodic defensive positioning in Asian and European currencies.",
        },
        {
            "topic": "Middle East Energy Security & Crude Oil",
            "tag": "Energy / Crude",
            "sentiment": "Inflationary Risk",
            "summary": "Strait of Hormuz and Red Sea shipping route watchfulness keeps Brent crude volatile, directly impacting net energy-importing economies including India.",
        },
        {
            "topic": "South Asian Regional Stabilization & Alliances",
            "tag": "South Asia",
            "sentiment": "Constructive",
            "summary": "Bilateral currency swap pacts (RBI-Maldives), robust Nepal-Bhutan energy grids, and IMF stabilization programs in Pakistan and Sri Lanka buffer regional contagion.",
        },
    ],
}

# ── Currency-Specific Geopolitical & Current News Drivers ─────────────────────
CURRENCY_GEOPOLITICAL_DRIVERS = {
    # ── Immediate Neighbours of India ──────────────────────────────────────────
    "BDT": {
        "headline": "Interim Government Reforms & Garment Export Revival Stabilize Forex",
        "political_driver": "Bangladesh Bank under interim administration exercises targeted reserve sterilization; steady European apparel order flows and Middle East remittances offset bi-monthly Asian Clearing Union (ACU) settlements, maintaining forex buffers near $31B-$33B.",
        "risk_level": "Moderate",
        "impact_bias": "Consolidation (Neutral-Stable)",
        "daily_geo_drift": 0.0002,
        "geo_volatility_mult": 1.05,
        "four_day_news_impact": "Day 1-2: Steady liquidity post-export proceeds realization; Day 3-4: Controlled crawl-managed band holds BDT/INR in a tight consolidation channel.",
    },
    "PKR": {
        "headline": "IMF 24-Month EFF Review & Bilateral Gulf Loan Rollovers Anchor Liquidity",
        "political_driver": "Pakistan's ongoing IMF program benchmarks, cooling domestic inflation, and confirmed rollover of $12B+ in bilateral deposits from Saudi Arabia and UAE keep the rupee steady despite regional geopolitical monitoring along western frontiers.",
        "risk_level": "Elevated",
        "impact_bias": "Range-Bound with Softening Bias",
        "daily_geo_drift": -0.0004,
        "geo_volatility_mult": 1.15,
        "four_day_news_impact": "Day 1-2: Moderate dollar demand for debt servicing; Day 3-4: Remittance inflows cushion daily volatility, keeping PKR/INR range-bound around ₹0.30.",
    },
    "NPR": {
        "headline": "Nepal-India Bilateral Hydro Power Exports & Robust Remittance Inflows Fortify 1.60 Peg",
        "political_driver": "Nepal Rastra Bank strictly maintains the statutory 1.60 INR fixed peg (1 NPR = 0.625 INR). Multi-year clean electricity export contracts with India and remittances accounting for >25% of GDP guarantee zero deviation from official parity.",
        "risk_level": "Low",
        "impact_bias": "Strict Fixed Peg (0% Volatility)",
        "daily_geo_drift": 0.0000,
        "geo_volatility_mult": 1.00,
        "four_day_news_impact": "Day 1-4: The 1.60 peg is legally and structurally invariant against the Indian Rupee. Rates remain exactly constant at ₹0.6250 across all forecast sessions.",
    },
    "LKR": {
        "headline": "Post-Election Debt Restructuring Accords & Tourism Influx Surge Rebuild Central Bank Reserves",
        "political_driver": "Sri Lanka's sovereign debt normalization under IMF governance, Paris Club approvals, and record peak-season winter tourist arrivals strengthen CBSL foreign reserves, reducing reliance on emergency spot dollar purchases.",
        "risk_level": "Moderate",
        "impact_bias": "Constructive / Modest Firming",
        "daily_geo_drift": 0.0003,
        "geo_volatility_mult": 1.08,
        "four_day_news_impact": "Day 1-2: Strong tourism FX conversions support LKR; Day 3-4: External debt repayment schedule keeps central bank cautious, maintaining steady trading near ₹0.28.",
    },
    "BTN": {
        "headline": "India-Bhutan Hydropower Integration & Bilateral Treaty Ensure Absolute 1:1 Parity",
        "political_driver": "The Royal Monetary Authority of Bhutan operates under bilateral treaty guaranteeing 1:1 parity with the Indian Rupee. Cross-border electricity sales from Tala and Punatsangchhu hydro projects provide continuous INR clearing reserves.",
        "risk_level": "Low",
        "impact_bias": "Statutory 1:1 Parity (Zero Risk)",
        "daily_geo_drift": 0.0000,
        "geo_volatility_mult": 1.00,
        "four_day_news_impact": "Day 1-4: Exact 1.0000 INR parity maintained with zero exchange rate uncertainty and zero volatility.",
    },
    "MMK": {
        "headline": "Border Post Trade Friction & Central Bank Foreign Exchange Rationing",
        "political_driver": "Domestic political developments and border checkpoint logistics in northern/western corridors prompt tight foreign currency rationing by the Central Bank of Myanmar; cross-border rupee trade remains confined to authorized banking channels.",
        "risk_level": "Elevated",
        "impact_bias": "Defensive / Wider Corridor",
        "daily_geo_drift": -0.0005,
        "geo_volatility_mult": 1.20,
        "four_day_news_impact": "Day 1-2: Cautious cross-border settlement volumes; Day 3-4: Wider confidence corridor reflects geopolitical risk premium along overland corridors.",
    },
    "AFN": {
        "headline": "Da Afghanistan Bank Weekly Currency Sterilization Auctions Maintain Relative Calm",
        "political_driver": "Da Afghanistan Bank conducts regular USD auction tranches to absorb surplus domestic currency; informal transit trade with South Asian economies and humanitarian aid transfers sustain baseline Afghani liquidity.",
        "risk_level": "Elevated",
        "impact_bias": "Neutral Range",
        "daily_geo_drift": 0.0001,
        "geo_volatility_mult": 1.12,
        "four_day_news_impact": "Day 1-2: Dollar auction supply balances domestic market needs; Day 3-4: Controlled trading corridor between ₹1.24 and ₹1.28 holds.",
    },
    "MVR": {
        "headline": "India-Maldives $400M Bilateral Currency Swap & Resort Tourism High-Season",
        "political_driver": "Reserve Bank of India (RBI) currency swap facility provides emergency liquidity support; peak luxury European and Asian tourist bookings bolster foreign currency inflows, ensuring the 15.42 MVR per USD peg remains rock solid.",
        "risk_level": "Low-Moderate",
        "impact_bias": "Pegged to USD Anchor",
        "daily_geo_drift": 0.0001,
        "geo_volatility_mult": 1.02,
        "four_day_news_impact": "Day 1-4: Cross-rate strictly tracks USD/INR divided by 15.42. Steady tourism revenue ensures seamless currency availability.",
    },
    "CNY": {
        "headline": "PBOC Counter-Cyclical Daily Fixings Counteract Potential US Tariff Escalations",
        "political_driver": "The People's Bank of China sets firm daily midpoint fixings to prevent speculative yuan depreciation amidst US trade tariff rhetoric; domestic monetary stimulus measures inject targeted manufacturing liquidity.",
        "risk_level": "Moderate",
        "impact_bias": "Managed Float / Stable",
        "daily_geo_drift": 0.0001,
        "geo_volatility_mult": 1.06,
        "four_day_news_impact": "Day 1-2: PBOC fixing anchors offshore CNH; Day 3-4: Regional Asian currency stability preserves CNY/INR within an orderly ₹11.60-₹11.85 band.",
    },

    # ── Major Global Vehicle Currencies ────────────────────────────────────────
    "USD": {
        "headline": "US Federal Reserve Interest Rate Stance & Flight-to-Safety Demand Bolster Greenback",
        "political_driver": "US Federal Reserve signals deliberate pacing on interest rate cuts due to resilient domestic consumer data; elevated Treasury yields and Middle East energy supply vigilance drive institutional safe-haven dollar accumulation; RBI spot interventions manage excessive volatility.",
        "risk_level": "Moderate",
        "impact_bias": "Bullish Dollar Drift",
        "daily_geo_drift": 0.0005,
        "geo_volatility_mult": 1.10,
        "four_day_news_impact": "Day 1-2: Upward pressure supported by DXY strength; Day 3-4: RBI smoothing operations temper spike risks, consolidating rate within 90% confidence corridor.",
    },
    "EUR": {
        "headline": "ECB Monetary Easing Cycle & German Industrial Slowdown Dampen Euro Momentum",
        "political_driver": "European Central Bank leans toward further monetary accommodation amidst sluggish manufacturing data across major eurozone hubs and structural energy cost headwinds; capital reallocates toward dollar-denominated assets.",
        "risk_level": "Moderate",
        "impact_bias": "Mild Bearish Softening",
        "daily_geo_drift": -0.0003,
        "geo_volatility_mult": 1.08,
        "four_day_news_impact": "Day 1-2: ECB dovish remarks weigh on euro upside; Day 3-4: Cross-hedging against dollar strength keeps EUR/INR trading near lower-middle band.",
    },
    "GBP": {
        "headline": "Bank of England Balances Autumn Budget Fiscal Tightrope Against Sticky Services Inflation",
        "political_driver": "UK fiscal policy targets and public borrowing caps limit aggressive growth stimulus; Bank of England proceeds with data-dependent monetary adjustments while sterling reacts to broader risk-off geopolitical sentiment.",
        "risk_level": "Moderate",
        "impact_bias": "Range-Bound Consolidation",
        "daily_geo_drift": 0.0001,
        "geo_volatility_mult": 1.07,
        "four_day_news_impact": "Day 1-2: Inflation print expectations anchor sterling; Day 3-4: Sideways drift as UK bond yields consolidate against US Treasuries.",
    },
    "JPY": {
        "headline": "Bank of Japan Rate Normalization Stance vs. Global Carry-Trade Liquidity Unwinds",
        "political_driver": "Bank of Japan reiterates commitment to gradual rate hikes if wage-price cycle solidifies, but high sensitivity to global market volatility and US yield differentials generates periodic carry-trade liquidation waves.",
        "risk_level": "Elevated",
        "impact_bias": "High Beta / Volatile",
        "daily_geo_drift": 0.0004,
        "geo_volatility_mult": 1.25,
        "four_day_news_impact": "Day 1-2: Japanese institutional repatriation flows support yen; Day 3-4: Global yield differentials limit sustained breakouts, maintaining dynamic oscillation.",
    },
    "AED": {
        "headline": "OPEC+ Energy Strategy & UAE Sovereign Diversification Underpin 3.6725 Peg",
        "political_driver": "UAE Dirham remains formally pegged to the USD at 3.6725. Non-oil trade expansion, AI infrastructure investments, and massive sovereign wealth fund reserves make AED an exceptionally stable proxy for vehicle currency transactions.",
        "risk_level": "Low",
        "impact_bias": "USD Anchor Tracking",
        "daily_geo_drift": 0.0005,
        "geo_volatility_mult": 1.00,
        "four_day_news_impact": "Day 1-4: Trajectory matches USD/INR divided by 3.6725. Sovereign fiscal surpluses eliminate domestic credit risk.",
    },
    "SAR": {
        "headline": "Saudi Vision 2030 Capital Expenditure & Petrodollar Parity Shield Riyal",
        "political_driver": "Saudi Central Bank (SAMA) preserves the unshakeable 3.7500 SAR peg to the US Dollar; strategic crude production quotas defend fiscal revenue baselines, ensuring seamless convertibility.",
        "risk_level": "Low",
        "impact_bias": "USD Anchor Tracking",
        "daily_geo_drift": 0.0005,
        "geo_volatility_mult": 1.00,
        "four_day_news_impact": "Day 1-4: Exact USD cross-rate parity maintained at 3.7500 SAR per USD across the entire forecast window.",
    },
    "SGD": {
        "headline": "Monetary Authority of Singapore (MAS) Tight Exchange Rate Policy Band Holds Strong",
        "political_driver": "MAS maintains an appreciating NEER policy band to combat imported inflation, reinforcing Singapore's standing as Asia's premier financial safe-haven hub amid regional geopolitical uncertainty.",
        "risk_level": "Low",
        "impact_bias": "Resilient Firming",
        "daily_geo_drift": 0.0002,
        "geo_volatility_mult": 1.04,
        "four_day_news_impact": "Day 1-2: Institutional wealth inflows support SGD strength; Day 3-4: Orderly tracking against Asian basket with minimal downside volatility.",
    },
    "AUD": {
        "headline": "China Stimulus Expectations & Commodity Export Pricing Drive Aussie Dollar",
        "political_driver": "Reserve Bank of Australia (RBA) maintains a cautious monetary stance; iron ore and LNG export demand from China acts as primary barometer, leaving the Aussie sensitive to Asian growth metrics.",
        "risk_level": "Moderate",
        "impact_bias": "Commodity-Linked Swings",
        "daily_geo_drift": 0.0001,
        "geo_volatility_mult": 1.12,
        "four_day_news_impact": "Day 1-2: Chinese industrial policy headlines dictate direction; Day 3-4: Balanced momentum against Indian Rupee with healthy two-way trading.",
    },
    "CAD": {
        "headline": "Bank of Canada Accommodative Easing & Energy Export Realignment",
        "political_driver": "Bank of Canada accelerates interest rate normalization to counter domestic housing and consumer deceleration; North American energy pipeline flows cushion the Loonie against deeper pullbacks.",
        "risk_level": "Moderate",
        "impact_bias": "Mild Softening Bias",
        "daily_geo_drift": -0.0002,
        "geo_volatility_mult": 1.09,
        "four_day_news_impact": "Day 1-2: Rate differential headwinds vs US Dollar; Day 3-4: Canadian crude differentials stabilize CAD/INR within a predictable channel.",
    },
    "CHF": {
        "headline": "Swiss National Bank Navigates Global Safe-Haven Franc Inflows",
        "political_driver": "Swiss Franc continues to attract European capital flight during periods of geopolitical tension in Ukraine and the Middle East; Swiss National Bank monitors real effective exchange rate to curb excessive export headwinds.",
        "risk_level": "Low",
        "impact_bias": "Strong Safe-Haven Support",
        "daily_geo_drift": 0.0003,
        "geo_volatility_mult": 1.05,
        "four_day_news_impact": "Day 1-2: Geopolitical risk hedges favor franc accumulation; Day 3-4: High structural valuation against INR maintained.",
    },
    "THB": {
        "headline": "Tourism High Season & Bank of Thailand Fiscal Stimulus Package",
        "political_driver": "Thailand's peak international travel arrivals and government digital wallet stimulus distributions stimulate internal consumption, offsetting regional trade headwinds.",
        "risk_level": "Moderate",
        "impact_bias": "Moderate Recovery",
        "daily_geo_drift": 0.0002,
        "geo_volatility_mult": 1.10,
        "four_day_news_impact": "Day 1-2: Tourism receipts bolster commercial bank foreign exchange sales; Day 3-4: Steady cross-rate stabilization against INR.",
    },
    "MYR": {
        "headline": "Semiconductor Investment Boom & Bank Negara Malaysia Policy Stability",
        "political_driver": "Malaysia benefits from global AI hardware and chip packaging supply chain diversification into Penang and Johor; Bank Negara maintains steady benchmark rates to support ringgit stability.",
        "risk_level": "Moderate",
        "impact_bias": "Bullish Tech-Driven Support",
        "daily_geo_drift": 0.0003,
        "geo_volatility_mult": 1.07,
        "four_day_news_impact": "Day 1-2: High FDI conversion into local assets; Day 3-4: Ringgit maintains favorable momentum against regional peers.",
    },
    "NZD": {
        "headline": "Reserve Bank of New Zealand Rate Reductions & Agricultural Export Demand",
        "political_driver": "RBNZ continues an aggressive monetary easing path to stimulate economic recovery; dairy and agricultural export prices provide a floor to the Kiwi dollar.",
        "risk_level": "Moderate",
        "impact_bias": "Dovish Pressure",
        "daily_geo_drift": -0.0003,
        "geo_volatility_mult": 1.14,
        "four_day_news_impact": "Day 1-2: RBNZ policy rate drag; Day 3-4: Commodity support arrests extended depreciation.",
    },
    "KRW": {
        "headline": "Global AI Semiconductor Demand & Chip Export Surge Counter Trade Headwinds",
        "political_driver": "South Korean electronics and high-bandwidth memory (HBM) chip exports to global tech giants generate strong corporate earnings, mitigating domestic political friction and consumer softness.",
        "risk_level": "Moderate",
        "impact_bias": "Tech Cycle Support",
        "daily_geo_drift": 0.0002,
        "geo_volatility_mult": 1.11,
        "four_day_news_impact": "Day 1-2: Tech export earnings support KRW conversion; Day 3-4: Moderate sideways trading against INR.",
    },
}


def get_geopolitical_summary() -> dict:
    """Return top-level global political news intelligence."""
    return GLOBAL_GEOPOLITICAL_LANDSCAPE


def get_currency_driver(currency_code: str) -> dict:
    """Return specific geopolitical intelligence and news for a currency."""
    code = currency_code.upper().strip()
    return CURRENCY_GEOPOLITICAL_DRIVERS.get(
        code,
        {
            "headline": "Global Foreign Exchange Macroeconomic Balance",
            "political_driver": "Standard international cross-border trade flows and central bank liquidity management.",
            "risk_level": "Moderate",
            "impact_bias": "Neutral",
            "daily_geo_drift": 0.0,
            "geo_volatility_mult": 1.05,
            "four_day_news_impact": "Day 1-4: Follows standard macroeconomic drift within expected volatility bounds.",
        },
    )
