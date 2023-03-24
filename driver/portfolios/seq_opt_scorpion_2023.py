SAS_FILE = "output.sas"
OPTIMAL = True

CONFIGS_STRIPS =  [
    # scorpion:sys-scp-interesting_non_negative-100s-cartesian-single-1M
    (1, ['--search', 'astar(scp_online([projections(sys_scp(max_time=100, max_time_per_restart=10, max_pdb_size=2M, max_collection_size=20M, pattern_type=interesting_non_negative)), cartesian(subtasks=[landmarks(order=random), goals(order=random)], max_states=infinity, max_transitions=1M, max_time=100, pick_flawed_abstract_state=first_on_shortest_path, pick_split=max_refined, tiebreak_split=min_cg, search_strategy=incremental)], saturator=perimstar, max_time=100, max_size=1M, interval=10K, orders=greedy_orders()), pruning=limited_pruning(pruning=atom_centric_stubborn_sets(), min_required_pruning_ratio=0.2))']),
]

CONFIGS_COND_EFFS = [
    # scorpion:sys-scp-interesting_non_negative-100s
    (1, ['--search', 'astar(scp_online([projections(sys_scp(max_time=100, max_time_per_restart=10, max_pdb_size=2M, max_collection_size=20M, pattern_type=interesting_non_negative, create_complete_transition_system=true), create_complete_transition_system=true)], saturator=perimstar, max_time=100, max_size=1M, interval=10K, orders=greedy_orders()))']),
]

CONFIGS_AXIOMS = [
    # scorpion:astar-blind
    (1, ['scorpion', '--search', 'astar(blind())']),
]



def get_pddl_features(task):
    has_axioms = False
    has_conditional_effects = False
    with open(task) as f:
        in_op = False
        for line in f:
            line = line.strip()
            if line == "begin_rule":
                has_axioms = True

            if line == "begin_operator":
                in_op = True
            elif line == "end_operator":
                in_op = False
            elif in_op:
                parts = line.split()
                if len(parts) >= 6 and all(p.lstrip('-').isdigit() for p in parts):
                    has_conditional_effects = True
    return has_axioms, has_conditional_effects


HAS_AXIOMS, HAS_CONDITIONAL_EFFECTS = get_pddl_features(SAS_FILE)

print(f"Task has axioms: {HAS_AXIOMS}")
print(f"Task has conditional effects: {HAS_CONDITIONAL_EFFECTS}")

if HAS_AXIOMS:
    CONFIGS = CONFIGS_AXIOMS
elif HAS_CONDITIONAL_EFFECTS:
    CONFIGS = CONFIGS_COND_EFFS
else:
    CONFIGS = CONFIGS_STRIPS
