from typing import Optional


class Client(object):
    """Client object."""

    def __init__(self) -> None:
        """Initialize the client object."""
        self.name = "John Doe"
        self.age = 30
        self.address = "123 Main Street"
        self.phone = "555-555-5555"

    def verify(self) -> None:
        """Verify the client object."""
        print("Client verified!")

def client_object(verify: Optional[bool] = True) -> Client:
    """Create a client object.

    Args:
        verify (bool, optional): Verify if the client is valid. Defaults to True.

    Returns:
        Client: Client object.
    """
    client = Client()
    if verify:
        client.verify()
    return client

# write a method that calls the client_object function and returns the client object
def get_client_object() -> Client:
    """Get the client object.

    Returns:
        Client: Client object.
    """
    client = client_object()
    if client:
        return True
    else:
        return False