from abc import ABC, abstractmethod

# Strategy Pattern for different payment methods
class PaymentStrategy(ABC):

    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

class PaypalPayment(PaymentStrategy):

    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount:.2f} through PayPal.")

class StripePayment(PaymentStrategy):

    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount:.2f} through Stripe.")

class CreditcardPayment(PaymentStrategy):

    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount:.2f} through Credit Card.")


class PaymentFactory:
    _processors = {
        "paypal": PaypalPayment,
        "stripe": StripePayment,
        "creditcard": CreditcardPayment
    }

    @classmethod
    def get_payment_method(cls, method: str)-> PaymentStrategy:
        processor_class = cls._processors.get(method.lower())
        if not processor_class:
            raise ValueError(f"Unknown payment method: {method}")
        return processor_class()

class PaymentGatewaySingleton:
    _instance = None
    # implementing Singleton pattern mathod
    # using __new__ method to control instance creation
    # this ensures only one instance of PaymentGatewaySingleton exists
    def __new__(cls,payment_strategy: PaymentStrategy):
        if cls._instance is None:
            cls._instance = super(PaymentGatewaySingleton, cls).__new__(cls)
            cls._instance.payment_strategy = payment_strategy
        return cls._instance
    
    # change strategy method to change payment strategy at runtime
    def set_strategy(self, payment_strategy: PaymentStrategy) -> None:
        self.payment_strategy = payment_strategy

    def pay(self, amount: float) -> None:
        self.payment_strategy.process_payment(amount)
        
# Example usage
if __name__ == "__main__":
    amount = 100.0
    method = "paypal"  # This could be dynamic based on user input

    payment_gateway = PaymentGatewaySingleton(PaymentFactory.get_payment_method(method))
    payment_gateway.pay(amount)
    

    method = "stripe"
    payment_gateway.set_strategy(PaymentFactory.get_payment_method(method))
    payment_gateway.pay(amount)

    method = "creditcard"
    amount = 250.0
    gateway2 = PaymentGatewaySingleton(PaymentFactory.get_payment_method(method))
    gateway2.pay(amount)
    # to show that both gateway2 and payment_gateway are the same instance
    print(gateway2 is payment_gateway)  