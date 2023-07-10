from data_model import Data

data = {
    "id": "1",
    "name": "first",
    "metadata": {
        "system": {
            "size": 10.7
        },
        "user": {
            "batch": 14
        }
    }
}

# load from dict
my_inst_1 = Data.from_dict(data)

# load from inputs
my_inst_2 = Data(name="my")

# reflect inner value
print(my_inst_1.size)  # prints: 10.7

# default values
print(my_inst_1.height)  # prints: 100
print(my_inst_1.to_dict()['metadata']['system']['height'])  # prints: 100

## autocomplete - should complete to metadata
data.me