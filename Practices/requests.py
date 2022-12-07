import requests


class RequestHandler:
    def __init__(self, url):
        self.url = url

    def get(self):
        return requests.get(self.url)

    def post(self, data):
        return requests.post(self.url, data)


# write a function that use function annotations to check if the input is a string and if the output is a list
def check_input_output(inputs: str) -> list:
    return [inputs]
