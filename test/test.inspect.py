import importlib.util
import inspect
import os

def import_and_inspect(file_path):

    file_name = os.path.basename(file_path)
    module_name = os.path.splitext(file_name)[0]
    spec = importlib.util.spec_from_file_location(module_name, file_path)

    # 动态导入模块
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # 获取模块中所有的函数
    functions = inspect.getmembers(module, inspect.isfunction)

    # 打印每个函数的名称和参数
    for name, func in functions:
        if name == 'main':
            print(f"函数名称: {name}")
            params = inspect.signature(func).parameters
            for param_name, param in params.items():
                print(f"参数名称: {param_name}, 类型: {param.annotation}")


# 使用这个函数来导入和检查你的Python文件
import_and_inspect('/Users/chen_yiru/Desktop/chen yiru MacBook Air/simple-pyper/example_pipeline/plus_test.py')