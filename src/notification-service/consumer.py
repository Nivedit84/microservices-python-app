import pika, sys, os
from send import email
from prometheus_client import Counter, start_http_server

messages_consumed = Counter(
    "notification_messages_consumed_total",
    "Total RabbitMQ messages consumed"
)

emails_sent = Counter(
    "notification_emails_sent_total",
    "Total emails sent successfully"
)

email_failures = Counter(
    "notification_email_failures_total",
    "Total failed email sends"
)

def main():
    start_http_server(8000)
    # rabbitmq connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq",heartbeat=0))
    channel = connection.channel()

    def callback(ch, method, properties, body):
          messages_consumed.inc()

          err = email.notification(body)

          if err:
            email_failures.inc()
            ch.basic_nack(delivery_tag=method.delivery_tag)
          else:
            emails_sent.inc()
            ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue=os.environ.get("MP3_QUEUE"), on_message_callback=callback
    )

    print("Waiting for messages. To exit press CTRL+C")

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