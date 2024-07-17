import uvicorn

def main():
    uvicorn.run("routes:app", host="0.0.0.0", port=80, log_level="debug", reload=True)

if __name__ == "__main__":
    main()
