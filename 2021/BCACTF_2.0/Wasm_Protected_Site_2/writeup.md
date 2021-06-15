# Writeup

http://web.bcactf.com:49158/ にアクセスする。

`Wasm Protect Site 1`と同様にwasmを見る。

```wasm
(module
  (memory $memory (;0;) (export "memory") 1)
  (func $cmp (;0;) (param $v0 (;0;) i32) (param $v1 (;1;) i32) (result i32)
    (local $v2 (;2;) i32)
    loop $label0
      local.get $v2
      local.get $v0
      i32.add
      i32.load8_u
      local.get $v2
      local.get $v1
      i32.add
      i32.load8_u
      local.get $v2
      i32.const 9
      i32.mul
      i32.const 127
      i32.and
      i32.xor
      i32.ne ★
      local.get $v2
      i32.const 27
      i32.ne
      i32.and
      if
        i32.const 0
        return
      end
      local.get $v2
      i32.const 1
      i32.add
      local.tee $v2
      i32.const 1
      i32.sub
      local.get $v0
      i32.add
      i32.load8_u
      i32.eqz
      if
        i32.const 1
        return
      end
      br $label0
    end $label0
    i32.const 0
    return
  )
  (func $checkFlag (;1;) (export "checkFlag") (param $a (;0;) i32) (result i32)
    local.get $a
    i32.const 1000
    call $cmp
    return
  )
  (data (i32.const 1000) "bjsxPKMH|\227N\1bD\043b]PR\19e%\7f/;\17")
)
```

★ 部分で文字の比較を行っているので、Breakpointをつけて変数を監視する。`stack[1].value`に比較対象の文字コードが入っている。

```py
char = [98, 99, 97, 99, 116, 102, 123, 119, 52, 115, 109, 45, 119, 49, 122, 52, 114, 68, 114, 121, 45, 88, 99, 48, 119, 90, 125]

for c in char:
    print(chr(c),end='')
```

<!-- bcactf{w4sm-w1z4rDry-Xc0wZ} -->
