import os
import re
import ast
import pandas as pd
import json

gold_labels_folder = "Labels2"

smells = [
    "BuiltInBehavior",
    "ExtraUsageOfArrays",
    "ImproperDataStructure",
    "LackingBreak",
    "NotCaching",
    "OveruseOfLoops",
    "UnnecessaryConditionals",
    "UnnecessaryRecursion",
    "UnnecessaryTypeConversion",
]


def read_file(smell, problem, file):
    with open(f"{gold_labels_folder}/{smell}/{problem}/{file}", "r") as f:
        py_text = f.read()
    return py_text


def get_imports(py_text):
    imports = re.findall(r"from .+ import .+|import .+", py_text)
    imports = [
        imp
        for imp in imports
        if "random" not in imp and "time" not in imp and "numpy" not in imp
    ]
    create_imports = "\n".join(imports) + "\n"
    return create_imports


def get_functions_and_classes(py_text):
    tree = ast.parse(py_text)
    functions = [
        ast.unparse(node) for node in tree.body if isinstance(node, ast.FunctionDef)
    ]
    classes = [
        ast.unparse(node) for node in tree.body if isinstance(node, ast.ClassDef)
    ]

    return "\n".join(classes) + "\n" + "\n".join(functions) + "\n"


def read_energy_consumed(notebook_text):
    d = json.loads(notebook_text)

    output = d["cells"][0]["outputs"][0]["text"]

    smelly_energy = re.findall(r"total energy: (\d+\.\d+)", output[0])[0]
    refactored_energy = re.findall(r"total energy: (\d+\.\d+)", output[2])[0]

    return round(float(smelly_energy), 2), round(float(refactored_energy), 2)


def read_gold_labels():
    df = pd.DataFrame(
        columns=[
            "smelly_code",
            "refactored_code",
            "smelly_energy",
            "refactored_energy",
            "problem_name",
        ]
        + smells
    )

    counter = 0

    for smell_type in os.listdir(gold_labels_folder):
        for problem in os.listdir(f"{gold_labels_folder}/{smell_type}"):
            row = {}
            for file in os.listdir(f"{gold_labels_folder}/{smell_type}/{problem}"):
                py_text = read_file(smell_type, problem, file)
                if file.endswith(".py"):
                    # Get imports
                    create_imports = get_imports(py_text)
                    create_imports = "" if create_imports == "\n" else create_imports

                    # Get functions and classes
                    classes_functions = get_functions_and_classes(py_text)
                    created_file = create_imports + classes_functions

                    # ---> Change this to if file name starts with refactored_ else it's smelly
                    file_type = "refactored" if "refactored" in file else "smelly"

                    row[f"{file_type}_code"] = created_file

                elif file.endswith(".ipynb"):
                    smelly_energy, refactored_energy = read_energy_consumed(py_text)
                    row["smelly_energy"] = smelly_energy
                    row["refactored_energy"] = refactored_energy

            row["problem_name"] = problem
            row[smell_type] = 1
            [row.update({smell: 0}) for smell in smells if smell != smell_type]

            df.loc[counter] = row
            counter += 1
    return df


df = read_gold_labels()
df.head()