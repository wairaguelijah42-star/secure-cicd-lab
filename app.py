import os

def main():
    secret = os.getenv("secret = "APP_SECRET")
    
    if secret:
        print(f"Secret loaded securely")
    else:
        print("No secret found")

if __name__ == "__main__":
    main()
