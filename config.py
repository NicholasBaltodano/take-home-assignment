from enum import Enum
import data_service as ds


hour_look_back = 24


metric_wait_interval = 60
ranking_wait_interval = 86400

#TODO create this dynamically
class MetricName(str, Enum):
    btcusd = "btcusd"
    bntbtc = "bntbtc"
    cbceth = "cbceth"

metric_list = []
metric_list.append(ds.Metric("Kraken", "BTCUSD"))
metric_list.append(ds.Metric("Kraken", "BNTBTC"))
metric_list.append(ds.Metric("HITBTC","CBCETH"))
