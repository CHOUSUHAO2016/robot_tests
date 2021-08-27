# Check your warranty

> easy, one-off immutable directories!

[Pure functions](https://en.m.wikipedia.org/wiki/Pure_function) are a powerful concept. They allow you to, given an input,
produce the same deterministic output, *without side effects*.

On the filesystem, this is hard to achieve. Filesystems are all about side
effects! Consider creating a directory as a function, and then creating a file
within it:

Base on below information to create the test cases.

URL: https://www.barco.com/en/clicksshare/aupport/warranty-info
Test Scope: The Orange rectangle below 
Please describe your strategy in your plan.



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
2. Go to " cd C:\Users\carl_chou\Documents\Barco\1\robot " this path.
3. Open a CMD, and excute the robot script as below.

```sh
$ cd C:\Users\carl_chou\Documents\Barco\1\robot

$ robot robot_tests
```

If this was part of a script you used in, say, a build process, you might run
into some problems:

1. your current directory is an implicit input; being in the wrong directory
   will have unintended side effects.
2. `mkdir foobar` is not
   [idempotent](https://en.wikipedia.org/wiki/Idempotence): multiple
   applications of it in the same directory yield different results (generally,
   an error).
3. it creates *global mutable state*. what if another not-quite-pure function
   decided it wanted to use `foobar/quux` for a different purpose? Each script
   can clobber and conflict with the other!
4. the resultant folder can be modified between functions. If I ran `mkdir foo;
   sleep 10; touch foo/quux` and, during those 10 seconds, another process did
   `rm -rf foo`, the result would be different than if they hadn't.

From this, we can say that a better solution would have the three inverse
properties:

1. the current directory should be irrelevant (that is, all paths should be
   absolute).
2. each application of a function should produce a brand new folder.
3. each brand new folder should be unique named, to prevent conflicts.
4. each brand new folder should have write permissions removed, so that its
   contents are frozen.

Enter **ice-box**: a module that manages a store of uniquely-named, immutable
directories, and makes it easy to create new ones.

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


## Case1 : Input " 1 " charactor 

Make show page will show "Please enter a valid serial number".

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

Make show page will show "Please enter a valid serial number".

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


## Case3 : Input 3 charactors 

Make show page will show "Please enter a valid serial number".

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


## Case4 : Input 4 charactors 

Make show page will show "Please enter a valid serial number".

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


## Case4 : Input 5 charactors 

Make show page will show "Please enter a valid serial number".

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


## Case6 : Input 6 charactors 

Make show page will show "Please enter a valid serial number".

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

Running `node make-tar.js some-directory/` will output

```
/home/sww/ice-box/8755ce4b-9ab0-c667-ea28-1f36bd0c8512
```

which contains the output file, `result.tar`.

## Pipelines

Much like UNIX pipes, this enables the creation of UNIX-like pipes: programs
that consume a directory can produce a new immutable directory and output that.

Imagine we had a program that took a directory of JS files and packaged them for
[Electron](http://electron.atom.io/) before the tarball step:

```js
var icebox = require('ice-box')('./ice-box')

var packager = require('electron-packager')

var src = process.argv[2]

icebox(function (dst, done) {
  packager({
    dir: src,  // use the input dir, 'src'
    arch: 'x64',
    platform: 'linux',
    out: dst,  // use the output dir, 'dst'
    tmpdir: false,
    prune: true,
    overwrite: true,
  }, done)
}, function (err, finalDir) {
  console.log(finalDir)
})
```

Now we could run this as just

```sh
$ node build-electron.js .

/home/sww/ice-box/8e3a47f8-f91d-a70b-692f-d0f54b730fb2
```

to get the electron-ready output, *or* it can be piped into `make-tar.js` from
the above section to produce the final `.tar` file!

```sh
$ node build-electron.js . | node make-tar.js

/home/sww/ice-box/a5339569-ae8f-4430-2dc1-a1a55340ea67
```

Now we have a directory with a tarball of the electron package!

*Bonus*: all intermediate steps are permanently cacheable, since they're
immutable and permanent!


## API

```js
var iceBox = require('ice-box')
```

### var icebox = iceBox([outDir], [tmpDir])

Creates a new function for adding new directories to an icebox. Both parameters
are optional, and default to sane values.

- `outDir` (string) - The location to place the immutable output directories.
  Defaults to `./ice-box`.
- `tmpDir` (string) - The temporary location to create in-progress directories
  that haven't yet finished being produced. These are cleaned up once they are
  frozen and placed in `outDir`.

### icebox(work, done)

Creates a new directory for writing to.

`work` is a function of the form `function (dir, done) { ... }`. `dir` is the
absolute path to the in-progress temporary directory. It has full write
permissions. `done` is a function to call once you are done writing, to signify
that the directory can be "frozen" and placed in the icebox. If you pass in an
error (`done(err)`) then the entire operation will abort cleanly.

`done` is a function of the form `function (dir) { ... }`. It is called once the
newly-frozen output directory is placed in the ice-box (`outDir` from the above
section). `path` is a string containing the absolute path to the frozen,
immutable, unique directory.


## Install

With [npm](https://npmjs.org/) installed, run

```
$ npm install ice-box
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
