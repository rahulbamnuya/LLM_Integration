from pinecone import Pinecone, ServerlessSpec

# Initialize Pinecone client with API key
pc = Pinecone(api_key="your-api-key-here")  # Replace with your Pinecone API Key

# Print connection status and existing indexes
print("Pinecone client initialized:", pc)
print("📦 Existing Indexes:", pc.list_indexes())

# ---------- (Run once only to create index) ----------
# Create a new index with dimension = 8
# pc.create_index(
#     name="test-index",
#     dimension=8,
#     metric="euclidean",
#     spec=ServerlessSpec(cloud="aws", region="us-east-1")
# )

# ---------- Describe an index ----------
# print("ℹ️  Index Description:", pc.describe_index("test-index"))

# ---------- Connect to an existing index ----------
index = pc.Index("test-index")

# ---------- Upsert vectors ----------
# vectors = [
#     {"id": "vec1", "values": [0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]},
#     {"id": "vec2", "values": [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]}
# ]
# index.upsert(vectors=vectors, namespace="ns1")

# More sample vectors (run once)
# vectors = [
#     {"id": "vec3", "values": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]},
#     {"id": "vec4", "values": [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]},
#     {"id": "vec5", "values": [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75]},
#     {"id": "vec6", "values": [0.99, 0.88, 0.77, 0.66, 0.55, 0.44, 0.33, 0.22]}
# ]
# index.upsert(vectors=vectors, namespace="ns2")

# ---------- Fetch specific vectors ----------
# result = index.fetch(["vec1", "vec2"], namespace="ns1")
# print("🔍 Fetch result:", result)

# ---------- Update vector values ----------
# index.update(id="vec1", values=[2.2, 4.4, 8.8, 2.2, 9.9, 3.3, 5.5, 6.6], namespace="ns1")

# ---------- Update metadata ----------
# index.update(id="vec2", set_metadata={"type": "website", "new": True}, namespace="ns1")

# ---------- Delete vectors ----------
# index.delete(ids=["vec1", "vec2"], namespace="ns1")

# ---------- Delete all vectors in a namespace ----------
# index.delete(delete_all=True, namespace="ns1")

# ---------- Delete the index itself ----------
# Be careful! This deletes the index permanently
# pc.delete_index("test-index")
