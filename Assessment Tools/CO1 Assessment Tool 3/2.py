# DFA to accept strings ending with "ab"

transitions = {
    "q0": {"a": "q1", "b": "q0"},
    "q1": {"a": "q1", "b": "q2"},
    "q2": {"a": "q1", "b": "q0"}
}

start_state = "q0"
final_state = "q2"

string = input("Enter Input String: ")

current = start_state
path = [current]

valid = True

for ch in string:
    if ch not in ["a", "b"]:
        valid = False
        break
    current = transitions[current][ch]
    path.append(current)

if not valid:
    print("Invalid Input")
else:
    print("Transition Path:", " -> ".join(path))
    if current == final_state:
        print("Accepted")
    else:
        print("Rejected")