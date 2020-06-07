from flask import request, g, jsonify
from . import api
from .utils import validate_license
import time
from multiprocessing import Pool
from app import db

from ..models import MetricData


@api.route('/metrics', methods=['POST'])
@validate_license
def create_metric_data():
    received_at = time.time()
    sec = int(received_at)
    m_sec = int(received_at * 1000)
    if sec % 2 == 0 and m_sec % 1000 < 250:
        __process_data(request.json, g.account_id, sec)
        return jsonify({"received": True, "processed": True})
    else:
        return jsonify({"received": True, "processed": False})


def __process_data(json_map, account_id, m_sec):
    chunks = __create_chunks(json_map, 5, account_id, m_sec)
    pool = Pool(5)
    pool.map(__save_data_point, chunks)
    pool.close()
    pool.join()


def __create_chunks(json_map, chunk_size, account_id, m_sec):
    items = list(json_map.items())
    chunks = [(items[i:i + chunk_size], account_id, m_sec) for i in range(0, len(items), chunk_size)]
    return chunks


def __save_data_point(chunk):
    account_id, ts = chunk[1], chunk[2]
    for tup in chunk[0]:
        data_point = MetricData(metric_name=tup[0], metric_value=tup[1], account_id=account_id, timestamp=ts)
        # Send to kafka Here
        db.session.add(data_point)
        db.session.commit()
