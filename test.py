import requests
import json
from sandbox_fusion import run_code, RunCodeRequest


print("hello world")
# Using default retry count (5 times)
# run_code(RunCodeRequest(code='print("Hello World")', language='python'))

response = run_code(RunCodeRequest(code='print("Hello World")', language='python'))
print(json.dumps(response.json(), indent=2))

# import requests
# import json

# response = requests.post('http://localhost:8080/run_code', json={
#     'code': '''
# #include <iostream>

# int main() {
#     std::cout << 2 + 233 + 235 << std::endl;
#     return 0;
# }
# ''',
#     'language': 'cpp',
# })

# print(json.dumps(response.json(), indent=2))