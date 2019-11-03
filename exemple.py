import kor

#Open the file
my_file = kor.Kor(file_path="test_file.kor")

#In this example I reset the fill on each run
my_file.reset()

#add author and description
my_file.add_author(author="Koraku")
my_file.add_desc(desc="This is a example file")

#encode some msg
my_file.encode(line_type='var', line=3, name="My_var", value="Hello, I'm a var content !", value_type="str")


### custom encoding example ### ------------------------------------------------------------
### Step 1 - Define a object for your custom line type
class My_Object:
    def __init__(self, name, language):
        self.name=name
        self.language=language

### Step 2 - Create an encoding function (name does not matter) which returns the format of your custom line_type
def custom_encoding(line_type, name, value, value_type): #Your function should have all these parameters
    """
    template for custom encoding with 'My_Object'

    """
    return f"{line_type} : {name} -> {value_type} -> {value.name},{value.language}\n"

### Step 3 - Define a decoding function (name does not matter) which returns your object with the correct parameter in the right position
def custom_decoding(value_args): #Your function should have all these parameters
    """
    template for custom decoding with 'My_Object'

    """
    return My_Object(name=value_args[0], language=value_args[1])


my_test_object = My_Object(name="Obj", language="Python") # do not forget to create an instance of your object and store it in a variable

### Step 4 - now you can encode with you custom encoding following this template
custom_line_type = "Custom_Line" # I recommend using a variable to store your custom line_type so you don't spell it wrong by accident
custom_value_type = "Custom_Value"

my_file.encode(line_type="custom",
               line=5, name="My_Object_Name",
               value=my_test_object, value_type=None,
               custom_encoding=custom_encoding,
               custom_line_type=custom_line_type,
               custom_value_type=custom_value_type)


print(my_file.decode(custom_line_type=custom_line_type, custom_decoding=custom_decoding, custom_separator=","))

### Step 5 - To decode your custom line type just use the decode() method with the parameters 'custom_line_type' set to your custom line type and 'custom_decoding' set to your decoding function
my_new_test_object = my_file.decode(custom_line_type=custom_line_type, custom_decoding=custom_decoding, custom_separator=",")[1][1]

print(" ")
print(my_new_test_object.name, my_new_test_object.language)


### (New) Overrding ###
#If you want you line to be overrided just add `override=True`, it will delete any line at the given line number an replace it with the new line
my_file.encode(line_type="var", line=8, name="Ligne", value=42, value_type="num")

my_file.encode(line_type="var", line=8, name="Ligne", value=43, value_type="num", override=True)
