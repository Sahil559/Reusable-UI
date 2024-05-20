import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app="webapp.auth.auth_page.main:app",
        host="localhost",
        port=8000,
        reload=True
    )
