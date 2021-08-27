# Check your warranty

Base on below information to create the test cases.

URL: https://www.barco.com/en/clicksshare/aupport/warranty-info

Test Scope :  
As below plan, I described all my strategy. The test cases are Manual test cases and Automation test cases. 
And then, choose some Automation cases to create scripts and run in robot framework. 

# Design search box test cases
1. The search content is empty, verify how the system handles it
2. The search content is blank, check how the system handles it
3. Boundary value verification, within and outside the allowed string length, verify the processing of the system
4. Enter a very long string, whether the system will capture the allowed length to verify the result
5. After entering a string of legal length, add a space to verify that the result of the system is correct
6. Add spaces, commas, and TAB between multiple keywords to verify that the result of the system is correct
7. Verify each legal input and the result is correct
8. Whether to support copying, pasting, editing and other operations of retrieved content
9. Whether to support enter key search
10. Enter the same content multiple times to check whether the search results of the system are consistent
11. Special characters, translated characters, HTML, scripts, etc. need to be processed
12. Enter sensitive words, prompt the user to have no permission, etc.
13. Does the input support shortcut key operations, etc.
14. Only enter the allowed string length, etc.
15. Whether the input key is correct and jumps correctly
16. Is the search history displayed below
17. Does the search content have association function?
18. Is it possible to input numbers, English, Chinese
19. Is it possible to mix input numbers, English, and Chinese?
20. Input pinyin can also search
21. Whether the content of voice search matches
22. Unable to search when the internet is disconnected
23. You can choose to take a picture or select a picture from the album when searching for pictures
24. If you select a picture from the album to search, is there a limit to the size of the picture, and what is the maximum?
25. There are camera pictures on the side of the search box for easy picture search
26. Click Clear History, whether the search box will clear the history
27. Can identify the content in the picture
28. Click Search to display the search interface

# Interface test
1. Check if the UI is displayed correctly and the layout is reasonable
2. Are there any typos
3. Is the layout displayed in the search results beautiful?
4. The checked results are keyed and the color of the keyed is brilliantly processed
5. When the result data is huge, is the page layout of the page reasonable?
6. Is the color matching of the interface correct?



# Security test
1. Disabling the script
2. SQL injection, retrieval of SQL SELECT statements, etc.
3. Retrieval of sensitive content is prohibited
4. Search for special characters
5. The deleted, encrypted, and authorized data are not allowed to be found out
6. Is there a safety design control

# Compatibility test
1. Multi-platform Windows Mac
2. Mobile platform Android iOS
3. Multi-browser Firefox, Chrome, IE, etc.

# Performance test
1. The time when the key of the search page was opened
2. Time consumed to search for results
3. The response time of search when the network is weak
4. Response time when searching under different network speeds, such as 3G

# Ease of use
1. Has Lenovo function
2. The degree of match between the search results and the search results
3. Support photo search, voice search


# Automation Test - Start to run robot script
1. First, please unzip robot_tests.7z.
2. Go to robot folder inside.
3. Open a CMD, and excute the robot script as below.

```sh
$ cd C:\Users\carl_chou\Documents\Barco\1\robot

$ robot robot_tests
```


## Case0 : Input no any charactors as empty

Make show page will show "Please enter a valid serial number".

```python
def getEmptyC():
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    data = {"SerialNumber":""}
    uri = "https://www.barco.com/en/clickshare/support/warranty-info"
    rs = requests.session()
    res = rs.post(uri, data=data, headers=header, timeout=300)
    html_data = ''
    if res.status_code == 200:
        print('OK')
        html_data = res.text
        print(html_data)
    else:
        print('Server error')
    if(html_data.find("Please enter a valid serial number")):
        return "Please enter a valid serial number."
    else:
        return 0 
```


## Case1 : Input "1" charactor 

Front page will show "Minimum 6 characters required".if only input 1 charactor.

```python
def get_web_data1():
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    data = {"SerialNumber":"1"}
    uri = "https://www.barco.com/en/clickshare/support/warranty-info"
    rs = requests.session()
    res = rs.post(uri, data=data, headers=header, timeout=300)
    html_data = ''
    if res.status_code == 200:
        print('OK')
        html_data = res.text
        print(html_data)
    else:
        print('Server error')
    if(html_data.find("Minimum 6 characters required")):
        return "Please input 6 charactors at least."
    else:
        return 0 
```


## Case2 : Input "2" charactors 

Front page will show "Minimum 6 characters required".if only input 2 charactor.

```python
def get_web_data1():
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    data = {"SerialNumber":"11"}
    uri = "https://www.barco.com/en/clickshare/support/warranty-info"
    rs = requests.session()
    res = rs.post(uri, data=data, headers=header, timeout=300)
    html_data = ''
    if res.status_code == 200:
        print('OK')
        html_data = res.text
        print(html_data)
    else:
        print('Server error')
    if(html_data.find("Minimum 6 characters required")):
        return "Please input 6 charactors at least."
    else:
        return 0 
```


## Case3 : Input "3" charactors 

