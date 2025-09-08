""" Первый пробный пакет. 
Содержит классы:
    CustomerDataClass (реализует клиента со списком заказов)
    OrderDataClass (реализует заказ клиента)
Содержит функции:
    CalculateDiscount Функция вычисляет сумму скидки клиента
    PrintCustomerReport Функция выполняет вывод информации по клиенту
"""

# Версия пакета
__version__ = "0.1.0"

# Импорт публичного API (оставляем только то, что нужно пользователю)
from .core import CustomerDataClass, OrderDataClass, CalculateDiscount, PrintCustomerReport

# Ограничение экспорта при `from ... import *` 
__all__ = [
    "CustomerDataClass",
    "OrderDataClass",
    "CalculateDiscount",
    "PrintCustomerReport",
]

# Метаданные (необязательно)
__author__ = "Глухов Д.Н."
__license__ = "MIT"
