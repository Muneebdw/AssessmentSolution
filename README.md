# Dataloop.AI Assessment Test

This repository contains the solution for the Dataloop.AI assessment test. The test involves building a Pythonic data model class called `Data` with specific requirements.


## Usage

To use the `Data` class, follow these steps:

1. Instantiate the `Data` class directly or use the `from_dict()` method to create an instance from a dictionary.
2. Access attributes of the `Data` instance, set default values, or retrieve inner values reflected on the main level.
3. Utilize the `to_dict()` method to convert the `Data` instance back to a dictionary, if needed.

Example Usage:

```python
# Instantiate a Data instance from a dictionary
data = {
    "id": "1",
    "name": "first",
    "metadata": {
        "system": {
            "size": 10.7
        },
        "user": {
            "batch": 10
        }
    }
}

my_inst = Data.from_dict(data)

# Access attributes and reflect inner values
print(my_inst.metadata)  # Retrieve the 'metadata' attribute
print(my_inst.size)  # Retrieve the 'size' attribute reflected from 'metadata.system'

# Set default values
print(my_inst.height)  # Retrieve the default value for 'height' from 'metadata.system'
print(my_inst.to_dict()['metadata']['system']['height'])  # Print the default value

# Convert the Data instance back to a dictionary
data_dict = my_inst.to_dict()
