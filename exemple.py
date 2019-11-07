import kor

#Open the file
my_file = kor.Kor(file_path="test_file.kor")

#In this example I reset the fill on each run
my_file.reset()

#add author and description
my_file.add_author(author="Koraku")
my_file.add_desc(desc="This is a example file")

# Create a new line
my_line = kor.Var(name="My_Var", value="Hello i'm a var", value_type="str") #Create the var obj

my_line.encode(line=3, file=my_file) #Add it to the file

print(my_file.decode())

my_file.encode_comment(line=2, value="This is a comment !")

# class
class obj:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f"obj(name='{self.name}', age='{self.age}')"

# Fuctions
def custom_encode(line_type, name, value, value_type, separator):
	return f"{line_type} : {name} -> {value_type} -> {value.name}{separator}{value.age}"

def custom_decode(args):
	return obj(name=args[0], age=args[1])

c_line_type = []
c_separators = []
c_value_type = []
c_decoding = []

c_line_type.append("My_Custom_Line_Type")
c_value_type.append("My_Custom_Value_Type")
c_separators.append(";")
c_decoding.append(custom_decode)

my_custom_line = kor.CustomLines(name="My_line",
                                value=obj(name="KoraKu", age="16"),
                                custom_encoding=custom_encode,
                                custom_line_type=c_line_type[0],
                                custom_separator=c_separators[0],
                                custom_value_type=c_value_type[0])

my_custom_line.encode(line=10, file=my_file, override=True)

my_file.decode(custom_line_type=c_line_type, custom_decoding=c_decoding, custom_separator=c_separators)
