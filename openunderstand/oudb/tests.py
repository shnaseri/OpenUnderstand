from metrics.count_decl_method import main as count_decl_method

try:
    import understand as und
except ImportError:
    print("Can not import understand")

db = und.open(
    "D:/UNI/term_6/Comiler/project/ym/OpenUnderstand/benchmark/jvlt-1.3.2/jvlt-1.3.2/src/src.und")

kind_names = set()
count = 0
class_count_function = {}
for ent in db.ents("Java Class ~Unknown ~Unresolved"):
    cycle = ent.metric(['CountDeclMethod']).get('CountDeclMethod', 0)
    ent_kind = ent.kind()
    if cycle:
        kind_names.add(ent_kind.__repr__())
        count += cycle
        class_count_function[ent.name()] = cycle + class_count_function.get(ent.name(), 0)
print(class_count_function)
print(count)
# map_result = count_decl_function()


# map_result = count_decl_instance_method()
# map_result = count_decl_instance_variable()
map_result = count_decl_method()
for key, index in class_count_function.items():
    find = False
    for key2, index2 in map_result.items():
        if key == key2:
            find = True
            if index != index2:
                continue
                print(key)
    if not find:
        continue
        print(key)
c = 2
