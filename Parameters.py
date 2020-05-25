# Tabu search parameters
number_of_iterations = 50000
number_of_iterations_with_no_improvement = 250
number_of_tweaks = 10
tabu_list_length_probability = 0.0
fully_random_initial_solution = False
minimal_perturb_intensity = 50
perturbed_solution_deprecation_percentage = 0.7
insert_nodes_in_initial_solution_descending_order = True
insert_nodes_in_random_order = False
insert_nodes_in_descending_order = True
max_number_of_paths_list = [30, 40, 50, 60, 70, 80, 90, 100]
max_number_of_paths = 50
max_partial_path_length_percentage = 0.9

# Problem related parameters
node_type_selection_probability = {'subtree': 10, 'internal': 10, 'leaf': 5, 'leafs': 10, 'root': 5, 'top': 10,
                                   'bottom': 10, 'level': 5, 'path': 10, 'partial_path': 10, 'partial_path_bottom': 15}
random_walk_limit = 0.9
sub_tree_size_probability = 0.8
top_max_limit_probability = 0.8
bottom_depth_max_limit_probability = 0.05

# Instance selection
instance_type = 'exact'
start_instance_index = 23
end_instance_index = start_instance_index + 1
