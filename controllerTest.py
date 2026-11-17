# 创建 HTTP 接口服务
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/print_params', methods=['GET', 'POST'])
def print_params():
    """打印接口传入的参数"""
    print("=" * 50)
    print("收到请求参数:")

    # 获取 GET 参数
    if request.args:
        print("GET 参数:")
        for key, value in request.args.items():
            print(f"  {key}: {value}")

    # 获取 POST 参数（JSON 格式）
    if request.is_json:
        data = request.get_json()
        print("POST JSON 参数:")
        for key, value in data.items():
            print(f"  {key}: {value}")
    elif request.form:
        print("POST 表单参数:")
        for key, value in request.form.items():
            print(f"  {key}: {value}")

    print("=" * 50)

    return jsonify({
        "message": "参数已打印到控制台",
        "params": {
            "get": dict(request.args),
            "json": request.get_json() if request.is_json else None,
            "form": dict(request.form) if request.form else None
        }
    })


if __name__ == '__main__':
    # 启动服务
    print("服务启动中...")
    print("访问地址：http://localhost:5000/api/print_params")
    print("示例：http://localhost:5000/api/print_params?name=张三&age=25")
    app.run(debug=True, port=5000)
