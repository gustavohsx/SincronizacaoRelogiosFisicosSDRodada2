import grpc
import time
import clock_sync_pb2
import clock_sync_pb2_grpc
import concurrent.futures
import logging

logging.basicConfig(level=logging.INFO)

class ClockSyncServicer(clock_sync_pb2_grpc.ClockSyncServicer):
    def __init__(self):
        self.client_times = {}

    def GetTime(self, request, context):
        client_id = context.peer()
        server_time = int(time.time() * 1000) + 10000

        if client_id not in self.client_times:
            self.client_times[client_id] = []

        self.client_times[client_id].append(request.client_time)

        adjustment = self.calculate_adjustment(client_id)

        logging.info(f"Client {client_id} adjusted by {adjustment} milliseconds")

        return clock_sync_pb2.TimeResponse(server_time=int(time.time() * 1000), adjustment=adjustment)

    def GetTimeStream(self, request, context):
        client_id = context.peer()

        while True:
            server_time = int(time.time() * 1000) + 10000
            adjustment = self.calculate_adjustment(client_id)
            yield clock_sync_pb2.TimeResponse(server_time=int(time.time() * 1000), adjustment=adjustment)
            time.sleep(1)

    def calculate_adjustment(self, client_id):

        client_time_avg = sum(self.client_times[client_id]) / len(self.client_times[client_id])
        server_time = int(time.time() * 1000) + 10000
        server_time_avg = sum([server_time - client_time for client_time in self.client_times[client_id]]) / len(self.client_times[client_id])
        # return int(server_time_avg - client_time_avg)
        return int(server_time - client_time_avg)

def run_server():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    clock_sync_pb2_grpc.add_ClockSyncServicer_to_server(ClockSyncServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    run_server()
