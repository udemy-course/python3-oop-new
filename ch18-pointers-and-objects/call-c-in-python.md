创建一个 C 文件 `add.c`

```
int add(int x, int y)
{
    return x + y;
}

```

编译 Linux 下的动态链接库

```
gcc -c -fpic add.c
gcc -shared -o libadd.so add.o
```

使用

```
>>> import ctypes
>>> add_lib = ctypes.CDLL("./libadd.so")
>>> add = add_lib.add
>>> add
<_FuncPtr object at 0x7ff4f2908dc0>
>>> add(1,2)
3
```
