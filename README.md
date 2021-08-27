# ice-box

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



Case1
Check web device
    check web device

Case2
Get web dataEmptyC
    getEmptyC

Case3
Input 1 charactor
    get_web_data1

Case4
Input 2 charactors
    get_web_data2

Case5
Input 3 charactors
    get_web_data3

Case6
Input 4 charactors
    get_web_data4

Case6
Input 5 charactors
    get_web_data5

Case7
Input 6 charactors
    get_web_data6

Case8
Input 10 charactors
    get_web_data10

Case9
Input 11 charactors
    get_web_data11

Case10
Input BeyondBorder1024 charactors

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

## Case1 : Input no any charactors as empty

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
