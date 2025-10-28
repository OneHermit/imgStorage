import decimal


class Book:
    """图书模型类，包含图书核心属性及操作方法"""
    def __init__(
            self,
            name: str,
            num: int,
            price: decimal.Decimal,
            id = None,
    ):
        # 初始化图书实例
        self.id = id
        self.name = name
        self.num = num
        self.price = price

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int) -> None:
        """设置图书ID"""
        self._id = value

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        """设置图书名称"""
        self._name = value

    @property
    def num(self) -> int:
        return self._num
    
    @num.setter
    def num(self, value: int) -> None:
        """设置图书数量"""
        self._num = value

    @property
    def price(self) -> decimal.Decimal:
        return self._price
    
    @price.setter
    def price(self, value: decimal.Decimal) -> None:
        """设置图书价格"""
        self._price = value

    def to_dict(self) -> dict:
        """将图书信息转换为字典（用于序列化）"""
        return {
            "id": self.id,
            "name": self.name,
            "num": self.num,
            "price": str(self.price),
        }

    def __repr__(self) -> str:
        """图书实例的字符串表示（便于调试）"""
        return f"Book(id={self.id!r}, name={self.name!r}, num={self.num!r}, price={self.price!r})"