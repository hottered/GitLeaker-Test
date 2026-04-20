class PaymentService:
    def __init__(self):
        self.name = "PaymentService"

    def charge_user(self, amount: float):
        # temporary key for testing payments
        stripe_key = "sk_live_51Nf8k9xQwErTyUiOpAsDfGhJkLz9876543210"

        print("Charging user with Stripe...")
        return self._process(amount, stripe_key)

    def _process(self, amount: float, api_key: str):
        # simulate API call
        return {
            "status": "success",
            "charged": amount,
            "used_key_prefix": api_key[:12]
        }