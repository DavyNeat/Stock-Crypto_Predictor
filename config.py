import numpy as np
import pandas as pd
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries 

key_file = open("key.txt", "r")
key = key_file.read()
config = {
    "alpha_vantage": {
        "key": key, 
        "symbol": ["IBM", "GOOG", "NFLX", "AMZN", "AAPL", "MSFT", "TSLA", "NVDA", "ADBE", "INTC"],
        "outputsize": "full",
        "key_adjusted_close": "5. adjusted close",
    },
    "data": {
        "window_size": 40,
        "train_split_size": 0.70,
    }, 
    "plots": {
        "xticks_interval": 90, # show a date every 90 days
        "color_actual": "#001f3f",
        "color_train": "#3D9970",
        "color_val": "#0074D9",
        "color_pred_train": "#3D9970",
        "color_pred_val": "#0074D9",
        "color_pred_test": "#FF4136",
    },
    "model": {
        "input_size": 11, # since we are only using 1 feature, close price
        "num_lstm_layers": 2,
        "lstm_size": 32,
        "dropout": 0.2,
    },
    "training": {
        "device": "cpu", # "cuda" or "cpu"
        "batch_size": 64,
        "num_epoch": 100,
        "learning_rate": 0.01,
        "scheduler_step_size": 40,
        "n_past": 30,
        "n_future": 20,
    }
}