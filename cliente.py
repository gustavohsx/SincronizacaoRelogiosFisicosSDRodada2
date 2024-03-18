import grpc
import time
import clock_sync_pb2
import clock_sync_pb2_grpc
import logging
import random

logging.basicConfig(level=logging.INFO)

def run_client():
    channel = grpc.insecure_channel("localhost:50051")
    stub = clock_sync_pb2_grpc.ClockSyncStub(channel)

    response = stub.GetTime(clock_sync_pb2.TimeRequest(client_time=(int(time.time() * 1000) + random.randint(10000, 20000))))
    server_time = response.server_time
    adjustment = response.adjustment
    adjusted_time = server_time + adjustment
    logging.info(f"Server time: {server_time}, Adjustment: {adjustment}, Adjusted time: {adjusted_time}")

    for response in stub.GetTimeStream(clock_sync_pb2.TimeRequest(client_time=(int(time.time() * 1000) + random.randint(10000, 20000)))):
        server_time = response.server_time
        adjustment = response.adjustment
        adjusted_time = server_time + adjustment
        logging.info(f"Server time: {server_time}, Adjustment: {adjustment}, Adjusted time: {adjusted_time}")

if __name__ == "__main__":
    run_client()
