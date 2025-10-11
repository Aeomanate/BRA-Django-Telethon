import os

packages = ["telethon", "vtk", "colorama"]

for pkg_name in packages:
    try:
        pkg = __import__(pkg_name)
        path = pkg.__path__[0]
        py_typed = os.path.join(path, "py.typed")

        if not os.path.exists(py_typed):
            with open(py_typed, "w"):
                pass
            print(f"py.typed created at {py_typed}")
        else:
            print(f"py.typed already exists at {py_typed}")

    except Exception as e:
        print(f"Error processing {pkg_name}: {e}")

