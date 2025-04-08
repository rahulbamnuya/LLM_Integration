📁 Project Structure
Copy
Edit
PineconeDB_vector/
│
├── app.py
├── README.md
└── requirements.txt
✅ 1. app.py
python
Copy
Edit
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
📝 2. README.md
markdown
Copy
Edit
# 🧠 Pinecone Vector DB with Python

This project demonstrates how to use [Pinecone](https://www.pinecone.io/) to create, insert, update, query, and delete vector data using Python.

---

## 📦 Features

- ✅ Connect to Pinecone with API key
- 📌 Create and list indexes
- 📤 Upsert (insert/update) vectors with values
- 🔍 Fetch vectors by ID
- ✏️ Update vector values and metadata
- 🗑️ Delete vectors or entire index
- 📂 Work within namespaces

---

## 📁 File Structure

```bash
PineconeDB_vector/
├── app.py              # Python script for all operations
├── README.md           # This file
└── requirements.txt    # Python dependencies
🔧 Installation & Setup
Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/PineconeDB_vector.git
cd PineconeDB_vector
Step 2: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 3: Add Your Pinecone API Key
Open app.py and replace this line:

python
Copy
Edit
pc = Pinecone(api_key="your-api-key-here")
with your actual Pinecone API key.

Step 4: Run the Script
bash
Copy
Edit
python app.py
Uncomment the parts you want to test (create index, upsert, fetch, etc.).

🧠 Example Vector Format
python
Copy
Edit
{
  "id": "vec1",
  "values": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
}
🚀 Quick Command Reference
Task	Command
List Indexes	pc.list_indexes()
Create Index	pc.create_index(...)
Connect to Index	pc.Index("test-index")
Upsert Vectors	index.upsert([...], namespace="ns1")
Fetch Vectors	index.fetch(["vec1"], namespace="ns1")
Update Vector Values	index.update(id="vec1", values=[...])
Update Metadata	index.update(id="vec1", set_metadata={...})
Delete Vectors	index.delete(ids=["vec1"], namespace="ns1")
Delete Namespace	index.delete(delete_all=True, namespace="ns1")
Delete Index	pc.delete_index("test-index")
📃 License
MIT License

✨ Author
Developed by Your Name

yaml
Copy
Edit

---

## 📦 3. `requirements.txt`

```txt
pinecone-client>=3.0.0
🧾 Final Notes
To push to GitHub:

bash
Copy
Edit
git init
git add .
git commit -m "Initial Pinecone VectorDB project"
git branch -M main
git remote add origin https://github.com/your-username/PineconeDB_vector.git
git push -u origin main
Would you like a downloadable .zip with all files?