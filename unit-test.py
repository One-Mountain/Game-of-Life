from game import next_state

if __name__ == '__main__':
    #dead state stays dead
    init_state1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    expected_next_state1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    #dead state becomes alive when surrounded by 3
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    #overpopulated state dies.
    init_state3 = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    expected_next_state3= [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    #underpopulated state dies
    init_state4 = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]
    expected_next_state4 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    #random state 1
    init_state5 = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 0]
    ] 
    expected_next_state5 = [
        [1, 0, 1],
        [0, 0, 1],
        [1, 1, 0]
    ]
    #random state 2
    init_state6 = [
        [0, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
    expected_next_state6 = [
        [1, 1, 1],
        [1, 0, 0],
        [1, 0, 0]
    ]
    init_states = [init_state1, init_state2, init_state3, init_state4, init_state5, init_state6]
    expected_states = [expected_next_state1, expected_next_state2, expected_next_state3,
                       expected_next_state4, expected_next_state5, expected_next_state6]
    for i in range(len(init_states)):
        actual = next_state(init_states[i])
        if actual == expected_states[i]:
            txt = f'Passes {i+1}'
            print(txt)
        else: 
            txt = f'Failed {i+1}'
            print(txt)
            print("Expected:")
            print(expected_states[i])
            print("Actual: ")
            print(actual)