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
├── app.py               # Python script for all Pinecone operations
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```


---

## 🔧 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/PineconeDB_vector.git
cd PineconeDB_vector
```
### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```
### Step 3: Add Your Pinecone API Key

```bash
pc = Pinecone(api_key="your-api-key-here")

```
### Step 4: Run the Script

```bash
python app.py

```
## 🧠 Example Vector Format
```bash
{
  "id": "vec1",
  "values": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
}
```
## 🚀 Quick Command Reference

| Task                   | Command                                               |
|------------------------|--------------------------------------------------------|
| **List Indexes**       | `pc.list_indexes()`                                    |
| **Create Index**       | `pc.create_index(...)`                                 |
| **Connect to Index**   | `pc.Index("test-index")`                               |
| **Upsert Vectors**     | `index.upsert([...], namespace="ns1")`                |
| **Fetch Vectors**      | `index.fetch(["vec1"], namespace="ns1")`              |
| **Update Vector Values** | `index.update(id="vec1", values=[...])`            |
| **Update Metadata**    | `index.update(id="vec1", set_metadata={...})`         |
| **Delete Vectors**     | `index.delete(ids=["vec1"], namespace="ns1")`         |
| **Delete Namespace**   | `index.delete(delete_all=True, namespace="ns1")`      |
| **Delete Index**       | `pc.delete_index("test-index")`                       |

