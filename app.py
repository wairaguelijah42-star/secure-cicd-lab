import os

def main():
    secret = os.getenv("secret = "APP_SECRET")
    
    if secret:
        print(f"Secret loaded securely: {secret[:3]}***")
    else:
        print("No secret found")

if __name__ == "__main__":
    main()
