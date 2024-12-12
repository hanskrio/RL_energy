# Deep reinforcement learning for optimizing heat pumps.

## Setup Instructions for `boptestgym`

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

Set up a virtual environment (recommended) and install dependencies:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

3. Set Up BOPTEST

Follow the official instructions to set up BOPTEST:
https://github.com/ibpsa/project1-boptest

4. Set Up boptestgym

Follow the instructions for setting up `boptestgym`:
https://github.com/ibpsa/project1-boptest-gym

5. Configure Simulation Parameters

Edit the configuration file in `config/boptest_config.yaml` to match your simulation settings, such as:
- Test case (e.g., `bestest_hydronic_heat_pump`)
- Simulation duration and start time
- Reward function parameters

6. Run Your First Simulation

Execute a test script to ensure everything is set up correctly:
python scripts/test_boptestgym.py

Troubleshooting
- Docker connection issues: Ensure Docker is running, and the container is active.
- Port conflicts: Check if port 5000 is already in use. Modify the `-p` option in the `docker run` command if necessary (e.g., `-p 5001:5000`).
- Dependency errors: Ensure all packages in `requirements.txt` are installed without errors.
