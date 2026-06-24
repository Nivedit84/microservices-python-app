from tracemalloc import start

import pika, sys, os, time
from pymongo import MongoClient
import gridfs
from convert import to_mp3
from prometheus_client import start_http_server
from prometheus_client import (
    start_http_server,
    Counter,
    Gauge,
    Histogram
)

conversion_requests = Counter(
    "conversion_requests_total",
    "Total conversion requests",
    ["status"]
)

active_conversions = Gauge(
    "active_conversions",
    "Currently running conversions"
)

conversion_duration = Histogram(
    "conversion_duration_seconds",
    "Time taken for conversion"
)

def main():
    start_http_server(8000)
    client = MongoClient(os.environ.get('MONGODB_URI'))
    db_videos = client.videos
    db_mp3s = client.mp3s
    # gridfs
    fs_videos = gridfs.GridFS(db_videos)
    fs_mp3s = gridfs.GridFS(db_mp3s)

    # rabbitmq connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq',heartbeat=0)
    )
    channel = connection.channel()

    def callback(ch, method, properties, body):
        start = time.time()

        active_conversions.inc()

        try:

            err = to_mp3.start(
                body,
                fs_videos,
                fs_mp3s,
                ch
            )

            if err:

                conversion_requests.labels(
                    status="failed"
                ).inc()

                ch.basic_nack(
                    delivery_tag=method.delivery_tag
                )

            else:

                conversion_requests.labels(
                    status="success"
                ).inc()

                ch.basic_ack(
                    delivery_tag=method.delivery_tag
                )

        except Exception:

            conversion_requests.labels(
                status="failed"
            ).inc()

            raise

        finally:

            active_conversions.dec()

            conversion_duration.observe(
                time.time() - start
            )

        queue = channel.queue_declare(
        queue=os.environ.get("VIDEO_QUEUE"),
        passive=True
        )
        queue_depth = Gauge(
          "rabbitmq_queue_depth",
          "Current queue depth"
        )

        queue_depth.set(
          queue.method.message_count
        )

    channel.basic_consume(
        queue=os.environ.get("VIDEO_QUEUE"), on_message_callback=callback
    )

    print("Waitting for messages, to exit press CTRL+C")

    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
