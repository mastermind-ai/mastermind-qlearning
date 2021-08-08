# mastermind-qlearning
uses q-learning algorithm to solve the mastermind puzzle. </br>

Built with reference to https://github.com/Amelrich/Mastermind_RL/blob/master/AI_agent.py which implements the SARSA algorithm for mastermind </br>

To get the results of average and worst performing cases using different values of epsilon</br>
`python evaluate.py`

To train an agent of a specific epsilon value based on the evaluation</br>
`python train.py <epsilon>`

To get the gameplay of the agent given a specific code: run `python qlearning.py`. This tests the saved agent on a randomly generated target

This is not implemented as we are developing the function as an endpoint directly using Flask for integration

**Epsilon Evaluation**

Run the following to evaluate the agent's performance with different epsilon values

This is done for 5 choose 4 with duplicates
```bash
python evaluation.py
```
Results

| Epsilon value       | worst case number of guesses | Average guesses |
| ------------------- | -----------------------------| --------------- |
| 0.1                 | 7                            | 4.69            |
| 0.2                 | 7                            | 4.59            |
| 0.3                 | 7                            | 4.70            |
| 0.4                 | 7                            | 4.58            |
| 0.5                 | 7                            | 4.73            |
| 0.6                 | 7                            | 4.65            |
| 0.7                 | 7                            | 4.64            |
| 0.8                 | 7                            | 4.64            |
| 0.9                 | 7                            | 4.61            |

Lowest average guess achieved: 4.58 with an epsilon value of 0.4
