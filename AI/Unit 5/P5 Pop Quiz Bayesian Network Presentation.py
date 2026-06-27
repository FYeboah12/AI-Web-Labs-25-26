import sys
def parse_input(prob_file, neh_file):
    probabilities = {}
    neighbors = {}
    all_nodes = set()  
    try:
        with open(prob_file) as p_f:
            for line in p_f:
                if ":" not in line: continue
                key, val = line.strip().split(":")
                probabilities[key.strip()] = float(val)
                clean_key = key.replace("~", "").replace("|", ",").split(",")
                for n in clean_key: 
                    if n.strip(): all_nodes.add(n.strip())
                    
        with open(neh_file) as n_f:
            for line in n_f:
                if ":" not in line: continue
                parent, children = line.strip().split(":")
                p_name = parent.strip()
                c_list = [c.strip() for c in children.split(",") if c.strip()]
                neighbors[p_name] = c_list
                all_nodes.add(p_name)
                for c in c_list: all_nodes.add(c)
    except OSError as e:
        print(f"File error: {e}")
        sys.exit()
    ordered_vars = get_topological_order(all_nodes, neighbors) #organizes by parents (top to bottom)
    return [probabilities, neighbors, ordered_vars]

def get_topological_order(nodes, neighbors):
    ordered = []
    visited = set()
    
    def visit(n):
        if n not in visited:
            visited.add(n)
            # Find children of n
            for child in neighbors.get(n, []):
                visit(child)
            ordered.insert(0, n)
            
    for node in nodes:
        visit(node)
    real_order = []
    nodes_left = list(nodes)
    while nodes_left:
        for n in nodes_left:
            parents = [p for p, children in neighbors.items() if n in children]
            if all(p in real_order for p in parents):
                real_order.append(n)
                nodes_left.remove(n)
                break
    return real_order

def get_node_prob(node, val, evidence, probs):
    for key in probs:
        if "|" in key:
            n_name, parents_str = key.split("|")
            if n_name.strip() == node:
                parents = [p.strip() for p in parents_str.split(",")]
                if all(evidence.get(p.replace("~", "")) == (not p.startswith("~")) for p in parents):
                    p_true = probs[key]
                    return p_true if val else 1.0 - p_true
        elif key.strip() == node:
            p_true = probs[key]
            return p_true if val else 1.0 - p_true
    return 1.0

def enumerate_all(vars, evidence, probs):
    if not vars: return 1.0
    Y = vars[0]
    rest = vars[1:]
    if Y in evidence:
        return get_node_prob(Y, evidence[Y], evidence, probs) * enumerate_all(rest, evidence, probs)
    else:
        total = 0
        for val in [True, False]:
            evidence[Y] = val
            total += get_node_prob(Y, val, evidence, probs) * enumerate_all(rest, evidence, probs)
        del evidence[Y]
        return total

def calculate_probability(user_input_str, graph):
    probs, neighbors, all_vars = graph
    parts = user_input_str.split("|")
    q_node = parts[0].replace("~", "").strip()
    q_val = not parts[0].strip().startswith("~")
    ev_dict = {}
    if len(parts) > 1:
        for e in parts[1].split(","):
            if not e.strip(): continue
            ev_dict[e.replace("~", "").strip()] = not e.strip().startswith("~")
    # Normalize: P(Q|E) = P(Q,E) / (P(Q,E) + P(~Q,E))
    ev_true = ev_dict.copy()
    ev_true[q_node] = True
    p_true = enumerate_all(all_vars, ev_true, probs)
    ev_false = ev_dict.copy()
    ev_false[q_node] = False
    p_false = enumerate_all(all_vars, ev_false, probs)
    if p_true + p_false == 0: return 0
    res_true = p_true / (p_true + p_false)
    return res_true if q_val else 1.0 - res_true

def main():
    p_file = input("Probabilities file (with txt): ")
    n_file = input("Neighbors file (with txt): ")
    graph = parse_input(p_file, n_file)
    print("Graph:", graph[2])
    while True:
        user_input = input("\nEnter probability or 'stop': ")
        if user_input.lower() == 'stop': break
        try:
            ans = calculate_probability(user_input, graph)
            print(f"P({user_input}) = {ans:.4f}")
        except Exception as e:
            print(f"Uh oh")

if __name__ == "__main__":
    main()
