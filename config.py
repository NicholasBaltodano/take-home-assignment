from enum import Enum
import data_service as ds


class MetricName(str, Enum):
    btcusd = "btcusd"
    bntbtc = "bntbtc"
    cbceth = "cbceth"



metric_list = []
metric_list.append(ds.Metric("Kraken", "BTCUSD"))
metric_list.append(ds.Metric("Kraken", "BNTBTC"))
metric_list.append(ds.Metric("HITBTC","CBCETH"))
