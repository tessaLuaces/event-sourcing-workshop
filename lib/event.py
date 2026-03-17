class Event:
    """
    Representation of a domain event.
    An event is a fact that happened in the past, relevant to the domain. It's immutable.

    As a basic implementation it will contain only:
    - id
    - name
    - data
    - timestamp
    """