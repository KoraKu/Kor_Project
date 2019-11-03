﻿

# Kor Project
This repository contains the files of the Kor project with all the doc that you need

## The Kor Project Goals
The kor project is desinged to store easlily data in file (.kor file) such as numbers, list, and many more ! You can define your own encoding method to encode your own object or varaible type.

## Why use kor files ?
- Kor files allows you to easily store data 
- Can easily be customized to suit your needs 
- Is very simple to use

## Example

1) First of all you'll need to import kor
```python
import kor
```


2) The you'll need to create your file object before working with it 
```python
my_file = kor.Kor(file_path="test_file.kor")
```


3) Now you can use one one the module's method to do something with it, for instance we can add an author and a description

```python
my_file.add_author(author="Koraku")  
my_file.add_desc(desc="This is a example file")
```

The content of the file :
```
*Author : Koraku  
*Desc : This is a example file
```

4) Add more content !

```python
my_file.encode(line_type='var', line=3, name="My_var", value="Hello, I'm a var content !", value_type="str")
```


# Kor project documentation

## List of all the method you'll need 
### File options
- `add_author(author)` is used to add an author to your file
- `add_desc(desc)` is used to add a description to your file
- `get_author()` returns the author of the file
- `get_desc()` returns the description of the file

### Encoding and decoding
- `encode(line_type, line, name, value, value_type, custom_encoding=None, custom_line_type=None, custom_value_type=None)` see the "**Encode parameters description**" section for further information

- `decode(custom_line_type=None, custom_decoding=None)` see the "**Decode parameters description**" for further information

### Others
- `reset()` erase all the data in your file, **irreversible**
- `search(line_type, name)`  search in the file if a line has a certain name and returns `[True, line_name, line_number]` if found and `[False, None, None]` if not found


## Encode parameters description
### Line types
There are three line type by default : 
1) `var` is used to store `str` (string) or numbers
2) `list` is used to store `list` or `tuple`
3) `custom` is used to use your custom encoding method, see bellow for further information

### Line
The first two lines of the files are dedicated to the file author and description, keep in mind that the **first line starts at 0** not 1

### Value
The value is what your line will contain, the type of the content must be specified with `value_type`

### Value type
There are 2 value type by default :
1) `str` for string
2) `num`for numbers (int, float...)

### Custom_encoding/custom_line_type/custom_value_type
Used for custom encoding, see "**How to : Custom encoding**" section for further information

## Decode parameters description
The only parameters that `decode()` takes are `custom_line_type`, `custom_decoding` & `custom_separator` which are both used for custom decoding, see "**How to : custom decoding**" section for further information.

## Custom parameters
The Kor Project allows you to create your own encoding methods, in those two examples you will learn how to do so
Also, see "**example.py**" in the github page

### How to : custom encoding

1) Firstly, import kor and create your file object
```python
import kor

my_file = kor.Kor(file_path="test_file.kor")
```

2) Secondly, create your object
```python
class My_Object:  
    def __init__(self, name, language):  
        self.name=name
        self.language=language

my_test_object = My_Object(name="Obj", language="Python")
```

3) Then you'll need to create one fuction for encoding, for instance :
```python
def custom_encoding(line_type, name, value, value_type): 
	return f"{line_type} : {name} -> {value_type} -> {value.name},{value.language}\n"
```
Value is your instance of `My_Object`, name is the name of your line, line_type will be your custom line type and value type your custom value_type

4) I highly recommend you to define thos variables to prevent spelling mistakes
```python
custom_line_type = "Custom_Line"
custom_value_type = "Custom_Value"
``` 
5) Now you can encode your object !
Use the `encode()` method as showed 
```python
my_file.encode(line_type="custom",  
	line=3, 
	name="My_Object_Name",  
	value=my_test_object, 
	value_type=None,  
	custom_encoding=custom_encoding,  
	custom_line_type=custom_line_type,  
	custom_value_type=custom_value_type)
```
You must set `line_type` to `custom` to use your custom encoding
`value` is your instance of you object (step 2)
`custom_encoding` should be set to your custom encoding fuction (step 3)
`custom_line_type` & `custom_value_type` are used for you custom line and value type (step 4)

The result of the above code :
```kor
*Author : Koraku  
*Desc : This is a example file  

Custom_Line : My_Object_Name -> Custom_Value -> Obj,Python
```

### How to : custom decoding

Repeat steps 1 & 2

3. Create your custom decoding fuction
```python
def custom_decoding(value_args):
	return My_Object(name=value_args[0], language=value_args[1])
```

`value_args` will be passed in your function, it represent a list with the value of you objetc parameters (in this exemple), here it is `['Obj', 'Python']`

4. Now decode your file with the `decode()` method
```python
my_file.decode(custom_line_type=custom_line_type,
	custom_decoding=custom_decoding, 
	custom_separator=",")
```

5. if you print the output of this method it will give
```python
[('My_Object_Name', <__main__.My_Object object at 0x00000270B6579E48>)`]
```
We can print the name and the value of our object :
```python
my_new_obj = my_file.decode(custom_line_type=custom_line_type,
	custom_decoding=custom_decoding, 
	custom_separator=",")[0][1]

print(my_new_obj.name, my_new_obj.language)
```

output : 
```
Obj Python
```

Now you know how to encode and decode your own object ! 🙌🎉
