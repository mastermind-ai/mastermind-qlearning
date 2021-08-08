# mastermind-qlearning
uses q-learning algorithm to solve the mastermind puzzle. </br>

Built with reference to https://github.com/Amelrich/Mastermind_RL/blob/master/AI_agent.py which implements the SARSA algorithm for mastermind </br>

To get the results of average and worst performing cases using different values of epsilon</br>
`python evaluate.py`

To train an agent of a specific epsilon value based on the evaluation</br>
`python train.py <epsilon>`

To get the gameplay of the agent given a specific code: run `python qlearning.py`. This tests the saved agent on a randomly generated target

This is not implemented as we are developing the function as an endpoint directly using Flask for integration
