import requests

def main():
    print("Codex starter activo.")
    response = requests.get("https://httpbin.org/get")
    if response.status_code == 200:
        print("Respuesta OK:")
        print(response.json())
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    main()
