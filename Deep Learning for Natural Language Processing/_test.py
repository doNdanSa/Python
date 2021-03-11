load_file_in_context("script.py")

inputs_list = [decoder_state_input_hidden, decoder_state_input_cell]

try:
  # Attempt to access a variable identifier:
  if decoder_states_inputs != inputs_list:
    fail_tests("Expected `decoder_states_inputs` to be set equal to `[decoder_state_input_hidden, decoder_state_input_cell]`.")
  
except NameError:
  fail_tests("Expected `decoder_states_inputs` to be defined.")

pass_tests()
