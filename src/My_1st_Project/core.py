class CustomerDataClass:
    """ Класс реализует клиента со списком заказов.
    """
    def __init__(self, customerId, customerName):
        """ Конструктор класса

        Args:
            customerId (number): Номер клиента
            customerName (string): Название клиента
        """
        self.CustomerId = customerId
        self.CustomerName = customerName
        self.Orders = []

    def AddOrder(self, orderObject):
        """ Метод класса добавляет заказ в спиок заказов клиента.

        Args:
            orderObject (OrderDataClass): объект заказа
        """
        self.Orders.append(orderObject)

    def GetTotalAmount(self):
        """ Метод класса возвращает суммарный объем заказов клиента.

        Returns:
            float: суммарный объем заказов
        """
        total = 0
        for o in self.Orders:
            total = total + o.amount
        return total


class OrderDataClass:
    """ Класс реализует заказ клиента.
    """
    
    def __init__(self, orderId, amount):
        """ Конструктор класса заказа.

        Args:
            orderId (number): номер заказа
            amount (float): сумма заказа
        """
        self.orderId = orderId
        self.amount = amount


def CalculateDiscount(customerObj):
    """ Функция вычисляет сумму скидки клиента.

    Args:
        customerObj (CustomerDataClass): объект класса клиента

    Returns:
        float: сумма скидки
    """
    totalAmount = customerObj.GetTotalAmount()
    if totalAmount > 1000:
        discount = totalAmount * 0.1
    else:
        discount = 0
    return discount


def PrintCustomerReport(customerObj):
    """ Функция выполняет вывод информации по клиенту.

    Args:
        customerObj (CustomerDataClass): объект класса клиента
    """
    # вывести название клиента и число заказов
    print("Customer Report for:", customerObj.CustomerName)
    print("Total Orders:", len(customerObj.Orders))
    # вывести общую сумму заказов
    print("Total Amount:", customerObj.GetTotalAmount())
    # вывести сумму скидки для клиента
    print("Discount:", CalculateDiscount(customerObj))
    # вывести среднюю сумму заказа
    if len(customerObj.Orders) > 0:
        # - расчет средней суммы заказа для клиента выполняется
        #   только при наличии у него хотя бы одного заказа
        print("Average Order:", customerObj.GetTotalAmount() / len(customerObj.Orders))
    else:
        print("Average Order: no orders")



def MainProgram():
    """ Главная функция программы.
    """
    # создадим объект класса для первого клиента
    c1 = CustomerDataClass(1, "SAP Customer")
    # и добавим в него заказы
    o1 = OrderDataClass(101, 500)
    o2 = OrderDataClass(102, 800)
    c1.AddOrder(o1)
    c1.AddOrder(o2)

    # выведем информацию по первому клиенту
    PrintCustomerReport(c1)

    # создадим объект второго клиента без заказов
    c2 = CustomerDataClass(2, "Empty Customer")
    # выведем информацию по второму клиенту
    PrintCustomerReport(c2)

# запуск главной функции программы
MainProgram()
