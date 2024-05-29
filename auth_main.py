import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app="auth_page:app",
        host="localhost",
        port=8080,
        reload=True
    )
