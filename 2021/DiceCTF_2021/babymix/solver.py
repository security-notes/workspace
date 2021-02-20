
import angr

p = angr.Project('babymix')
main_addr = p.loader.main_object.get_symbol('main').rebased_addr
print('main_addr = ',main_addr)
state = p.factory.entry_state()
sim = p.factory.simulation_manager(state)
addr_success = main_addr + (0x222C-0x21C5)
addr_failed = main_addr + (0x2238-0x21C5)
sim.explore(find=addr_success,avoid=addr_failed)
if len(sim.found) > 0:
    print(sim.found[0].posix.dumps(0))