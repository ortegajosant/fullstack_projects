################################
# Description: Diamond Pattern #
################################

# I had a problem where there was multiple internal services in a system that required different payloads for each service.
# I had to create a class that could handle the different payloads.
# I used a diamond pattern to create a class that could handle the different payloads and also be able to validate them.
# I created the different payloads as the classes that every service would depend and also created a base class that will inherit the different payloads classes.
# So I could use the general class to load the payloads and pass it to the different services.


class BasePayload:
    def __init__(self, data=None):
        self.data = data

    def validate(self):
        raise NotImplementedError("Subclasses must implement the validate method")


class PayloadA(BasePayload):
    def __init__(self, data=None):
        super().__init__(data)
        self.specific_data_in_A = "PayloadA specific data"

    def validate(self):
        if not isinstance(self.data, dict):
            raise ValueError("PayloadA data must be a dictionary")
        if "keyA" not in self.data:
            raise ValueError("PayloadA data must contain 'keyA'")
        return True


class PayloadB(BasePayload):
    def __init__(self, data=None):
        super().__init__(data)
        self.specific_data_in_B = "PayloadB specific data"

    def validate(self):
        if not isinstance(self.data, dict):
            raise ValueError("PayloadB data must be a dictionary")
        if "keyB" not in self.data:
            raise ValueError("PayloadB data must contain 'keyB'")
        return True


class GeneralPayloadHandler(PayloadA, PayloadB):
    def __init__(self, dataA=None, dataB=None):
        BasePayload.__init__(self)  # Initialize the shared base class
        if dataA:
            PayloadA.__init__(self, dataA)
        if dataB:
            PayloadB.__init__(self, dataB)


class ServiceA:
    def process(self, payload: PayloadA):
        if not isinstance(payload, PayloadA):
            raise ValueError("ServiceA requires a PayloadA instance")
        payload.validate()
        print("ServiceA processed:", payload.data)


class ServiceB:
    def process(self, payload: PayloadB):
        if not isinstance(payload, PayloadB):
            raise ValueError("ServiceB requires a PayloadB instance")
        payload.validate()
        print("ServiceB processed:", payload.data)


def main():
    # Example usage
    try:
        payload_a = GeneralPayloadHandler(dataA={"keyA": "valueA"})
        service_a = ServiceA()
        service_a.process(payload_a)

        payload_b = GeneralPayloadHandler(dataB={"keyB": "valueB"})
        service_b = ServiceB()
        service_b.process(payload_b)

        invalid_payload = GeneralPayloadHandler(dataA={"keyC": "valueC"})
        service_a.process(invalid_payload)
    except ValueError as e:
        print("Validation error:", e)


if __name__ == "__main__":
    main()
