from app.sift_app import get_sift_app
import redis
import argparse

if __name__=="__main__":

    app = get_sift_app(config)
    redis_connection = redis.Redis(connection_pool=app.pool)
    redis_connection.flushall()
    app.raun(host='0.0.0.0', port=int(args.port))
