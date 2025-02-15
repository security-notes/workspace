# Writeup

実行ファイルと、datファイルの2つが与えられる。

datファイルの中身は`FAKE{aaa_bbb_ccc}`になっていて、デフォルトでは`Failed to activate.`となってしまう。

```
$ ./licence key.dat 
Failed to activate.
```

これが成功するようなdatファイルの中身をangrを使って調べる。引数としてファイルを与えるにはSimFileを使うらしい。

```py
import angr

bin_path = './rev-licence/licence'
licence_path = './rev-licence/key.dat'

project = angr.Project(bin_path, load_options={"auto_load_libs": False})
main_addr = project.loader.main_object.get_symbol('main').rebased_addr
state = project.factory.entry_state(args=[project.filename, licence_path])
input_file = angr.storage.SimFile(licence_path)
state.posix.fs = {licence_path: input_file}

sim = project.factory.simulation_manager(state)
# address from IDA
addr_fail = [main_addr + (0x5D88-0x5CB0) , main_addr + (0x5DE1-0x5CB0), main_addr + (0x5E44-0x5CB0)]
addr_success = main_addr + (0x5E66-0x5CB0)

sim.explore(find=addr_success,avoid=addr_fail)

if sim.found:
    print(repr(sim.one_found.fs.get(licence_path).concretize()))
```

[参考]

* [Solving file input](https://github.com/angr/angr/issues/968)

* [GCC Tokyo(Global Cybersecurity Camp v2.0) 応募課題晒し](https://ptr-yudai.hatenablog.com/entry/2019/12/16/183641)

<!-- FLAG{4n6r_15_4_5up3r_p0w3rfu1_5ymb0l1c_3x3cu710n_4n4ly515_700l} -->
