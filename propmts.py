def count_loops_ast(code):
    """Count loops using AST parsing"""
    tree = ast.parse(code)
    return sum(isinstance(node, ast.For) or isinstance(node, ast.While)
            for node in ast.walk(tree))

def validate_refactoring(row):
    """Ensure v1 is actually improved"""
    if row['cpu_time_v1'] >= row['cpu_time_v0'] and \
       row['memory_v1'] >= row['memory_v0']:
        return False
    return True

"These seem useful, how do I use them in code?"