class Data:
    def __init__(self, **kwargs):
        self._data = kwargs  #Assigns Rcv Argument into data
        self._default_values = {'height': 100}  #Default Values

    @classmethod
    def from_dict(cls, data_dict): #class method
        return cls(**data_dict) #Gives the data to the class through kwargs

    def to_dict(self):
        return self._data #Returns the data

    def __getattr__(self, name):
        # This method gets called when the attribute is not found in the instance dictionary

        #Checking if it exists in metadata.system
        if 'metadata' in self._data and 'system' in self._data['metadata']:
            if name in self._data['metadata']['system']:
                return self._data['metadata']['system'][name]

        # Check if default value exists for the attribute
        if name in self._default_values:
            # Set default value to the attribute
            if 'metadata' in self._data and 'system' in self._data['metadata']:
                self._data['metadata']['system'][name] = self._default_values[name]
                return self._default_values[name]

        # Raising appropriate error
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        
    def __dir__(self):       
        # This method gets called upon the dir() function call and allows data.metadata to be autocompleted
        system_attrs = list(self._data.get('metadata', {}).get('system', {}).keys()) #Gets all the keys in metadata.system
        return super().__dir__() + system_attrs #Returns all the attributes