Front page will show "Minimum 6 characters required".if only input 3 charactor.

```python
def get_web_data1():
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    data = {"SerialNumber":"111"}
    uri = "https://www.barco.com/en/clickshare/support/warranty-info"
    rs = requests.session()
    res = rs.post(uri, data=data, headers=header, timeout=300)
    html_data = ''
    if res.status_code == 200:
        print('OK')
        html_data = res.text
        print(html_data)
    else:
        print('Server error')
    if(html_data.find("Minimum 6 characters required")):
        return "Please input 6 charactors at least."
    else:
        return 0 
```


## Case4 : Input "4" charactors 

#Front page will show "Minimum 6 characters required".if only input 4 charactor.

```python
def get_web_data1():
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    data = {"SerialNumber":"1111"}
    uri = "https://www.barco.com/en/clickshare/support/warranty-info"
    rs = requests.session()
    res = rs.post(uri, data=data, headers=header, timeout=300)
    html_data = ''
    if res.status_code == 200:
        print('OK')
        html_data = res.text
        print(html_data)
    else:
        print('Server error')
    if(html_data.find("Minimum 6 characters required")):
        return "Please input 6 charactors at least."
    else:
        return 0 
```


## Case5 : Input "5" charactors 

Front page will show "Minimum 6 characters required".if only input 5 charactor.

```python
def get_web_data1():
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    data = {"SerialNumber":"11111"}
    uri = "https://www.barco.com/en/clickshare/support/warranty-info"
    rs = requests.session()
    res = rs.post(uri, data=data, headers=header, timeout=300)
    html_data = ''
    if res.status_code == 200:
        print('OK')
        html_data = res.text
        print(html_data)
    else:
        print('Server error')
    if(html_data.find("Minimum 6 characters required")):
        return "Please input 6 charactors at least."
    else:
        return 0 
```


## Case6 : Input "6" charactors 

Front page will show "Minimum 6 characters required".if only input 6 charactor.

```python
def get_web_data1():
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    data = {"SerialNumber":"111111"}
    uri = "https://www.barco.com/en/clickshare/support/warranty-info"
    rs = requests.session()
    res = rs.post(uri, data=data, headers=header, timeout=300)
    html_data = ''
    if res.status_code == 200:
        print('OK')
        html_data = res.text
        print(html_data)
    else:
        print('Server error')
    if(html_data.find("Minimum 6 characters required")):
        return "Please input 6 charactors at least."
    else:
        return 0 
```


## Case7 : Input "10" charactors 

Front page will show "Minimum 6 characters required".if only input 6 charactor.

```python
def get_web_data10():
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    data = {"SerialNumber":"1111111111"}
    uri = "https://www.barco.com/services/website/en/WarrantyLister/GetWarrantyResult"
    rs = requests.session()
    res = rs.post(uri, data=data, headers=header, timeout=300)
    html_data = ''
    if res.status_code == 200:
        print('OK')
        html_data = res.text
        print(html_data)
    else:
        print('Server error')
    if(html_data.find("R9849880")):
        return "R9849880"
    else:
        return 0   
```


## Case8 : Input "11" charactors 

Front page will show "We are sorry, there is no warranty information available about this product, if you need more information about this, please.

```python
def get_web_data11():
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    data = {"SerialNumber":"11111111111"}
    uri = "https://www.barco.com/services/website/en/WarrantyLister/GetWarrantyResult"
    rs = requests.session()
    res = rs.post(uri, data=data, headers=header, timeout=300)
    html_data = ''
    if res.status_code == 200:
        print('OK')
        html_data = res.text
        print(html_data)
    else:
        print('Server error')
    if(html_data.find("We are sorry, there is no warranty information available about this product, if you need more information about this, please")):
        return "We are sorry, there is no warranty information available about this product, if you need more information about this, please"
    else:
        return 0   
```


## Case9 : Input "1024" charactors (Beyond the border) 

Front page will show "Please enter a valid serial number.

```python
def get_web_BeyondBorder1024():
    str = ""
    for i in range(1024): 
        str = str+"1"
    print(str)    
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    data = {"SerialNumber":f"{str}"}
    uri = "https://www.barco.com/en/clickshare/support/warranty-info"
    rs = requests.session()
    res = rs.post(uri, data=data, headers=header, timeout=300)
    html_data = ''
    if res.status_code == 200:
        print('OK')
        html_data = res.text
        print(html_data)
    else:
        print('Server error')
    if(html_data.find("Please enter a valid serial number")):
        return "Please enter a valid serial number"
    else:
        return "fail"
```


## Acknowledgments

I was inspired by looking at how many codebases will use a many-step build
process that involves transforming directories (source dir -> build dir ->
packaged dir -> windows installer program), but suffer from side effects and
shared global state. If build steps were interrupted the series of output
directories would be inconsistent, hard to track down, etc. I really wanted to
be able to make build and release pipelines that were as easy to reason about as
UNIX pipes.

## See Also

- [`noffle/common-readme`](https://github.com/noffle/common-readme)

## License

ISC
