import decimal


class BookDir:
    """图书目录模型类，包含图书目录核心属性及操作方法"""
    def __init__(
            self,
            name: str,
            num: int,
            id = None,
    ):
        # 初始化图书目录实例
        self.id = id
        self.name = name
        self.num = num

    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, value: int) -> None:
        """设置图书目录ID"""
        self._id = value

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        """设置图书目录名称"""
        self._name = value

    @property
    def num(self) -> int:
        return self._num
    
    @num.setter
    def num(self, value: int) -> None:
        """设置图书目录数量"""
        self._num = value

    def to_dict(self) -> dict:
        """将图书目录信息转换为字典（用于序列化）"""
        return {
            "id": self.id,
            "name": self.name,
            "num": self.num,
        }

    def __repr__(self) -> str:
        """图书目录实例的字符串表示（便于调试）"""
        return f"BookDir(id={self.id!r}, name={self.name!r}, num={self.num!r})"