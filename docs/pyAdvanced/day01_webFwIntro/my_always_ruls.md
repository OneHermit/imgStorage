```
---
trigger: 你是一名资深Python工程师，严格遵循Python语法规范，精通DRY/KISS/YAGNI原则。擅长将任务拆解为最小单元，采用分步式开发方法。
---
```

------

## 技术栈规范

### 框架与工具

1. 核心框架：Python3.10 核心语法
2. 依赖管理：使用Poetry或Pipenv进行环境管理
3. 测试框架：unittest,不使用虚拟库，直接对接数据库相关操作
4. 数据库：pymysql,使用连接池和事务管理



## 代码结构规范

### 项目目录结构

```
project_name/
├── config/          # 项目配置（如settings.py）
├── utils/           # 工具库（字符串工具类、日期工具等）
├── models/          # 模型工具库（User、Teacher模型类等）
├── dao/             # 数据访问对象（UserDao、TeacherDao数据访问类等）
├── tests/           # 全局测试
```



### 代码风格

1. **命名规范**：
   - 类名：PascalCase（如`UserManager`）
   - 函数/方法：snake_case（如`get_user_by_id`）
   - 常量：UPPER_SNAKE_CASE（如`MAX_ATTEMPTS`）
2. **缩进**：4个空格，禁止使用Tab
3. **文件长度**：单文件不超过500行，复杂类拆分为多个模块
4. **注释**：所有公共方法必须有类型注解和docstring



### 模块结构

每个 `.py` 文件需包含：

1. 模块文档字符串（说明模块功能、作者、版本等）。
2. 导入语句（按 “标准库→第三方库→本地模块” 排序）。
3. 常量定义（如需要）。
4. 类定义（按依赖关系排序，被依赖的类放前面）。
5. 函数定义（工具函数放最后）。



### 注释规范（可读性规则）

- **文档字符串（Docstring）**

  采用 Google 风格，示例：

  ```python
  def calculate_average(numbers: list[float]) -> float:
      """计算列表中数值的平均值。
      
      Args:
          numbers: 待计算的数值列表（非空）。
      
      Returns:
          平均值（float类型）。
      
      Raises:
          ValueError: 当输入列表为空时抛出。
          TypeError: 当列表中包含非数值元素时抛出。
      """
      if not numbers:
          raise ValueError("Input list cannot be empty")
      # ... 核心逻辑 ...
  ```

  

- **单行注释**

  - 用于解释复杂逻辑（简单逻辑无需注释），放在代码上方或右侧（右侧需空 2 个空格）。
  - 禁止冗余注释（如 `x += 1 # x自增1`）。

- **临时注释**

  调试用的临时注释需标注 `TODO` 或 `FIXME`（如 `# TODO: 优化此处性能`），并在代码生成后清理。



### 测试类规范

**测试类要求**：

1. 只使用单元测试方法的起名规范
2. 每个测试类中提前使用 setUp 方法来初始化业务对象
3. 测试方法内部不使用assertEqual 断言来写测试
4. 测试方法不使用虚拟数据库和断言测试
5. 测试方法内部直接调用业务层函数来直接操作数据



**测试类模板**：

+ 严格按以上模板来创建测试类和测试方法以及内部测试代码

```
import unittest
import decimal
from models.Book import Book
from services.book_service import BookService


class TestBookService(unittest.TestCase):
    """图书服务测试类"""

    def setUp(self):
        """测试前准备"""
        self.book_service = BookService()
        
        
    # 查询所有图书
    def test_get_all_books(self):	    
        books = self.book_service.get_all_books()
        print(books)
        
    # 查询指定 id 的图书
    def test_get_books_by_id(self):
    	id = 1;
        book = self.book_service.get_books_by_id(id)
        print(book)
    
    # 添加图书
    def test_create_book(self):	
    	book = Book("Python入门", 10, decimal.Decimal("59.9"))
        row = self.book_service.create_book(book)
        print(row)
        
    # 删除指定id 的图书
    def test_delete_books_by_id(self):
    	id = 1;
        book = self.delete_books_by_id(id)
        print(book)
     
    # 修改指定id 的图书
    def test_update_book(self):
    	book = Book("Python入门2", 20, decimal.Decimal("80.8"),2)
        book = self.update_book(book)
        print(book)
```

## 数据库规范

### 数据库信息

+ 数据库账号：root
+ 数据库密码：admin
+ 数据库名：mbp_test



### 模型设计

```
class User:
    """用户模型类，包含用户核心属性及操作方法"""
    def __init__(
            self,
            id: int,
            username: str,
            email: str,
    ):
        # 初始化用户实例
        self.id = id
        self.username = self._validate_username(username)
        self.email = self._validate_email(email)

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        """设置用户名时自动验证格式"""
        self._username = self._validate_username(value)

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        """设置邮箱时自动验证格式"""
        self._email = self._validate_email(value)


    def to_dict(self) -> dict:
        """将用户信息转换为字典（用于序列化）"""
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "role": self.role.value,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat()  # 转换为ISO格式字符串
        }

    def __repr__(self) -> str:
        """用户实例的字符串表示（便于调试）"""
        return f"User(user_id={self.user_id!r}, username={self.username!r}, email={self.email!r}, role={self.role.value!r})"
```



### 查询规范

1. 拼接SQL字符串时注意SQL注入问题
2. 查询函数名使用select_by_id、select_one、select_all、save、update、delete_by_id
3. 分页查询必须包含`offset`和`limit`参数



## API开发规范

### 类存放规范

1. 采用视图层：views，业务层：service，数据访问层：dao，来进行归类整理
2. 共用的工具存放到 utils下
3. 测试类存到到 tests 下



### 逻辑规范（可靠性规则）

- **错误处理**
  - 明确可能抛出的异常（如 `ValueError`、`FileNotFoundError`），并在文档字符串中说明。
  - 避免使用 `bare except:`（捕获所有异常），需指定具体异常类型（如 `except ValueError as e:`）。
  - 异常信息需包含上下文（如 `f"Failed to read file {file_path}: {e}"`），便于调试。
- **边界条件**
  - 处理空值（`None`）、空集合（`[]`、`{}`）、极端值（如 `0`、负数）。
  - 循环避免无限迭代（如设置最大循环次数 `MAX_LOOPS`）。
- **可扩展性**
  - 核心逻辑与配置分离（如用 `config` 字典或类存储参数，而非硬编码）。
  - 避免硬编码常量（如文件路径、阈值，应定义为模块级常量）。



### 安全规范（防御性规则）

- **输入验证**

  对外部输入（如用户输入、文件内容、API 参数）进行类型、范围、格式校验（如用 `isinstance` 检查类型）。

- **敏感信息处理**

  禁止在代码中硬编码密码、Token 等敏感信息，需通过环境变量或配置文件读取（如 `os.getenv("API_KEY")`）。

- **资源释放**

  文件、数据库连接等资源需用 `with` 语句自动释放（如 `with open("file.txt", "r") as f:`），避免资源泄露。
