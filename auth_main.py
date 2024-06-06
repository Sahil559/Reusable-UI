import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app="webapp/auth/auth_page:app",
        host="localhost",
        port=8080,
        reload=True
    )
