"""
app.py — RupeeVision AI Exchange Rate Forecaster Web Service
=============================================================
Provides REST endpoints and interactive visual dashboard
for rupee currency cross-rate calculations, 10-year macroeconomic
analysis, and 4-day AI forward forecasts for USD and 15 world currencies.
"""

import os
import logging
from datetime import datetime

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

import data_manager
import forecaster
import geopolitical_news

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

_historical_df = None


def get_df():
    global _historical_df
    if _historical_df is None:
        _historical_df = data_manager.fetch_historical_data()
    return _historical_df


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/currencies", methods=["GET"])
def currencies():
    return jsonify({"currencies": data_manager.get_currencies_list()})


@app.route("/api/geopolitical-news", methods=["GET"])
def geopolitical_news_feed():
    """Returns real-time world politics landscape and currency drivers."""
    return jsonify({
        "status": "success",
        "global_landscape": geopolitical_news.get_geopolitical_summary(),
        "drivers": geopolitical_news.CURRENCY_GEOPOLITICAL_DRIVERS,
    })


@app.route("/api/dollar-prediction", methods=["GET"])
def dollar_prediction():
    """
    Dedicated endpoint to predict the USD/INR rate for today and the
    next 3-4 days based strictly on 10 years of historical data analysis.
    Query parameters (optional):
      - base_rate: float (if user wants to anchor from a specific dollar rate)
      - days: int (default 4)
    """
    days = request.args.get("days", default=4, type=int)
    base_rate = request.args.get("base_rate", default=None, type=float)

    if days < 1 or days > 14:
        days = 4

    df = get_df()
    try:
        prediction = forecaster.predict_dollar_rate(df, days=days, base_rate=base_rate)
        return jsonify(prediction)
    except Exception as exc:
        logger.exception("Dollar prediction failed")
        return jsonify({"error": f"Dollar prediction failed: {str(exc)}"}), 500


@app.route("/api/calculate", methods=["POST"])
def calculate():
    """
    Calculate cross rates and forward forecasts for all currencies
    given today's USD/INR rate.
    """
    body = request.get_json(silent=True) or {}
    usd_inr = body.get("usd_inr_rate")

    if usd_inr is None:
        return jsonify({"error": "Please provide a 'usd_inr_rate' value."}), 400

    try:
        usd_inr = float(usd_inr)
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid rate. Please enter a valid number."}), 400

    if not (20.0 <= usd_inr <= 300.0):
        return jsonify({"error": "Rate out of expected range (20 to 300 INR/USD)."}), 400

    df = get_df()

    try:
        cross_rates = data_manager.get_cross_rates(usd_inr, df)
        forecast_results = forecaster.forecast_all_currencies(df, usd_inr, days=4)
        dollar_forecast = forecaster.predict_dollar_rate(df, days=4, base_rate=usd_inr)

        return jsonify({
            "status": "success",
            "usd_inr_rate": usd_inr,
            "timestamp": datetime.now().isoformat(),
            "dollar_forecast": dollar_forecast,
            "cross_rates": cross_rates,
            "forecasts": forecast_results,
            "currencies_count": len(forecast_results),
            "historical_data_years": 10,
            "global_geopolitics": geopolitical_news.get_geopolitical_summary(),
        })
    except Exception as exc:
        logger.exception("Calculation error")
        return jsonify({"error": f"Calculation failed: {str(exc)}"}), 500


@app.route("/api/historical/<currency>", methods=["GET"])
def historical(currency: str):
    currency = currency.upper().strip()
    period = request.args.get("period", "1Y").upper()
    current_usd_inr = request.args.get("usd_inr", type=float)

    if currency not in data_manager.CURRENCIES:
        return jsonify({"error": f"Currency '{currency}' not supported."}), 404

    df = get_df()
    chart_data = data_manager.get_historical_for_chart(df, currency, period, current_usd_inr)

    return jsonify({
        "currency": currency,
        "period": period,
        "data": chart_data,
        "count": len(chart_data),
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "currencies_supported": len(data_manager.CURRENCIES),
        "historical_engine": "10-Year ECB Frankfurter API (2016-2026)",
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    logger.info("Starting RupeeVision on http://0.0.0.0:%d", port)
    get_df()
    app.run(host="0.0.0.0", port=port, debug=False)
