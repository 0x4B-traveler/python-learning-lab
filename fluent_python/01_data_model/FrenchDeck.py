"""A small Card example inspired by Fluent Python's data model chapter."""
import collections

# 使用namedtyple构建只有属性没有自定义方法的类对象，例如数据库种的一条记录
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self) -> None:
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def spades_high(self, card):
        """排序函数"""
        rank_value = self.ranks.index(card.rank)
        return rank_value * len(self.suit_values) + self.suit_values[card.suit]

# 特殊方法供python解释器调用
# 在处理内置类型时，python解释器会从可变长度容器的底层C语言实现中的结构体PyVarObject的ob_size字段直接读取
# for i in x: 其实是在背后调用iter(x), 接着又调用x.__iter__()或x.__getitem__()
# 特殊方法最重要的用途：
# 模拟数值类型
