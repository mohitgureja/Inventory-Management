# Inventory Management

## Overview
This project consists of a backend built using Python (FastAPI) and a frontend developed with Vue.js.

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- Node.js (LTS version recommended)
- npm or yarn

## Backend (FastAPI)

### Installation
1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Backend Server
1. Run the FastAPI server:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
2. API Documentation:
   - Open Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Open Redoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Frontend (Vue.js)

### Installation
1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```

### Running the Frontend Server
1. Start the development server:
   ```sh
   npm run serve
   ```
2. Open the application in your browser:
   ```sh
   http://localhost:8081
   ```

## Environment Variables
Ensure you configure environment variables for both the backend and frontend as needed. Typically, FastAPI uses a `.env` file inside backend directory.
Navigate to `frontend/src/stores/InventoryStore.js` if you wish to change the backend url. 



