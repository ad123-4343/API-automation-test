import pytest
import requests
import yaml

# 1. 读取 YAML 题库
with open("test_cases.yaml", "r", encoding="utf-8") as f:
    TEST_CASES = yaml.safe_load(f)


# 2. 封装发请求的“跑腿工具”
def send_request(method, url, payload=None):
    print(f"\n正在发送 {method} 请求到: {url}")
    if method.upper() == "GET":
        response = requests.get(url, timeout=30)
    elif method.upper() == "POST":
        response = requests.post(url, json=payload, timeout=30)
    else:
        pytest.fail(f"❌ 暂不支持 {method} 方法")

    return response


# 3. 流水线自动循环 + 多维度断言
@pytest.mark.parametrize("case", TEST_CASES, ids=[c["name"] for c in TEST_CASES])
def test_restful_api(case):
    # 叫跑腿的去干活
    response = send_request(case["method"], case["url"], case.get("payload"))

    # ================= 开始断言 =================

    # 【状态码断言】
    assert response.status_code == case["expected_status"], \
        f"❌ 状态码错误！期望 {case['expected_status']}，实际 {response.status_code}"

    # 【JSON 内容断言】（查一下返回的数据对不对）
    if "expected_json" in case:
        res_data = response.json()
        for key, expected_value in case["expected_json"].items():
            assert res_data.get(key) == expected_value, \
                f"❌ 字段校验失败！期望 {key}='{expected_value}'，实际='{res_data.get(key)}'"

    print("✅ 该用例测试通过！")