from abc import ABC, abstractmethod

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

    @staticmethod
    def get_payment_method(method: str) -> PaymentStrategy:
        if method == "paypal":
            return PaypalPayment()
        elif method == "stripe":
            return StripePayment()
        elif method == "creditcard":
            return CreditcardPayment()
        else:
            raise ValueError(f"Unknown payment method: {method}")
        
# Example usage
if __name__ == "__main__":
    amount = 100.0
    method = "paypal"  # This could be dynamic based on user input

    payment_method = PaymentFactory.get_payment_method(method)
    payment_method.process_payment(amount)


'''Factory Pattern Explanation:
The main purpose of a factory class is to abstract a series of similar object creation operations 
and delegate them to a dedicated “factory” that is responsible for producing objects. 
The client does not need to create concrete instances directly; 
it only needs to specify the type of object it requires, 
and the factory will create and return the corresponding instance.

In terms of implementation, 
the factory usually leverages the inheritance relationship between a parent class and its subclasses: 
the parent class defines an abstract interface (or abstract methods) without implementing them, 
while concrete subclasses implement the parent’s methods to provide specific functionality. 
The factory creates the appropriate subclass instances through the parent class interface. 
This design ensures that the client is decoupled from the specific implementation, 
and it also makes it easy to extend the system with new product types in the future without modifying existing code.
'''