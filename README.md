# FastAPI Project

## Setup

### 1. Install Prerequisites

```bash
# Install Conda
# Install Python 3.9.6
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
touch .env
```

Add the following to `.env`:

```
SQLALCHEMY_DATABASE_URL=your_database_url_here
```

### 5. Run the Application

```bash
fastapi dev main.py
```
