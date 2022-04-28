from pprint import pprint

try:
    import understand as und
except ImportError:
    print("Can not import understand")

db = und.open(
    "D:/UNI/term_6/Comiler/project/OpenUnderstand/benchmark/ganttproject/ganttproject/ganttproject/ganttproject.und")

kind_names = set()

for ent in db.ents():
    for ref in ent.refs():
        kind_names.add(ref.kindname())
        if ref.kindname() == "Implicit Extend":
            print(f"ent name: {ent.name()}, ent longname: {ent.longname()}, \n"
                  f"ent parent: {ent.parent()}, ent kind: {ent.kind()}, ent value: {ent.value()},\n"
                  f"ent type: {ent.type()}")
            print("+++++++++++++++++++++++++")
            # print(f"file kind: {ref.file().kind()}, parent: {ref.file().parent()}, long name: {ref.file().longname()}"
            #       f"\nvalue: {ref.file().value()}, type: {ref.file().type()}, contents: {ref.file().contents()}, name: {ref.file().name()}")

            print(f"entity: {ent}\n, ref: {ref}\n ref.scope: {ref.scope()}, ref.ent: {ref.ent()}\n"
                  f"ref.line: {ref.line()}, ref.col: {ref.column()}, ref.file: {ref.file().name()}")
            print("--------------------------------------------------------")
            print(
                f"ref.ent.name:{ref.ent().name()}, ref.ent.longname:{ref.ent().longname()} ,ref.ent.kind:{ref.ent().kind()}\n"
                f"ref.ent.parent:{ref.ent().parent()}, ref.ent.value:{ref.ent().value()},ref.ent.type:{ref.ent().type()}\n"
            )
            print("**********************************************************")

c = 2
