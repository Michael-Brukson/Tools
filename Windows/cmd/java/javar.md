## javar.cmd

A shortening of two commands, `javac` ( java compile ) and `java` ( java execute ) to just one, `javar` ( java run ).

The file that must be passed to the parameter is the same as if `javac` would be run.

### Accepts parameters:

- `-verbose` / `-v` `<boolean>`: "Verbose"; whether to print out when file is being compiled and run. Defaults to false.

### Examples:

```bash
C:\>javar Test.java -v
compiling test.java...
running test.java...

Hello World!
```
