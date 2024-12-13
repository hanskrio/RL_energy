# Deep reinforcement learning for controlling heat pumps.

## Setup Instructions for the project.

The `boptestgym` environment is used to simulate heat pump optimization scenarios for reinforcement learning tasks. Follow these steps to set up the environment:

### Prerequisites
Ensure you have the following installed on your system:
- **Python** (version 3.8 or higher)
- **Docker** (for running BOPTEST test cases)
- **pip** (Python package manager)
- **git** (to clone the repository)
- A **Unix-based system** (Linux/MacOS recommended; Windows with WSL may also work but no guarantees!)

### Installation Steps

1. Clone the Repository

git clone https://github.com/your-username/RL_energy.git
cd RL_energy

2. Install Required Python Packages

- Set up a virtual environment (recommended) and install dependencies:
python -m venv venv
source venv/bin/activate
- On Windows, use `venv\Scripts\activate`

3. Set Up BOPTEST

Follow the official instructions to set up BOPTEST:
https://github.com/ibpsa/project1-boptest

4. Set Up boptestgym

## Quick-Start (running BOPTEST locally)
You need to set up BOPTEST locally if you plan to do any meaningful work. The BOPTEST-Service code provided in https://github.com/ibpsa/project1-boptest-gym is fun to play with, but be aware that the parameters of the DQN model from Stablebaslines 3 is not set to parameters that is not supported by the literature. For example the batch size is too small and the buffer is too low (batch_size=24, buffer_size=365*24). Also the simulation runs for just 24 hours (ie. one day). 

1. Create a conda environment from the environment.yml file provided (instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)).
2. Run a BOPTEST case with the building emulator model to be controlled (instructions [here](https://github.com/ibpsa/project1-boptest/blob/master/README.md)).
3. Set up a like url = 'http://127.0.0.1:5000' from your machine to the BOPTEST server.

### Or, follow the instructions for setting up `boptestgym`from:
https://github.com/ibpsa/project1-boptest-gym

6. Run Your First Simulation

Execute a test script to ensure everything is set up correctly:
python scripts/test_boptestgym.py

Troubleshooting
- Docker connection issues: Ensure Docker is running, and the container is active.
- Port conflicts: Check if port 5000 is already in use. Modify the `-p` option in the `docker run` command if necessary (e.g., `-p 5001:5000`).
- Dependency errors: Ensure all packages in `requirements.txt` are installed without errors.
