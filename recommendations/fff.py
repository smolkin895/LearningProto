import grpc

from recommendations_pb2 import RecommendationRequest, BookCategory
from recommendations_pb2_grpc import RecommendationsStub
channel = grpc.insecure_channel("localhost:50051")
client = RecommendationsStub(channel)
request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)
resp = client.Recommend(request)

print(resp)