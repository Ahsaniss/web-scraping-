# test_order_processor.py

import unittest
from refactory1 import process_order

class TestProcessOrder(unittest.TestCase):

    def test_credit_card_successful_order(self):
        order = {
            "payment_type": "credit_card",
            "card_number": "1234567812345678",
            "expiration_date": "12/24",
            "card_security_code": "123",
            "shipping_address": "123 Main St",
            "quantity": 2,
            "price": 100.0
        }
        result = process_order(order)
        print(result)
        self.assertEqual(result, "Order processed successfully")  # ✅ Add this

    def test_paypal_successful_order(self):
        order = {
            "payment_type": "paypal",
            "paypal_email": "user@example.com",
            "shipping_address": "456 Elm St",
            "quantity": 1,
            "price": 50.0
        }
      #  process_order(order)
        result = process_order(order)
        print(result)
        self.assertEqual(result, "Order processed successfully")

    def test_invalid_card_number(self):
        order = {
            "payment_type": "credit_card",
            "card_number": "1234",  # too short
            "expiration_date": "12/24",
            "card_security_code": "123",
            "shipping_address": "123 Main St",
            "quantity": 1,
            "price": 100.0
        }
        with self.assertRaises(ValueError) as context:
            process_order(order)
        self.assertEqual(str(context.exception), "Invalid card number")

    def test_missing_expiration_date(self):
        order = {
            "payment_type": "credit_card",
            "card_number": "1234567812345678",
            "expiration_date": "",
            "card_security_code": "123",
            "shipping_address": "123 Main St",
            "quantity": 1,
            "price": 100.0
        }
        with self.assertRaises(ValueError) as context:
            process_order(order)
        self.assertEqual(str(context.exception), "Expiration date is missing")

    def test_invalid_card_security_code(self):
        order = {
            "payment_type": "credit_card",
            "card_number": "1234567812345678",
            "expiration_date": "12/24",
            "card_security_code": "12",  # too short
            "shipping_address": "123 Main St",
            "quantity": 1,
            "price": 100.0
        }
        with self.assertRaises(ValueError) as context:
            process_order(order)
        self.assertEqual(str(context.exception), "Invalid card security code")

    def test_missing_paypal_email(self):
        order = {
            "payment_type": "paypal",
            "paypal_email": "",
            "shipping_address": "123 Main St",
            "quantity": 1,
            "price": 100.0
        }
        with self.assertRaises(ValueError) as context:
            process_order(order)
        self.assertEqual(str(context.exception), "PayPal email is missing")

    def test_missing_shipping_address(self):
        order = {
            "payment_type": "paypal",
            "paypal_email": "user@example.com",
            "shipping_address": "",
            "quantity": 1,
            "price": 100.0
        }
        with self.assertRaises(ValueError) as context:
            process_order(order)
        self.assertEqual(str(context.exception), "Shipping address is missing")

    def test_invalid_quantity(self):
        order = {
            "payment_type": "paypal",
            "paypal_email": "user@example.com",
            "shipping_address": "123 Main St",
            "quantity": 0,  # invalid quantity
            "price": 100.0
        }
        with self.assertRaises(ValueError) as context:
            process_order(order)
        self.assertEqual(str(context.exception), "Quantity must be greater than zero")

if __name__ == "__main__":
    unittest.main()
