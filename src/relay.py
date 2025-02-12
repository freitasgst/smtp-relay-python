import requests


def relayer_setup(secrets_file: str) -> str:
    with open(secrets_file) as file:
        secrets_list = file.read().splitlines()
        for secrets_line in secrets_list:
            secret_parts = secrets_line.split("=", 1)
            if secret_parts[0] == "GCHAT_API":
                api = secret_parts[1]
    return api


def body_composer(message: str) -> dict[str, str]:
    body = {"text": message}
    return body


def make_requests(api: str, body: dict[str, str]) -> int:
    response = requests.post(
        url = api,
        json = body
    )
    return response.status_code


def main():  # pragma: no cover
    src = input("Digite o nome do arquivo com a API: ")
    if src == "/":
        src = "api.txt"
    url = relayer_setup(src)

    msgm = input("Digite abaixo a mensagem: \n")
    body = body_composer(msgm)
    resp = make_requests(url, body)

    print("STATUS CODE DA MENSAGEM:", resp)


if __name__ == "__main__":  # pragma: no cover
    main()
